from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key, value):
        if self.value is None:
            self.value == value
        # Override existing key.
        if self.key == key:
            self.value = value

        elif self.value is None:
            self.key = key
            self.value = value

        elif key < self.key:
            if self.left is None:
                self.left = Node(key, value, None, None)

            else:

                self.left.put(key, value)

        else:
            if self.right is None:
                self.right = Node(key, value, None, None)

            else:
                self.right.put(key, value)

    def to_string(self):

        s = ''

        if self.left:
            s += self.left.to_string()

        s += '( ' + str(self.key) + ', ' + str(self.value) + ') '

        if self.right:
            s += self.right.to_string()

        return s

    def count(self):
        pass       # Placeholder code ==> to be replaced

    def get(self, key):

        if self.key == key:
            return self.value

        elif key < self.key:
            if self.left:
                return self.left.get(key)

        elif key > self.key:
            if self.right:
                return self.right.get(key)

        else:
            return 'None'

    def max_depth(self):

        # Start from one because if we have for example only...
        # one node to the left then we check if left node exist...
        # and we recurse the function in that only left node which
        # it will return 0 as there are no nodes attached to it.
        # and that will give us 1 node
        left_depth = 1
        right_depth = 1
        if self is None:
            return 0
        else:

            if self.left:
                left_depth += self.left.max_depth()
            if self.right:
                right_depth += self.right.max_depth()

        if left_depth > right_depth:
            return left_depth
        else:
            return right_depth


    def count_leafs(self):
        left_leafs = 0
        right_leafs = 0
        if self is None:
            return 0
        if (self.left is None) and self.right is None:
            return 1
        else:
            if self.left:
                left_leafs += self.left.count_leafs()
            if self.right:
                right_leafs += self.right.count_leafs()
            return left_leafs + right_leafs
        # We do a left-to-right in-order traversal of the tree
        # to get the key-value pairs sorted base on their keys

    def as_list(self, lst):

        if self.left:
            self.left.as_list(lst)

        t = (self.key, self.value)

        if len(t[0]) > 4:
            lst.append(t)

        if self.right:
            self.right.as_list(lst)

        return lst

# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)

    def count_leafs(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()