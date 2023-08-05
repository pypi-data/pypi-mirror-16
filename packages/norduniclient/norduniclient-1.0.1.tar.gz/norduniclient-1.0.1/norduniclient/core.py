# -*- coding: utf-8 -*-
#
#       core.py
#
#       Copyright 2016 Johan Lundberg <lundberg@nordu.net>
#

# This started as an extension to the Neo4j REST client made by Versae, continued
# as an extension for the official Neo4j python bindings when they were released
# (Neo4j 1.5, python-embedded).
#
# After the release of neo4j 3.0 and the bolt protocol we replaced neo4jdb-python with
# the official Neo4j driver.
#
# The goal is to make it easier to add and retrieve data from a Neo4j database
# according to the NORDUnet Network Inventory data model.
#
# More information about NORDUnet Network Inventory:
# https://portal.nordu.net/display/NI/

from __future__ import absolute_import

import re
from neo4j.v1 import GraphDatabase, basic_auth
from neo4j.v1.exceptions import ResultError, CypherError

from norduniclient import exceptions
from norduniclient import models

import logging
logger = logging.getLogger(__name__)

# Load Django settings
try:
    from django.core.exceptions import ImproperlyConfigured
    from django.conf import settings as django_settings
    try:
        NEO4J_URI = django_settings.NEO4J_RESOURCE_URI
    except ImproperlyConfigured:
        NEO4J_URI = None
except ImportError:
    NEO4J_URI = None
    logger.info('Starting up without a Django environment.')
    logger.info('Initial: norduniclient.neo4jdb == None.')
    logger.info('Use norduniclient.init_db(uri) to open a database connection.')


META_TYPES = ['Physical', 'Logical', 'Relation', 'Location']


def init_db(uri=NEO4J_URI, username=None, password=None, encrypted=False):
    if uri:
        try:
            from norduniclient.contextmanager import Neo4jDBSessionManager
            manager = Neo4jDBSessionManager(uri=uri, username=username, password=password, encrypted=encrypted)
            try:
                with manager.session as s:
                    s.run('CREATE CONSTRAINT ON (n:Node) ASSERT n.handle_id IS UNIQUE')
            except Exception as e:
                raise e
            try:
                with manager.session as s:
                    s.run('CREATE INDEX ON :Node(name)')
            except Exception as e:
                raise e
            return manager
        except Exception as e:
            logger.error('Could not connect to Neo4j database: {!s}'.format(uri))
            raise e


def get_db_driver(uri, username=None, password=None, encrypted=True, max_pool_size=50, trust=0):
    """
    :param uri: Bolt uri
    :type uri: str
    :param username: Neo4j username
    :type username: str
    :param password: Neo4j password
    :type password: str
    :param encrypted: Use TLS
    :type encrypted: Boolean
    :param max_pool_size: Maximum number of idle sessions
    :type max_pool_size: Integer
    :param trust: Trust cert on first use (0) or do not accept unknown cert (1)
    :type trust: Integer
    :return: Neo4j driver
    :rtype: neo4j.v1.session.Driver
    """
    return GraphDatabase.driver(uri, auth=basic_auth(username, password), encrypted=encrypted,
                                max_pool_size=max_pool_size, trust=trust)


def query_to_dict(manager, query, **kwargs):
    d = {}
    with manager.session as s:
        record = s.run(query, kwargs).single()
        for key, value in record.items():
            d[key] = value
    return d


def query_to_list(manager, query, **kwargs):
    l = []
    with manager.session as s:
        result = s.run(query, kwargs)
        for record in result:
            d = {}
            for key, value in record.items():
                d[key] = value
            l.append(d)
    return l


def query_to_iterator(manager, query, **kwargs):
    with manager.session as s:
        result = s.run(query, kwargs)
        for record in result:
            d = {}
            for key, value in record.items():
                d[key] = value
            yield d


