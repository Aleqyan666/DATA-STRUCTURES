class BST:
    def __init__(self):
        self.__size = 0
        self.__root = None

    class Node:
        def __init__(self, data):
            self._data = data
            self._left = None
            self._right = None
            self._parent = None
            
        def height(self):
            if not self._right and not self._left:
                return 0
            
            rh = -1
            if self._right:
                rh = self._right.height()
            lh = -1
            if self._left:
                lh = self._left.height()

            return 1 + max(rh, lh)

        def depth(self):
            depth = 0
            temp : "BST.Node" = self._parent
            while temp:
                depth += 1
                temp = temp._parent
            return depth
        
    def contains(self, el):
        temp : "BST.Node" = self.__root
        while temp:
            if temp._data == el:
                return True
            if temp._data < el:
                temp = temp._right
            else:
                temp = temp._left

        return False

    # class LevelOrderIterator:
    #     def __init__(self, node, size):
    #         self.node : "BST.Node" = node 
    #         self.level = 0
    #         self.pointer = 0
    #         self.size = size

    #     def __next__(self):
    #         if self.pointer >= self.size:
    #             raise StopIteration

    #         if self.pointer == 0:
    #             self.pointer += 1 
    #             return self.node._data
    


    def _get_largest_node(self, node):
        if not node:
            return None
        while node._right:
            node = node._right
        return node

    def height(self, node):
        if not node:
            return -1
        return node.height()


    @staticmethod
    def _get_smallest_node(node):
        if not node:
            return None
        while node._left:
            node = node._left
        return node

    
    def remove(self, el):
        temp = self.__root
        while temp:
            if temp._data == el:
                # case 1: node does not have any children
                if temp._left == None and temp._right == None:
                    p = temp._parent
                    if p._left == temp:
                        p._left = None
                    else:
                        p._right = None
                    self.__size -= 1
                    return True
                # case 3: node has two children
                if temp._left != None and temp._right != None:
                    # largest = self._get_largest_node(temp._left)
                    smallest = self._get_smallest_node(temp._right)
                    self.remove(smallest._data)
                    temp._data = smallest._data

                    return True
                # case 1: node has one child
                # child = None
                # if temp._left:
                #     child = temp._left
                # else:
                #     child = temp._right
                child = temp._left
                if not child:
                    child = temp._right
                p = temp._parent
                if p._left == temp:
                    p._left = child
                else:
                    p._right = child
                child._parent = p
                self.__size -= 1
                return True
            if el < temp._data:
                temp = temp._left
            else:
                temp = temp._right
        return False
       

    def add(self, el) -> bool: # 13
        if self.__root == None:
            self.__root = BST.Node(el)
            self.__size += 1
            return True

        temp = self.__root
        while temp:
            if temp._data == el:
                return False
            if temp._data > el:
                if temp._left:
                    temp = temp._left
                else:
                    # n = BST.Node(el)
                    # temp._left = n
                    # n._parent = temp
                    temp._left = BST.Node(el)
                    temp._left._parent = temp
                    self.__size += 1
                    self.check_is_balanced(temp)
                    return True
            else: # temp._data < el
                if temp._right:
                    temp = temp._right
                else:
                    temp._right = BST.Node(el)
                    self.__size += 1
                    temp._right._parent = temp
                    self.check_is_balanced(temp)
                    return True

    def rotate_left(self, y):
        if not y:
            return
        x = y._right
        if not x:
            return
        T1 = x._left
        p = y._parent
        x._left = y
        y._parent = x
        y._right = T1
        if T1:
            T1._parent = y
        x._parent = p
        if not p:
            self.__root = x
        else:
            if p._left == y:
                p._left = x
            else:
                p._right = x


    def rotate_right(self, y):
        if not y:
            return
        x = y._left
        if not x:
            return
        p = y._parent
        T2 = x._right
        x._right = y
        y._parent = x
        y._left = T2
        if T2:
            T2._parent = y
        x._parent = p
        if not p:
            self.__root = x
        else:
            if p._left == y:
                p._left = x
            else:
                p._right = x

    def rebalance(self, node):
        if not node:
            return
        if self.is_balanced(node):
            return
        if self.height(node._left) > self.height(node._right):
            if self.height(node._left._right) > self.height(node._left._left):
                self.rotate_left(node._left)
            # rotate to right
            self.rotate_right(node)
        else:
            if self.height(node._right._left) > self.height(node._right._right):
                self.rotate_right(node._left)
            # rotate to left
            self.rotate_left(node)


    def check_is_balanced(self, node):
        while node:
            if not self.is_balanced(node):
                self.rebalance(node)
            node = node._parent

    def is_balanced(self, node):
        if not node:
            return True
        return abs(self.height(node._left) - self.height(node._right)) <= 1

    def print_level_order(self):
        q = []
        q.append(self.__root)
        while len(q) != 0:
            q1 = []
            for e in q:
                print(e._data, end="")
                if e._parent:
                     print("(", e._parent._data,  ")  ",end="")
                if e._left:
                    q1.append(e._left)
                if e._right:
                    q1.append(e._right)
            print()
            q = q1

    def _print_preorder_recursive(self, node):
        if not node:
            return
        print(node._data, end=", ")
        self._print_preorder_recursive(node._left)
        self._print_preorder_recursive(node._right)


    def print_preorder(self):
        self._print_preorder_recursive(self.__root)
        print()
        

    def _print_postorder_recursive(self, node):
        if not node:
            return
        self._print_postorder_recursive(node._left)
        self._print_postorder_recursive(node._right)
        print(node._data, end=", ")


    def print_postorder(self):
        self._print_postorder_recursive(self.__root)
        print()
        

    def _print_inorder_recursive(self, node):
        if not node:
            return
        self._print_inorder_recursive(node._left)
        print(node._data, end=", ")
        self._print_inorder_recursive(node._right)


    def print_inorder(self):
        self._print_inorder_recursive(self.__root)
        print()

    def _get_div_by_recursive(self, node, num):
        if not node:
            return 0
        count = 0
        if node._data % num == 0:
            count += 1
        # NOTE we can also reuse the count var and add to it the return value of the rec calls for left and right subtrees
        num_of_elems_div_by_num_left_subtree = self._get_div_by_recursive(node._left, num)
        num_of_elems_div_by_num_right_subtree = self._get_div_by_recursive(node._right, num)
        return num_of_elems_div_by_num_left_subtree + count + num_of_elems_div_by_num_right_subtree


    def get_num_of_div_by_elements(self, num):
        return self._get_div_by_recursive(self.__root, num)

    def _get_next_in_inorder(self, node):
        if not node:
            return None
        if node._right:
            return self._get_smallest_node(node._right)
        p = node._parent
        while p and p._right == node:
            node = p
            p = p._parent
        return p

    def print_inorder_iterative(self):
        if self.__root == None:
            return
        temp = self._get_smallest_node(self.__root)
        while temp:
            print(temp._data, end=", ")
            temp = self._get_next_in_inorder(temp)
        print()

    def get_num_of_div_by_elements_iterative(self, num):
        if self.__root == None:
            return 0
        count = 0
        temp = self._get_smallest_node(self.__root)
        while temp:
            if temp._data % num == 0:
                count += 1
            temp = self._get_next_in_inorder(temp)
        return count

    
    def are_all_elements_odd(self):
        if self.__root == None:
            return False
        temp = self.__root
        while temp._left:
            temp = temp._left
        while temp:
            if temp._data % 2 == 0:
                return False
            if temp._right:
                temp = temp._right
                while temp._left:
                    temp = temp._left
            else:
                p = temp._parent
                while p and p._right == temp:
                    temp = p
                    p = p._parent
                temp = p
        return True

    def print_postorder_iterative(self):
        if self.__root == None:
            return None
        # get the first element in postorder traversal - the most left leaf
        temp = self.__root
        while temp._left or temp._right:
            if temp._left:
                temp = temp._left
            else:
                temp = temp._right
        while temp:
            # put the processing here
            print(temp._data, end =", ")
            if temp._parent == None:
                temp = None
            else:
                p = temp._parent
                if temp == p._right:
                    temp = p
                elif p._right == None:
                    temp = p
                else:
                    temp = p._right
                    while temp._left or temp._right:
                        if temp._left:
                            temp = temp._left
                        else:
                            temp = temp._right
        print()


    # just binary tree not search
    # Create a recursive instance method, which finds the maximum | minimum key in
    # the Binary Tree
    def find_max_recursive(self, node : "BST.Node"):
        if node is None:
            return float("-inf")
        
        lmax = self.find_max_recursive(node._left)
        rmax = self.find_max_recursive(node._right)
        
        return max(lmax, rmax)

    def find_min_recursive(self, node : "BST.Node"):
        if node is None:
            return float("inf")
        
        lmin = self.find_min_recursive(node._left)
        rmin = self.find_min_recursive(node._right)

        return min(lmin, rmin)
    
    def get_size_recursive(self, node: "BST.Node"):
        if node is None:
            return 0
        
        left = self.get_size_recursive(node._left)
        right = self.get_size_recursive(node._right)
    
        return 1 + left + right
    
    def get_height_recursive(self, node: "BST.Node"):
        if node is None:
            return -1
        
        left = self.get_height_recursive(node._left)
        right = self.get_height_recursive(node._right)

        return 1 + max(left, right)
    
    # Create a recursive instance method that returns the size of the largest Binary
    # Search Tree subtree
    def size_of_largest_subtree(self, node: "BST.Node"):
        if node is None:
           return 0
       
        left = self.size_of_largest_subtree(node._left)
        right = self.size_of_largest_subtree(node._right)

        current_size = left + 1 + right

        return max(left, current_size, right)
    
    def mirror_tree(self, node: "BST.Node"):
        if node is None:
            return None
        
        node._left, node._right = node._right, node._left

        self.mirror_tree(node._left)
        self.mirror_tree(node._right)

        return node
    
    
    
    
