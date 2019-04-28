from Contact import *
from week2_container import *
"""
CSCA48 Assignment 2, Summer 2018
I acknowledge that I am aware of University policy on academic integrity as
contained in https://www.utsc.utoronto.ca/aacc/academic-integrity and of the
disciplinary procedures applicable to breaches of such policy as contained
in thttp://academicintegrity.utoronto.ca/key-consequences.

I hereby declare that the code presented here is solely my work and that I
have not received any external help from my peers, nor have I used any
resources not directly supplied by the course in order to complete this
assignment. I have not looked at anyone else's solution, and no one has
looked at mine. I understand that by adding my name to this file, I am
making a formal declaration, and any subsequent discovery of plagiarism
or other academic misconduct could result in a charge of perjury in
addition to other charges under the academic code of conduct of the
University of Toronto Scarborough Campus
Name: Elton Kok
Date: 16Jul2018
"""
MAX_KEY = 3


class MSTNode():
    def __init__(self, key, value):
        ''' (MSTNode, str, Contact) -> NoneType
        Construct an MST node by the given key and value'''
        # representation invariant
        # MSTNode is a node
        # it is defined by its parent, keys that it holds, and children that
        # each key points to. Values are stored in a nested list with an index
        # that corresponds to its keys
        self._parent = None
        self._key = []
        self._value = []
        self._child = [None, None, None, None]
        self._key.append(key)
        self._value.append([value])
    # insert your code for MSTNode below this line

    def get_parent(self):
        '''(MSTNode) -> MSTNode
        Returns the parent (type MSTNode) of the given MSTNode
        '''
        return self._parent

    def get_key(self):
        '''(MSTNode) -> list of str
        Returns the keys at the given MSTNode'''
        return self._key

    def find_index(self, key):
        '''(MSTNode, str) -> int
        Returns the index of the given key in the self._key'''
        try:
            return self._key.index(key.upper())
        except:
            pass
        try:
            return self._key.index(key.lower())
        except:
            return -1

    def get_value(self):
        '''(MSTNode) -> list of Contact
        Returns the values (contacts) at the given MSTNode'''
        return self._value

    def get_child(self):
        '''(MSTNode) -> list of MSTNode
        Returns all the children of the MSTNode'''
        return self._child

    def get_child1(self):
        '''(MSTNode) -> MSTNode
        Returns the first child of the MSTNode'''
        return self._child[0]

    def get_child2(self):
        '''(MSTNode) -> MSTNode
        Returns the second child of the MSTNode'''
        return self._child[1]

    def get_child3(self):
        '''(MSTNode) -> MSTNode
        Returns the third child of the MSTNode'''
        return self._child[2]

    def get_child4(self):
        '''(MSTNode) -> MSTNode
        Returns the fourth child of the MSTNode'''
        return self._child[3]

    def get_child5(self):
        '''(MSTNode) -> MSTNode
        Returns the fifth child of the MSTNode only when overflow'''
        return self._child[4]

    def set_value(self, value):
        '''(MSTNode, Contact) -> NoneType
        Sets the value of the mst node
        '''
        self._value = value

    def set_keys(self, key):
        '''(MSTNode, list of str) -> NoneType
        Sets the keys of the mst node
        '''
        self._key = key

    def set_parent(self, new_parent):
        '''(MSTNode, MSTNode) -> NoneType
        Sets the parent of the given MSTNode to new_parent
        '''
        self._parent = new_parent

    def set_child(self, new_child):
        '''(MSTNode, list of MSTNode) -> NoneType
        Sets the new_child as the child of the MSTNode.
        '''
        self._child = new_child

    def set_child1(self, new_child):
        '''(MSTNode, MSTNode) -> NoneType
        Sets the first child of the MSTNode to new_child'''
        self._child[0] = new_child

    def set_child2(self, new_child):
        '''(MSTNode, MSTNode) -> NoneType
        Sets the second child of the MSTNode to new_child'''
        self._child[1] = new_child

    def set_child3(self, new_child):
        '''(MSTNode, MSTNode) -> NoneType
        Sets the third child of the MSTNode to new_child'''
        self._child[2] = new_child

    def set_child4(self, new_child):
        '''(MSTNode, MSTNode) -> NoneType
        Sets the fourth child of the MSTNode to new_child'''
        self._child[3] = new_child

    def has_child1(self):
        '''(MSTNode) -> bool
        Returns True if the MSTNode has a first child'''
        return self._child[0] is not None

    def has_child2(self):
        '''(MSTNode) -> bool
        Returns True if the MSTNode has a second child'''
        return self._child[1] is not None

    def has_child3(self):
        '''(MSTNode) -> bool
        Returns True if the MSTNode has a third child'''
        return self._child[2] is not None

    def has_child4(self):
        '''(MSTNode) -> bool
        Returns True if the MSTNode has a fourth child'''
        return self._child[3] is not None

    def add(self, contact):
        '''(MSTNode, Contact) -> NoneType
        Adds a Contact to the MSTNode'''
        contact_name = contact.get_name()
        contact_key = contact_name[0]
        # if the key is already in the node, we find the index of the key
        # and append the contact name to the right value list and sort the
        # values
        for key in self._key:
            if key.upper() == contact_key.upper():
                key_index = self._key.index(key)
                self._value[key_index].append(contact)
                for value in self._value:
                    self.sort_contacts(value)
                return None
        # if we finish looping through the key list and the key is not in the
        # node, then we append the contact key
        # to the key list and append the contact name to the value list
        # we then sort both lists
        self._key.append(contact_key)
        self._value.append([contact])
        self.sort_keys(self._key)
        self.sort_values(self._value)
        for value in self._value:
            self.sort_contacts(value)

    def sort_contacts(self, contact_list):
        '''(MSTNode, list of Contact) -> NoneType
        Sorts the List of contacts based on ascending alphabetical order'''
        i = 0
        # loop through list
        while i < len(contact_list) - 1:
            # if the contact name at the given index is greater than the next,
            # then swap and reset the index
            if contact_list[i].get_name().upper() > (contact_list[i+1].
                                                     get_name().upper()):
                (contact_list[i], contact_list[i+1]) = (contact_list[i+1],
                                                        contact_list[i])
                i = 0
            # else keep looking through the list
            else:
                i += 1

    def sort_keys(self, a_list):
        '''(MSTNode, list of str) -> NoneType
        Alphabetically sorts the given key_list case insensitive. This is a
        helper method.
        '''
        i = 0
        # check until the second last element of the list
        while i < len(a_list) - 1:
            # if the key at the given index is greater than the next then
            # swap and reset the index
            if a_list[i].upper() > a_list[i+1].upper():
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                i = 0
            # else keep looping through the list
            else:
                i += 1

    def sort_values(self, value_list):
        '''(MSTNode, list of list of Contacts) -> NoneType
        Alphabetically sorts the given value_list case insensitive. This is a
        helper method.
        '''
        i = 0
        # check until the second last element of the list
        while i < len(value_list) - 1:
            # since self._value holds a list of lists we need to check inside
            # each list, but nested lists will have the same first character
            # so we just need to check the first element of the nested list
            if value_list[i][0].get_name().upper() > (value_list[i+1][0].
                                                      get_name().upper()):
                value_list[i], value_list[i+1] = value_list[i+1], value_list[i]
                i = 0
            else:
                i += 1

    def search_helper(self, key, value):
        '''(MSTNode, str, Contact) -> bool
        Returns bool if the key is found in the tree. This is a helper method
        for the MST search method. This method is recursive.
        '''
        key_list = self.get_key()
        value_list = self.get_value()
        contact_name = value.get_name()
        contact_number = value.get_phone()
        child_list = self.get_child()
        # base case where we found the key in the node
        if key.upper() in key_list or key.lower() in key_list:
            i = 0
            # get the index of the key in the key_list
            while i < len(key_list):
                if key_list[i].upper() == key.upper():
                    index = i
                    i += 1
                else:
                    i += 1
            # result is false until the value is found in the value list
            result = False
            # if the value was found at the value list return true
            for contact in value_list[index]:
                if (contact.get_name().upper() == contact_name.upper() and
                        (contact.get_phone() == contact_number)):
                            result = True
        # base case 2 where the node has no children, we already checked
        # whether the key is in the node and it is not so return false
        elif all(item is None for item in child_list):
            result = False
        # recursive case
        else:
            result = False
            # in every case regardless of the number of keys, if the key we're
            # looking for is less than the first one in key list, then traverse
            # the first child
            if key.upper() < key_list[0].upper():
                if self.has_child1():
                    result = False or (self.get_child1().
                                       search_helper(key, value))
            # if the length of the key_list is 1, then we traverse to the
            # second child
            elif len(key_list) == 1:
                if self.has_child2():
                    result = False or (self.get_child2().
                                       search_helper(key, value))
            # if the length of the key list is 2 then we need to check which
            # child to traverse to
            elif len(key_list) == 2:
                # if the key is between the first and the second then traverse
                # the second child
                if key.upper() > key_list[0].upper() and (key.upper() <
                                                          key_list[1].upper()):
                    if self.has_child2():
                        result = False or (self.get_child2().
                                           search_helper(key, value))
                # else traverse the third child
                else:
                    if self.has_child3():
                        result = False or (self.get_child3().
                                           search_helper(key, value))
            # if the length of the key list is 3 we still have to check which
            # child to traverse
            elif len(key_list) == 3:
                # if the key is between the first and second, traverse second
                # child
                if key.upper() > key_list[0].upper() and (key.upper() <
                                                          key_list[1].upper()):
                    if self.has_child2():
                        result = False or (self.get_child2().
                                           search_helper(key, value))
                # if key is between the second and third, traverse third child
                elif key.upper() > key_list[1].upper() and (key.upper() <
                                                            key_list[2].
                                                            upper()):
                    if self.has_child3():
                        result = False or (self.get_child3().
                                           search_helper(key, value))
                # else traverse the fourth child
                else:
                    if self.has_child4():
                        result = False or (self.get_child4().
                                           search_helper(key, value))
        return result

    def compare_contents(self, mst_node):
        '''(MSTNode, MSTNode) -> bool
        Returns a bool which is true if the contents of the MSTNodes are the
        same. Contents are the same when they have the same keys and same
        values
        '''
        node1_keys = self.get_key()
        node2_keys = mst_node.get_key()
        node1_values = self.get_value()
        node2_values = mst_node.get_value()
        keys_same = True
        values_same = True
        # if the length of the key lists aren't the same, then they can't have
        # the same keys
        if len(node1_keys) != len(node2_keys):
            keys_same = False
        i = 0
        # if the keys lists have the same length then we check each key
        while i < len(node1_keys) and keys_same is True:
            # if the keys aren't the same letter case insensitive
            if node1_keys[i].upper() != node2_keys[i].upper():
                keys_same = False
            # else, the keys are the same and we look at the next key
            else:
                i += 1
        # if the value lists aren't the same length then, they can't have the
        # same values
        if len(node1_values) != len(node2_values):
            values_same = False
        i = 0
        # else we look through each value list that contains a nested list of
        # contacts
        while i < len(node1_values) and values_same is True:
            # if the length of the list of contacts aren't the same then the
            # values can't be the same
            if len(node1_values[i]) != len(node2_values[i]):
                values_same = False
            j = 0
            # else they have the same length of contacts and we have to check
            # if the contacts are the same
            while j < len(node1_values[i]) and values_same is True:
                # if the contact name and phone number are different then the
                # contacts aren't the same
                if (node1_values[i][j].get_name().upper() !=
                        node2_values[i][j].get_name().upper() or
                        node1_values[i][j].get_phone() != node2_values[i][j]
                        .get_phone()):
                            values_same = False
                # else the contacts have the same name and phone so we check
                # the next contact
                else:
                    j += 1
            i += 1
        # keys and values must all be the same to return True
        return keys_same and values_same

    def __eq__(self, mst_node):
        '''(MSTNode, MSTNode) -> bool
        Returns a bool which is True if the MSTNodes are the same. MSTNodes are
        equivalent if they contain same keys and same values, point to the
        same children and have the same parent.
        '''
        # check if the keys are the same
        key1 = self._key
        key2 = mst_node.get_key()
        keys_same = True
        i = 0
        # if the key list lengths aren't the same they can't be the same
        if len(key1) != len(key2):
            keys_same = False
        # loop to check each key in both lists if they are the same, the check
        # should be case insensitive
        while i < len(key1) and keys_same is True:
            if key1[i].upper() != key2[i].upper():
                keys_same = False
            else:
                i += 1
        # check if the values of both lists are the same
        value1 = self._value
        value2 = mst_node.get_value()
        values_same = True
        # if the length of the two value lists are not the same then they can't
        # be the same
        if len(value1) != len(value2):
            values_same = False
        i = 0
        # loop until end of value list
        while i < len(value1) and values_same is True:
            j = 0
            # loop for each contact in the nested value list
            while j < len(value1[i]) and values_same is True:
                # if the contacts don't have the same number and name, then
                # they are not the same contact
                if (value1[i][j].get_name().upper() !=
                    value2[i][j].get_name().upper()) or (value1[i][j].
                                                         get_phone() !=
                                                         value2[i][j].
                                                         get_phone()):
                    values_same = False
                # if they are then check the next contact
                else:
                    j += 1
            # check the next contact list in the value_list
            i += 1
        # check if the children are the same
        child1 = self._child
        child2 = mst_node.get_child()
        child_same = True
        i = 0
        # see if each item in the children list points to the same nodes
        while i < len(child1) and (child_same is True):
            # if both the children at the given index is None then they point
            # to the same child
            if child1[i] is None and child2[i] is None:
                i += 1
            # if one of the children is None while the other one is not, then
            # they don't point to the same children
            elif child1[i] is None and child2[i] is not None:
                child_same = False
            elif child1[i] is not None and child2[i] is None:
                child_same = False
            # else the two MSTNodes point to a child at the given index and we
            # compare the keys and values of that child
            elif child1[i].compare_contents(child2[i]) is False:
                # if the childs don't have the same keys and values
                child_same = False
            # else the two MSTNodes point to children that are the same and
            # we keep looking through the children list
            else:
                i += 1
        # check if they point to the same parent
        parent1 = self._parent
        parent2 = mst_node.get_parent()
        # if both parents are None then the MSTNodes point to the same parent
        if parent1 is None and parent2 is None:
            same_parent = True
        # if one parent is None while the other one is not, then they don't
        # point to the same parent
        elif parent1 is None and parent2 is not None:
            same_parent = False
        elif parent1 is not None and parent2 is None:
            same_parent = False
        # else, both nodes point to an MSTNode so we compare the parents'
        # keys and values
        elif parent1.compare_contents(parent2) is True:
            # if the parents have the same keys and values then they are the
            # same parent
            same_parent = True
        # else, then the parents don't have the same keys and values so they
        # aren't the same parent
        else:
            same_parent = False
        # all keys, values, children, and parent must be the same in order
        # for two MSTNodes to be the same
        return keys_same and values_same and child_same and same_parent

    def __str__(self):
        '''(MSTNode) -> str
        Returns a string representing the MSTNode. Gives its parent, keys
        values, and children'''
        if self._parent is not None:
            parents = 'my parent is: ' + str(hex(id(self._parent)))
        else:
            parents = 'my parent is: ' + str(self._parent)
        keys = ' my keys are: ' + str(self._key)
        names = []
        for contact_list in self._value:
            for contact in contact_list:
                names.append(contact.get_name())
        values = ' my values are: ' + str(names)
        child_list = []
        for node in self._child:
            if node is not None:
                child_values = []
                for value in node.get_value():
                    for contact in value:
                        child_values.append(contact.get_name())
                child_list.append(
                    hex(id(node))+str(node.get_key())+str(child_values))
            else:
                child_list.append(node)
        children = ' my children are: ' + str(child_list)
        return (parents + keys + values + children)


