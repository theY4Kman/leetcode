class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        # Return the longest prefix of all list elements.
        def commonprefix(m):
            "Given a list of pathnames, returns the longest common leading component"
            if not m: return ''
            s1 = min(m)
            s2 = max(m)
            for i, c in enumerate(s1):
                if c != s2[i]:
                    return s1[:i]
            return s1

        class TrieNode(object):
            def __init__(self, substring, val, children=None):
                self.substring = substring
                self.val = val
                if children is None:
                    children = []
                self._children = children

            def __str__(self):
                return self.val

            def __cmp__(self, node):
                return cmp(str(self), str(node))

            def __hash__(self):
                return hash(str(self))

            @property
            def is_leaf(self):
                return not self._children

            def matches(self, substring):
                return (self.substring.startswith(substring) or
                        substring.startswith(self.substring))

            def matches_exactly(self, substring):
                return self.substring == substring

            def is_prefix_of(self, substring):
                return substring.startswith(self.substring)

            def truncate_by(self, prefix):
                self.val = self.val[len(prefix) - 1:]

        class Trie(object):
            def __init__(self):
                #: list of TrieNode
                self.root = set()

            def _insert(self, nodes, original_val, val):
                for node in list(nodes):
                    if node.matches(val):
                        if node.matches_exactly(val):
                            return False

                        if node.is_prefix_of(val):
                            val = val[len(str(node)) - 1:]
                            new_node = TrieNode(val, original_val)
                            nodes.add(new_node)
                            return True
                        else:
                            prefix = commonprefix((str(node), val))
                            val = val[len(str(node)) - 1:]
                            new_node = TrieNode(val, original_val)
                            prefix_node = TrieNode(prefix, original_val,
                                                   [new_node, node])
                            nodes.remove(node)
                            nodes.add(prefix_node)
                            return True
                else:
                    #XXX######################################################################################
                    # TODO
                    pass


            def insert(self, val):
                """
                There are a few cases to manage:

                    1. If no node matches, create a new node
                    2. If a node partially matches another, a new Node must be
                        created with the common substring of the two existing
                        Nodes, and the existing Nodes would become children of
                        the new Node.
                    3. If an existing node's substring is the beginning of val,
                        slice val into the remaining piece, and add it as a
                        child on the existing node.
                """
                return self._insert(self.root, val, val)