class TreeMap:
    def __init__(self):
        self.__size = 0
        self.__root = None

    class Node:
        def __init__(self, key, value):
            self._key = key
            self._value = value
            self._left = None
            self._right = None
            self._parent = None

        def height(self):
            lh = self._left.height() if self._left else -1
            rh = self._right.height() if self._right else -1
            return 1 + max(lh, rh)

    def put(self, key, value):
        if self.__root is None:
            self.__root = TreeMap.Node(key, value)
            self.__size += 1
            return None

        temp = self.__root
        while temp:
            if key == temp._key:
                old_value = temp._value
                temp._value = value
                return old_value
            elif key < temp._key:
                if temp._left:
                    temp = temp._left
                else:
                    temp._left = TreeMap.Node(key, value)
                    temp._left._parent = temp
                    self.__size += 1
                    return None
            else:
                if temp._right:
                    temp = temp._right
                else:
                    temp._right = TreeMap.Node(key, value)
                    temp._right._parent = temp
                    self.__size += 1
                    return None

    def get(self, key):
        temp = self.__root
        while temp:
            if key == temp._key:
                return temp._value
            elif key < temp._key:
                temp = temp._left
            else:
                temp = temp._right
        return None

    def remove(self, key):
        temp = self.__root
        while temp:
            if key == temp._key:
                # Case 1: No children
                if not temp._left and not temp._right:
                    self.__replace_node(temp, None)
                # Case 2: Two children
                elif temp._left and temp._right:
                    successor = self.__get_min(temp._right)
                    temp._key, temp._value = successor._key, successor._value
                    self.__replace_node(successor, successor._right)
                # Case 3: One child
                else:
                    child = temp._left if temp._left else temp._right
                    self.__replace_node(temp, child)
                self.__size -= 1
                return True
            elif key < temp._key:
                temp = temp._left
            else:
                temp = temp._right
        return False

    def __replace_node(self, node, replacement):
        parent = node._parent
        if replacement:
            replacement._parent = parent
        if not parent:
            self.__root = replacement
        elif parent._left == node:
            parent._left = replacement
        else:
            parent._right = replacement

    def __get_min(self, node):
        while node and node._left:
            node = node._left
        return node

    def __get_max(self, node):
        while node and node._right:
            node = node._right
        return node

    def size(self):
        return self.__size

    def contains_key(self, key):
        return self.get(key) is not None

    def height(self):
        return self.__root.height() if self.__root else -1

    def keys(self):
        result = []
        self.__inorder_traversal(self.__root, lambda node: result.append(node._key))
        return result

    def values(self):
        result = []
        self.__inorder_traversal(self.__root, lambda node: result.append(node._value))
        return result

    def __inorder_traversal(self, node, visit):
        if not node:
            return
        self.__inorder_traversal(node._left, visit)
        visit(node)
        self.__inorder_traversal(node._right, visit)

        # TreeMap: Create a recursive instance method that calculates the sum of the keys.
    def treemap_sum_of_keys_recursive(self, node: "TreeMap.Node"):
        if node is None:
            return 0
        
        left_key_sum = self.treemap_sum_of_keys_recursive(node._left) # left_tree_sum 
        right_key_sum = self.treemap_sum_of_keys_recursive(node._right)# right_tree_sum

        return left_key_sum + node._key + right_key_sum
    
    def find_maximum_key(self, node: "TreeMap.Node"):
        if node is None:
            return float('-inf')
        
        left = self.find_maximum_key(node._left)
        right = self.find_maximum_key(node._right)

        return max(left, node._key, right)
    
    def find_minimum_key(self, node: "TreeMap.Node"):
        if node is None:
            return float("inf")
        
        left = self.find_minimum_key(node._left)
        right = self.find_minimum_key(node._right)

        return max(left, node._key, right)
    
    

        