class MST():
    def __init__(self, root):
        '''(MST, MSTNode) -> NoneType'''
        self._root = root

    # insert your code for MST below this line
    def get_root(self):
        '''(MST) -> MSTNode
        Returns the root of the MST'''
        return self._root

    def set_root(self, new_root):
        '''(MST) -> MSTNode
        Sets the new root of the tree to new_root
        '''
        self._root = new_root

    def is_root(self, mst_node):
        '''(MST) -> bool
        Returns True if the mst_node is the root
        '''
        return self._root == mst_node

    def search(self, key, value):
        '''(MST, str, Contact) -> bool
        Returns True if the value was found in the MST, else False.
        '''
        # start at the root
        root = self.get_root()
        # call the recursive helper function to traverse the tree and look for
        # the key and value
        result = root.search_helper(key, value)
        return result

    def find_helper(self, node, key):
        '''(MST, MSTNode, str) -> Tuple of MSTNode
        Returns a tuple of MSTNodes, if the key is not in the MST, then returns
        (None, last node traversed) else returns the node that contains the key
        and None
        '''
        key_list = node.get_key()
        child_list = node.get_child()
        # base case 1 where we find the key at the given MSTNode
        if key.upper() in key_list or key.lower() in key_list:
            # return the pointer to the node and None
            result = node, None
        # base case 2 where we don't find the key and the MSTNode has no child
        elif all(item is None for item in child_list):
            # return None and the node
            result = None, node
        # recursive case
        else:
            # we didn't find the key so set result to None for now
            result = None, node
            # if the key is less than the first key at the node then traverse
            # the first child
            if key.upper() < key_list[0].upper():
                if node.has_child1():
                    result = self.find_helper(node.get_child1(), key)
            # if the key list at the node has only 1 and we checked if the key
            # was less than the first key so we traverse the second child
            elif len(key_list) == 1:
                if node.has_child2():
                    result = self.find_helper(node.get_child2(), key)
            # if the length of the key list is 2 then we need to check which
            # child to traverse to
            elif len(key_list) == 2:
                # if the key is between the first and the second then traverse
                # the second child
                if key.upper() > key_list[0].upper() and (key.upper() <
                                                          key_list[1].upper()):
                    if node.has_child2():
                        result = self.find_helper(node.get_child2(), key)
                # else traverse the third child
                else:
                    if node.has_child3():
                        result = self.find_helper(node.get_child3(), key)
            # if the length of the key list is 3 we still have to check which
            # child to traverse
            elif len(key_list) == 3:
                # if the key is between the first and second, traverse second
                # child
                if key.upper() > key_list[0].upper() and (key.upper() <
                                                          key_list[1].upper()):
                    if node.has_child2():
                        result = self.find_helper(node.get_child2(), key)
                # if key is between the second and third, traverse third child
                elif key.upper() > key_list[1].upper() and (key.upper() <
                                                            key_list[2].
                                                            upper()):
                    if node.has_child3():
                        result = self.find_helper(node.get_child3(), key)
                # else traverse the fourth child
                else:
                    if node.has_child4():
                        result = self.find_helper(node.get_child4(), key)
        return result

    def find(self, node, key):
        '''(MST, MSTNode, str) -> MSTNode
        Returns the pointer to the MSTNode that holds the given key. If the
        key is not found in the MST, then return None.
        '''
        # get the pointer to the nodes, node1 will point to the node that has
        # the key or None if it doesn't. Node 2 is used for the insert method
        # so it is irrelevant here
        node1, node2 = self.find_helper(node, key)
        return node1

    def insert(self, key, value):
        '''(MST, str, Contact) -> NoneType
        Inserts the key and value into the MST. If the key is in the MST, then
        insert the value to the list that holds that key's values. If the key
        is not found, insert the key into the last node that was checked and
        add the value to the list
        '''
        # initialize root
        root = self.get_root()
        # find the node that contains the key
        node1, node2 = self.find_helper(root, key)
        # if node1 is not None, that means the key exists in the tree then we
        # just add the value to the node
        if node1 is not None:
            node1.add(value)
            cur = node1
        # if node1 is None, then that means the key doesn't exist in the tree
        # we use node2 which is the node the find method terminated its search
        # at, and add the key and value to the node
        else:
            node2.add(value)
            cur = node2
        # loop until no overload or at the root
        while cur is not None and len(cur.get_key()) > 3:
            key_index = cur.find_index(key)
            # insert a dummy child since now there are 4 keys and a children
            # should have keys+1 children at a given MSTNode
            cur.get_child().insert(key_index, None)
            v_node_keys = [cur.get_key()[0], cur.get_key()[1]]
            # create the new left most node with keys 1 and 2
            v_node = MSTNode(cur.get_key()[0], cur.get_value()[0][0])
            # add all the contacts that are in the first key to the v_node
            for i in range(1, len(cur.get_value()[0])):
                v_node.add(cur.get_value()[0][i])
            # add all the contacts that are in the second key to the v_node
            for contact in cur.get_value()[1]:
                v_node.add(contact)
            # child 1, 2, and 3 from the current node becomes the children for
            # v_node's first, second, and third children
            v_node.set_child1(cur.get_child1())
            v_node.set_child2(cur.get_child2())
            v_node.set_child3(cur.get_child3())
            w_node_keys = [cur.get_key()[3]]
            # create the right node with the 4th key and value
            w_node = MSTNode(cur.get_key()[3], cur.get_value()[3][0])
            j = 1
            # add all the values at the 4th key to the new w_node
            while j < len(cur.get_value()[3]):
                w_node.add(cur.get_value()[3][j])
                j += 1
            # child's 4 and 5 of the current node becomes the children for
            # w_node's 1st and second child
            w_node.set_child1(cur.get_child4())
            w_node.set_child2(cur.get_child5())
            parent = cur.get_parent()
            # if the current node that is overflowing is the root
            if parent is None:
                # create a new root with the third key and its values
                new_root = MSTNode(cur.get_key()[2], cur.get_value()[2][0])
                j = 1
                while j < len(cur.get_value()[2]):
                    new_root.add(cur.get_value()[2][j])
                    j += 1
                # set the root the the new_root
                self.set_root(new_root)
                # set the children of the new_root node to the two nodes that
                # were just created
                new_root.set_child1(v_node)
                new_root.set_child2(w_node)
                # set their parents to new_root
                v_node.set_parent(new_root)
                w_node.set_parent(new_root)
            # else the current node that is overflowing is not the root
            else:
                # add the 3rd key's values to its parent
                for contact in cur.get_value()[2]:
                    parent.add(contact)
                # store the index where the key was inserted into the parent
                parent_key_index = parent.find_index(cur.get_key()[2])
                v_node.set_parent(parent)
                w_node.set_parent(parent)
                # remove the current node as a child from its parent
                parent.get_child().remove(cur)
                # if the key was inserted as the first key of the parent's keys
                if parent_key_index == 0:
                    # v_node becomes the first child and w_node becomes the
                    # second
                    parent.get_child().insert(0, v_node)
                    parent.get_child().insert(1, w_node)
                # if the key was inserted as the 2nd key of the parent's keys
                elif parent_key_index == 1:
                    # v_node becomes the second child, and w_node becomes the
                    # third
                    parent.get_child().insert(1, v_node)
                    parent.get_child().insert(2, w_node)
                # if the key was inserted as the 3rd key of the parent's keys
                elif parent_key_index == 2:
                    # v_node becomes the third child, and w_node becomes the
                    # fourth
                    parent.get_child().insert(2, v_node)
                    parent.get_child().insert(3, w_node)
                # if the key was the fourth
                else:
                    # V_node becomes foruth child and w_node becomes the fifth
                    parent.get_child().insert(3, v_node)
                    parent.get_child().append(w_node)
            # inactiviate the current node
            cur.set_child1(None)
            cur.set_child2(None)
            cur.set_child3(None)
            cur.set_child4(None)
            cur.set_parent(None)
            cur.set_value(None)
            cur.set_keys(None)
            # cur becomes the parent
            cur = parent

    def __eq__(self, mst_tree):
        '''(MST, MST) -> bool
        Returns True if the two trees are the same. Two trees are the same when
        they are structurally similar and all the MSTNodes at each position
        are equal to each other.
        '''
        # base case both roots don't have children
        if (all(item is None for item in self.get_root().get_child()) and
                all(item is None for item in mst_tree.get_root().get_child())):
            # if the roots are equivalent then return True, else False
                    if self.get_root() == mst_tree.get_root():
                        result = True
                    else:
                        result = False
        # base cases: if one tree has a child at the root while the other
        # doesn't then the trees can't be the same
        elif (all(item is None for item in self.get_root().get_child()) and
              all(item is None for item in mst_tree.get_root().
                  get_child() is False)):
                    result = False
        elif (all(item is None for item in self.get_root().get_child())
              is False and all(item is None for item in mst_tree.get_root().
                               get_child())):
                result = False
        # recursive case
        else:
            # if the roots are equal
            if self.get_root() == mst_tree.get_root():
                # check all their children
                # if both have child 1 then traverse child1
                if (self.get_root().has_child1() and
                        mst_tree.get_root().has_child1()):
                            result_c1 = True and (MST(self.get_root().
                                                      get_child1()) ==
                                                  MST(mst_tree.get_root().
                                                      get_child1()))
                # if one doesn't have child 1 then the result is False
                elif ((self.get_root().has_child1() and not mst_tree.get_root()
                       .has_child1()) or (not self.get_root().has_child1() and
                                          mst_tree.get_root().has_child1())):
                        result_c1 = False
                # else then they both don't have child1 and they have same
                # child 1
                else:
                    result_c1 = True
                # if both have child2 then traverse child2
                if (self.get_root().has_child2() and
                        mst_tree.get_root().has_child2()):
                            result_c2 = True and (MST(self.get_root().
                                                      get_child2()) ==
                                                  MST(mst_tree.get_root().
                                                      get_child2()))
                # if one doesn't have child 2 then result is False
                elif ((self.get_root().has_child2() and not mst_tree.get_root()
                       .has_child2()) or (not self.get_root().has_child2() and
                                          mst_tree.get_root().has_child2())):
                    result_c2 = False
                # else they both don't have child2 and they have the same
                # child 2
                else:
                    result_c2 = True
                # if both have child 3 then traverse child3
                if (self.get_root().has_child3() and
                        mst_tree.get_root().has_child3()):
                            result_c3 = (True and MST(self.get_root().
                                                      get_child3()) ==
                                         MST(mst_tree.get_root().get_child3()))
                # if one doesn't have child 3 then result is False
                elif ((self.get_root().has_child3() and not mst_tree.get_root()
                       .has_child3()) or (not self.get_root().has_child3() and
                                          mst_tree.get_root().has_child3())):
                    result_c3 = False
                # else both don't have child3 and they have the same child 3
                else:
                    result_c3 = True
                # if both have child4 then traverse child4
                if (self.get_root().has_child4() and
                        mst_tree.get_root().has_child4()):
                            result_c4 = (True and MST(self.get_root().
                                                      get_child4()) ==
                                         MST(mst_tree.get_root().get_child4()))
                # if one doesn't have child 4 then result is False
                elif ((self.get_root().has_child4() and not mst_tree.get_root()
                       .has_child4()) or (not self.get_root().has_child4() and
                                          mst_tree.get_root().has_child4())):
                    result_c4 = False
                # if both don't have child4 then result is True
                else:
                    result_c4 = True
                # must have all the same children traversed to be true
                result = result_c1 and result_c2 and result_c3 and result_c4
            # if the root nodes aren't equal then it's false
            else:
                result = False
        return result

    def BFS_helper(self):
        '''(MST) -> dict of list of MSTNodes
        Returns a dictionary where the key is the levels of the MST and
        the values are a list of MSTNodes at that level'''
        level_dict = dict()
        # use a queue to push the nodes and a level number pair-wise into the
        # queue. The format of the queue will always be in the form:
        # MSTNode->level_num->MSTNode->level-num...
        queue = Queue()
        queue.put(self.get_root())
        level_num = 0
        queue.put(level_num)
        # traverse tree using BFS
        while not queue.is_empty():
            # pop the node and its level from the queue and store it to the
            # given vars
            cur = queue.get()
            level_num = queue.get()
            # check if the nodes have children starting from the first to the
            # fourth child. If it does then push the child and level number
            # into the queue
            if cur.has_child1():
                queue.put(cur.get_child1())
                queue.put(level_num+1)
            if cur.has_child2():
                queue.put(cur.get_child2())
                queue.put(level_num+1)
            if cur.has_child3():
                queue.put(cur.get_child3())
                queue.put(level_num+1)
            if cur.has_child4():
                queue.put(cur.get_child4())
                queue.put(level_num+1)
            # build the dictionary with level number as the key and
            # list of MSTNodes as the values
            if level_num not in level_dict:
                level_dict[level_num] = [cur]
            else:
                level_dict[level_num].append(cur)
        return level_dict

    def BFS(self):
        '''(MST) -> str
        Returns a string of the MST using BFS traversal.
        '''
        result = ''
        # call the BFS helper to get a dictionary with the nodes at each
        # level
        level_dict = self.BFS_helper()
        # loop for each level of the tree
        for level in level_dict:
            # each new level should start labelling with the respective level
            result += 'Level_' + str(level) + '=['
            # go through each node at the current level
            for node in level_dict[level]:
                i = 0
                # for each key in the node
                while i < len(node.get_key()):
                    # initialize a new list to hold the contacts of that key
                    contact_list = []
                    # append the contact names to the list
                    for contact in node.get_value()[i]:
                        contact_list.append(contact.get_name())
                    # build the string with the key, and contact names
                    # remove the spaces and quotations around the strings
                    result += (node.get_key()[i] + ':' +
                               str(contact_list).replace(' ', '').
                               replace("'", "") + '-')
                    i += 1
            # after each level, remove the ending dash and add a new line
            # character
            result = result[:-1] + ']' + '\n'
        # at the end of everything, remove the new_line character
        result = result[:-1]
        return result