def create_node(manager, name, meta_type_label, type_label, handle_id, legacy=True):
    """
    Creates a node with the mandatory attributes name and handle_id also sets type label.

    :param manager: Manager to handle sessions and transactions
    :param name: Node name
    :param meta_type_label: Node meta type
    :param type_label: Node label
    :param handle_id: Unique id
    :param legacy: Backwards compatibility

    :type manager: norduniclient.contextmanager.Neo4jDBSessionManager
    :type name: str|unicode
    :type meta_type_label: str|unicode
    :type type_label: str|unicode
    :type handle_id: str|unicode
    :type legacy: Boolean

    :rtype: dict|neo4j.v1.types.Node
    """
    if meta_type_label not in META_TYPES:
        raise exceptions.MetaLabelNamingError(meta_type_label)
    q = """
        CREATE (n:Node:%s:%s { name: { name }, handle_id: { handle_id }})
        RETURN n
        """ % (meta_type_label, type_label)
    with manager.session as s:
        if legacy:
            return s.run(q, {'name': name, 'handle_id': handle_id}).single()['n'].properties
        return s.run(q, {'name': name, 'handle_id': handle_id}).single()['n']


def get_node(manager, handle_id, legacy=True):
    """
    :param manager: Manager to handle sessions and transactions
    :param handle_id: Unique id
    :param legacy: Backwards compatibility

    :type manager: norduniclient.contextmanager.Neo4jDBSessionManager
    :type handle_id: str|unicode
    :type legacy: Boolean

    :rtype: dict|neo4j.v1.types.Node
    """
    q = 'MATCH (n:Node { handle_id: {handle_id} }) RETURN n'
    try:
        with manager.session as s:
            if legacy:
                return s.run(q, {'handle_id': handle_id}).single()['n'].properties
            return s.run(q, {'handle_id': handle_id}).single()['n']
    except ResultError:
        raise exceptions.NodeNotFound(manager, handle_id)


def get_node_bundle(manager, handle_id=None, node=None):
    """
    :param manager: Neo4jDBSessionManager
    :param handle_id: Unique id
    :type handle_id: str|unicode
    :param node: Node object
    :type node: neo4j.v1.types.Node
    :return: dict
    """
    if not node:
        node = get_node(manager, handle_id=handle_id, legacy=False)
    d = {
        'data': node.properties
    }
    labels = list(node.labels)
    labels.remove('Node')  # All nodes have this label for indexing
    for label in labels:
        if label in META_TYPES:
            d['meta_type'] = label
            labels.remove(label)
    d['labels'] = labels
    return d


def delete_node(manager, handle_id):
    """
    Deletes the node and all its relationships.

    :param manager: Neo4jDBSessionManager
    :param handle_id: Unique id

    :rtype: bool
    """
    q = """
        MATCH (n:Node {handle_id: {handle_id}})
        OPTIONAL MATCH (n)-[r]-()
        DELETE n,r
        """
    with manager.session as s:
        try:
            s.run(q, {'handle_id': handle_id}).single()
        except ResultError:
            pass
    return True


def get_relationship(manager, relationship_id, legacy=True):
    """
    :param manager: Manager to handle sessions and transactions
    :param relationship_id: Unique id
    :param legacy: Backwards compatibility

    :type manager: norduniclient.contextmanager.Neo4jDBSessionManager
    :type relationship_id: int
    :type legacy: Boolean

    :rtype int|neo4j.v1.types.Relationship
    """
    q = 'START r=relationship({relationship_id}) RETURN r'
    try:
        with manager.session as s:
            if legacy:
                return s.run(q, {'relationship_id': relationship_id}).single()['r'].properties
            return s.run(q, {'relationship_id': relationship_id}).single()['r']
    except CypherError:
        raise exceptions.RelationshipNotFound(manager, relationship_id)


def get_relationship_bundle(manager, relationship_id=None, legacy=True):
    """
    :param manager: Neo4jDBSessionManager
    :param relationship_id: Internal Neo4j id
    :param legacy: Backwards compatibility

    :type relationship_id: int
    :type legacy: bool

    :rtype: dictionary
    """
    q = '''
        START r=relationship({relationship_id})
        MATCH (start)-[r]->(end)
        RETURN start, r, end
        '''
    try:
        with manager.session as s:
            record = s.run(q, {'relationship_id': relationship_id}).single()
    except CypherError:
        raise exceptions.RelationshipNotFound(manager, relationship_id)

    if legacy:
        bundle = {
            'type': record['r'].type,
            'id': relationship_id,
            'data': record['r'].properties,
            'start': record['start'].properties['handle_id'],
            'end': record['end'].properties['handle_id'],
        }
    else:
        bundle = {
            'type': record['r'].type,
            'id': relationship_id,
            'data': record['r'].properties,
            'start': record['start'],
            'end': record['end'],
        }
    return bundle