bst = BST()
bst.add(10)
bst.add(11)
bst.add(12)
bst.print_level_order()

bst.add(25)
bst.add(23)
bst.print_level_order()

# bst.add(35)
# bst.add(33)
# bst.add(42)
# bst.add(13)
# bst.add(10)
# bst.add(11)
# bst.add(14)
# bst.add(5)
# bst.add(55)
# bst.add(65)
# # bst.remove(15)
# bst.print_level_order()
# print("Print the tree using preorder traversal")
# bst.print_preorder()
#
# print("Print the tree using postorder traversal")
# bst.print_postorder()
#
# print("Print the tree using inorder traversal")
# bst.print_inorder()
# print(bst.get_num_of_div_by_elements(5 ))
# #
# print("Print the tree using inorder iterative traversal")
# #
# bst.print_inorder_iterative()
# print(bst.get_num_of_div_by_elements_iterative(1))
# print(bst.are_all_elements_odd())
#
# bst1 = BST()
# bst1.add(11)
# bst1.add(1)
# bst1.add(3)
# print(bst1.are_all_elements_odd())
#
#
# print("Print the tree using postorder iterative traversal")
# bst.print_postorder_iterative()
# #
# # it = bst.get_inorder_iterator()
# # for e in it:
# #     print(e)
# #
# # it = bst.get_inorder_iterator()
# # while True:
# #     try:
# #         print(next(it))
# #     except StopIteration:
# #         break
#