if __name__ == "__main__":
    kok_contact = Contact('891-293-5839', 'Kok')
    block_contact = Contact('123-392-9380', 'Block')
    b_contact = Contact('213-643-6474', 'Brian')
    a = MSTNode('K', kok_contact)
    a.add(block_contact)
    a.add(b_contact)
    a1 = MSTNode('E', 'Elton')
    kok_contact1 = Contact('891-293-5839', 'Kok')
    block_contact1 = Contact('123-392-9380', 'Block')
    b_contact1 = Contact('213-643-6474', 'Brian')
    a1 = MSTNode('K', Contact('223-234-1342', 'Kok'))
    a1.add(block_contact1)
    a1.add(b_contact1)
    print(a)
    elton = Contact('152-234-1513', 'Elton')
    b = MSTNode('E', elton)
    g = Contact('12231124', 'Eaton')
    b.add(g)
    # b.add(block_contact)
    # b.add(kok_contact)
    c = MSTNode('B', Contact('132-422-1452', 'Brian'))
    h = MSTNode('B', Contact('783-238-1599', 'Brian'))
    b.set_child1(h)
    # b.add(d)
    z = MSTNode('Z', Contact('133-234-1350', 'Zelton'))
    b.set_child2(z)
    # b.add(z)
    print(b)
    my_tree = MST(b)
    # print(my_tree.BFS())
    # b._child[0] = c
    # a==b
    # building the tree in the handout
    t_node = MSTNode('T', Contact('112-558-3359', "Tanya"))
    f_node = MSTNode('F', Contact('124-353-3559', 'Frank'))
    w_node = MSTNode('W', Contact('135-236-3593', 'Wendy'))
    r_node = MSTNode('R', Contact('125-259-2239', 'Randy'))
    f_contact = Contact('135-556-2364', 'Fred')
    n_contact = Contact('151-552-3234', 'Neda')
    w_contact1 = Contact('122-355-2589', 'Wendy')
    w_contact2 = Contact('124-125-5389', 'Will')
    r_contact1 = Contact('121-241-2124', 'Ray')
    r_contact2 = Contact('123-412-3532', 'Roy')
    s_contact = Contact('121-241-2412', 'Sheila')
    t_node.set_child1(f_node)
    t_node.set_child2(w_node)
    f_node.set_parent(t_node)
    w_node.set_parent(t_node)
    f_node.add(f_contact)
    f_node.add(n_contact)
    f_node.set_child3(r_node)
    r_node.set_parent(f_node)
    w_node.add(w_contact2)
    w_node.add(w_contact1)
    r_node.add(r_contact1)
    r_node.add(r_contact2)
    r_node.add(s_contact)
    the_tree = MST(t_node)
    # building the same tree with one node different
    t_node1 = MSTNode('T', Contact('112-558-3359', 'Tanya'))
    f_node1 = MSTNode('F', Contact('124-353-3559', 'Frank'))
    w_node1 = MSTNode('W', Contact('135-236-3593', 'Wendy'))
    r_node1 = MSTNode('R', Contact('125-259-2239', 'Randy'))
    f_contacts = Contact('135-556-2364', 'Fred')
    n_contacts = Contact('151-552-3234', 'Neda')
    w_contacts1 = Contact('122-355-2589', 'Wendy')
    w_contacts2 = Contact('124-125-5389', 'Will')
    r_contacts1 = Contact('121-241-2124', 'Ray')
    r_contacts2 = Contact('123-412-3532', 'Roy')
    s_contacts = Contact('121-241-2412', 'Sheila')
    t_node1.set_child1(f_node1)
    t_node1.set_child2(w_node1)
    f_node1.set_parent(t_node1)
    w_node1.set_parent(t_node1)
    f_node1.add(f_contacts)
    f_node1.add(n_contacts)
    f_node1.set_child3(r_node1)
    r_node1.set_parent(f_node1)
    w_node1.add(w_contacts2)
    w_node1.add(w_contacts1)
    r_node1.add(r_contacts1)
    r_node1.add(r_contacts2)
    r_node1.add(s_contacts)
    # r_node1.set_child3(MSTNode('T', Contact('154-234-6543', 'Tim')))
    # r_node1.add(Contact('943-246-1235', 'Sarah'))
    the_tree1 = MST(t_node1)
    print(the_tree.BFS())
    print(' ')
    print(the_tree1.BFS())
    print(t_node)
    the_tree1.insert('M', Contact('124-546-4354', 'Mike'))
    the_tree1.insert('O', Contact('132532', 'Opal'))
    the_tree1.insert('E', Contact('13234526', 'Elton'))
    the_tree1.insert('D', Contact('12443523', 'Dan'))
    the_tree1.insert('C', Contact('12443523', 'Cencen'))
    the_tree1.insert('B', Contact('12443523', 'Ben'))
    new_node = MSTNode('F', 'Frank')
    new_node = MSTNode('F', Contact('223950', 'Frank'))
    new_tree = MST(new_node)
    new_tree.insert('N', Contact('13253', 'Neda'))
    new_tree.insert('W', Contact('131663', 'Wendy'))
    new1 = MSTNode('R', Contact('125126', 'Randy'))
    # new_node.set_child3(new1)
    # new_tree.insert('S', Contact('62223', 'Sandy'))
    # new_tree.insert('T', Contact('62223', 'Ted'))
    # new_tree.insert('U', Contact('62223', 'Urusla'))