def delete_relationship(manager, relationship_id):
    """
    Deletes the relationship.

    :param manager:  Neo4jDBSessionManager
    :param relationship_id: Internal Neo4j relationship id
    :return: bool
    """
    q = 'START r=relationship({relationship_id}) DELETE r'

    try:
        with manager.session as s:
            s.run(q, {'relationship_id': relationship_id})
    except CypherError:
        raise exceptions.RelationshipNotFound(manager, relationship_id)
    return True


def get_node_meta_type(manager, handle_id):
    """
    Returns the meta type of the supplied node as a string.

    :param manager: Neo4jDBSessionManager
    :param handle_id: Unique id
    :return: string
    """
    node = get_node(manager=manager, handle_id=handle_id, legacy=False)
    for label in node.labels:
        if label in META_TYPES:
            return label
    raise exceptions.NoMetaLabelFound(handle_id)


# TODO: Try out elasticsearch
def get_nodes_by_value(manager, value, prop=None, node_type=None):
    """
    Traverses all nodes or nodes of specified label and compares the property/properties of the node
    with the supplied string.

    :param manager: Neo4jDBSessionManager
    :param value: Value to search for
    :param prop: Which property to look for value in
    :param node_type:
    :return: dicts
    """
    if not node_type:
        node_type = 'Node'
    if prop:
        if isinstance(value, basestring):
            q = '''
                MATCH (n:{label})
                USING SCAN n:{label}
                WHERE n.{prop} =~ "(?i).*{value}.*"
                RETURN distinct n
                '''.format(label=node_type, prop=prop, value=value)
        else:
            q = '''
                MATCH (n:{label})
                USING SCAN n:{label}
                WHERE n.{prop} = {value}
                RETURN distinct n
                '''.format(label=node_type, prop=prop, value=value)

        with manager.session as s:
            for result in s.run(q):
                yield result['n']
    else:
        q = '''
            MATCH (n:{label})
            RETURN n
            '''.format(label=node_type)
        pattern = re.compile(u'.*{0}.*'.format(value), re.IGNORECASE)
        with manager.session as s:
            for result in s.run(q):
                for v in result['n'].properties.values():
                    if pattern.match(unicode(v)):
                        yield result['n']
                        break


# TODO: Try out elasticsearch
def get_nodes_by_type(manager, node_type, legacy=True):
    q = '''
        MATCH (n:{label})
        RETURN n
        '''.format(label=node_type)
    with manager.session as s:
        for result in s.run(q):
            if legacy:
                yield result['n'].properties
            else:
                yield result['n']


# TODO: Try out elasticsearch
def get_nodes_by_name(manager, name, legacy=True):
    q = '''
        MATCH (n:Node {name: {name}})
        RETURN n
        '''
    with manager.session as s:
        for result in s.run(q, {'name': name}):
            if legacy:
                yield result['n'].properties
            else:
                yield result['n']


def legacy_node_index_search(manager, lucene_query):
    """
    :param manager: Neo4jDBSessionManager
    :param lucene_query: string
    :return: dict
    """
    q = """
        START n=node:node_auto_index({lucene_query})
        RETURN collect(n.handle_id) as result
        """
    return query_to_dict(manager, q, lucene_query=lucene_query)


def get_unique_node_by_name(manager, node_name, node_type):
    """
    Returns the node if the node is unique for name and type or None.

    :param manager: Neo4jDBSessionManager
    :param node_name: string
    :param node_type: str|unicode
    :return: norduniclient node model or None
    """
    q = """
        MATCH (n:Node { name: {name} })
        WHERE {label} IN labels(n)
        RETURN n.handle_id as handle_id
        """

    with manager.session as s:
        result = list(s.run(q, {'name': node_name, 'label': node_type}))

    if result:
        if len(result) == 1:
            return get_node_model(manager, result[0]['handle_id'])
        raise exceptions.MultipleNodesReturned(node_name, node_type)
    return None


