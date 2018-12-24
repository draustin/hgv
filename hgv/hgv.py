"""Hierarchical Global Variables

Allows setting and getting of global variables organized in a dotted name hierarchy (like loggers in the logging module).
It is encouraged but not mandatory to use module names for this purpose. Each dotted name corresponds to a node.
Global variables are properties of a node. Nodes are created automatically when a property is assigned to them. When
a global variable for a given node is requested (using get), the properties of that node are checked. If the property
is defined, it returned. Otherwise the parent node is examined, and so on.

The public interface is just functions get and set.
"""
from collections import defaultdict


class Node:
    def __init__(self, nodes=None, properties=None):
        if nodes is None:
            nodes = defaultdict(Node)
        if properties is None:
            properties = {}
        self.nodes = nodes
        self.properties = properties


root = Node()


def split_node_key(node_key):
    if node_key is None:
        return []
    else:
        return node_key.split('.')

def get(node_key:str, property_name:str, default=None):
    """Lookup value of a property in the hierarchy.

    Args:
        node_key: dotted name, typically a module's  __name__ attribute.
        property_name: the global variable's name e.g. 'lut' for pyqtgraph colormap lookup table default.
        default: default value to return if property not found

    Returns:
        property value
    """
    node_names = split_node_key(node_key)
    node = root
    try:
        property = node.properties[property_name]
    except KeyError:
        property = default
    for node_name in node_names:
        try:
            node = node.nodes[node_name]
        except KeyError:
            break
        try:
            property = node.properties[property_name]
        except KeyError:
            pass
    return property


def set(node_key:str, property_name:str, value):
    """Set propety in the hierarchy.

    Args:
        node_key: dotted name, typically a module's  __name__ attribute.
        property_name: the global variable's name e.g. 'lut' for pyqtgraph colormap lookup table default.
        value: value to which property is set.
    """
    node_names = split_node_key(node_key)
    node = root
    for node_name in node_names:
        node = node.nodes[node_name]
    node.properties[property_name] = value
