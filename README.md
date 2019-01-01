# Hierarchical Global Variables

Allows setting and getting of global variables organized in a dotted name hierarchy (like loggers in the logging module).
It is encouraged but not mandatory to use module names for this purpose. Each dotted name corresponds to a node.
Global variables are properties of a node. Nodes are created automatically when a property is assigned to them. When
a global variable for a given node is requested (using get), the properties of that node are checked. If the property
is defined, it returned. Otherwise the parent node is examined, and so on.

The public interface is just functions get and set.

# Documentation
See the [unit tests](https://github.com/draustin/hgv/blob/master/hgv/test_hgv.py).