def _create_relationship(manager, handle_id, other_handle_id, rel_type, legacy=True):
    """
    :param manager: Context manager to handle transactions
    :param handle_id: Node handle id
    :param other_handle_id: Other node handle id
    :param rel_type: Relationship type
    :param legacy: Backwards compatibility

    :type manager: Neo4jDBSessionManager
    :type handle_id: str|unicode
    :type other_handle_id: str|unicode
    :type rel_type: str|unicode
    :type legacy: Boolean

    :rtype: int|neo4j.v1.types.Relationship
    """

    q = """
        MATCH (a:Node {handle_id: {start}}),(b:Node {handle_id: {end}})
        CREATE (a)-[r:%s]->(b)
        RETURN r
        """ % rel_type

    with manager.session as s:
        if legacy:
            return s.run(q, {'start': handle_id, 'end': other_handle_id}).single()['r'].id
        return s.run(q, {'start': handle_id, 'end': other_handle_id}).single()['r']


def create_location_relationship(manager, location_handle_id, other_handle_id, rel_type):
    """
    Makes relationship between the two nodes and returns the relationship.
    If a relationship is not possible NoRelationshipPossible exception is
    raised.
    """
    other_meta_type = get_node_meta_type(manager, other_handle_id)
    if other_meta_type == 'Location' and rel_type == 'Has':
        return _create_relationship(manager, location_handle_id, other_handle_id, rel_type)
    raise exceptions.NoRelationshipPossible(location_handle_id, 'Location', other_handle_id, other_meta_type, rel_type)


def create_logical_relationship(manager, logical_handle_id, other_handle_id, rel_type):
    """
    Makes relationship between the two nodes and returns the relationship.
    If a relationship is not possible NoRelationshipPossible exception is
    raised.
    """
    other_meta_type = get_node_meta_type(manager, other_handle_id)
    if rel_type == 'Depends_on':
        if other_meta_type == 'Logical' or other_meta_type == 'Physical':
            return _create_relationship(manager, logical_handle_id, other_handle_id, rel_type)
    elif rel_type == 'Part_of':
        if other_meta_type == 'Physical':
            return _create_relationship(manager, logical_handle_id, other_handle_id, rel_type)
    raise exceptions.NoRelationshipPossible(logical_handle_id, 'Logical', other_handle_id, other_meta_type, rel_type)


def create_relation_relationship(manager, relation_handle_id, other_handle_id, rel_type):
    """
    Makes relationship between the two nodes and returns the relationship.
    If a relationship is not possible NoRelationshipPossible exception is
    raised.
    """
    other_meta_type = get_node_meta_type(manager, other_handle_id)
    if other_meta_type == 'Logical':
        if rel_type in ['Uses', 'Provides']:
            return _create_relationship(manager, relation_handle_id, other_handle_id, rel_type)
    elif other_meta_type == 'Location' and rel_type == 'Responsible_for':
        return _create_relationship(manager, relation_handle_id, other_handle_id, rel_type)
    elif other_meta_type == 'Physical':
        if rel_type in ['Owns', 'Provides']:
            return _create_relationship(manager, relation_handle_id, other_handle_id, rel_type)
    raise exceptions.NoRelationshipPossible(relation_handle_id, 'Relation', other_handle_id, other_meta_type, rel_type)


def create_physical_relationship(manager, physical_handle_id, other_handle_id, rel_type):
    """
    Makes relationship between the two nodes and returns the relationship.
    If a relationship is not possible NoRelationshipPossible exception is
    raised.
    """
    other_meta_type = get_node_meta_type(manager, other_handle_id)
    if other_meta_type == 'Physical':
        if rel_type == 'Has' or rel_type == 'Connected_to':
            return _create_relationship(manager, physical_handle_id, other_handle_id, rel_type)
    elif other_meta_type == 'Location' and rel_type == 'Located_in':
        return _create_relationship(manager, physical_handle_id, other_handle_id, rel_type)
    raise exceptions.NoRelationshipPossible(physical_handle_id, 'Physical', other_handle_id, other_meta_type, rel_type)


def create_relationship(manager, handle_id, other_handle_id, rel_type):
    """
    Makes a relationship from node to other_node depending on which
    meta_type the nodes are. Returns the relationship or raises
    NoRelationshipPossible exception.
    """
    meta_type = get_node_meta_type(manager, handle_id)
    if meta_type == 'Location':
        return create_location_relationship(manager, handle_id, other_handle_id, rel_type)
    elif meta_type == 'Logical':
        return create_logical_relationship(manager, handle_id, other_handle_id, rel_type)
    elif meta_type == 'Relation':
        return create_relation_relationship(manager, handle_id, other_handle_id, rel_type)
    elif meta_type == 'Physical':
        return create_physical_relationship(manager, handle_id, other_handle_id, rel_type)
    other_meta_type = get_node_meta_type(manager, other_handle_id)
    raise exceptions.NoRelationshipPossible(handle_id, meta_type, other_handle_id, other_meta_type, rel_type)


def get_relationships(manager, handle_id1, handle_id2, rel_type=None, legacy=True):
    """
    Takes a start and an end node with an optional relationship
    type.
    Returns the relationships between the nodes or an empty list.
    """
    if rel_type:
        q = """
        MATCH (a:Node {{handle_id: {{handle_id1}}}})-[r:{rel_type}]-(b:Node {{handle_id: {{handle_id2}}}})
        RETURN collect(r) as relationships
        """.format(rel_type=rel_type)
    else:
        q = """
            MATCH (a:Node {handle_id: {handle_id1}})-[r]-(b:Node {handle_id: {handle_id2}})
            RETURN collect(r) as relationships
            """
    with manager.session as s:
        if legacy:
            relationships = s.run(q, {'handle_id1': handle_id1, 'handle_id2': handle_id2}).single()['relationships']
            return [relationship.id for relationship in relationships]
        return s.run(q, {'handle_id1': handle_id1, 'handle_id2': handle_id2}).single()['relationships']


def set_node_properties(manager, handle_id, new_properties, legacy=True):
    new_properties['handle_id'] = handle_id  # Make sure the handle_id can't be changed

    q = """
        MATCH (n:Node {handle_id: {props}.handle_id})
        SET n = {props}
        RETURN n
        """
    try:
        with manager.session as s:
            if legacy:
                return s.run(q, {'handle_id': handle_id, 'props': new_properties}).single()['n'].properties
            return s.run(q, {'handle_id': handle_id, 'props': new_properties}).single()['n']
    except ResultError:
        raise exceptions.BadProperties(new_properties)


def set_relationship_properties(manager, relationship_id, new_properties):

    q = """
        START r=relationship({relationship_id})
        SET r = {props}
        RETURN r
        """
    try:
        with manager.session as s:
            return s.run(q, {'relationship_id': relationship_id, 'props': new_properties}).single()
    except ResultError:
        raise exceptions.BadProperties(new_properties)


def get_node_model(manager, handle_id=None, node=None):
    """
    :param manager: Context manager to handle transactions
    :type manager: Neo4jDBSessionManager
    :param handle_id: Nodes handle id
    :type handle_id: str|unicode
    :param node: Node object
    :type node: neo4j.v1.types.Node
    :return: Node model
    :rtype: models.BaseNodeModel or sub class of models.BaseNodeModel
    """
    bundle = get_node_bundle(manager, handle_id, node)
    for label in bundle.get('labels'):
        try:
            classname = '{meta_type}{base}Model'.format(meta_type=bundle.get('meta_type'), base=label).replace('_', '')
            return getattr(models, classname)(manager).load(bundle)
        except AttributeError:
            pass
    for label in bundle.get('labels'):
        try:
            classname = '{base}Model'.format(base=label).replace('_', '')
            return getattr(models, classname)(manager).load(bundle)
        except AttributeError:
            pass
    try:
        classname = '{base}Model'.format(base=bundle.get('meta_type'))
        return getattr(models, classname)(manager).load(bundle)
    except AttributeError:
        return models.BaseNodeModel(manager).load(bundle)


def get_relationship_model(manager, relationship_id):
    """
    :param manager: Context manager to handle transactions
    :type manager: Neo4jDBSessionManager
    :param relationship_id: Internal Neo4j relationship id
    :type relationship_id: int
    :return: Relationship model
    :rtype: models.BaseRelationshipModel
    """
    bundle = get_relationship_bundle(manager, relationship_id)
    return models.BaseRelationshipModel(manager).load(bundle)
