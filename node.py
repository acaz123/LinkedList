from logging import exception
from random import randint

# object used as element to hold data and pointer
# for the creation of a linked list of data objects
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


# creates a head node for a linked list
# method calls:
#               gen_list(x)                 :generates a linked list of size x
#               print_list()                :prints current linked list data elements
#               is_empty()                  :returns true if linked list is empty
#               get_data_index(index)    :returns data from index in linked list
#               get_len()                   :returns the length of linked list
#
# insert:       insert_begin(data)          :inserts data at beginning of linked list
#               insert_end(data)            :inserts data at the end of linked list
#               insert_index(i, data)       :inserts data at index=i in linked list
#               insert_after_data(key, data):inserts data after key in linked list
#
# delete        delete_data(key)            :deletes key from linked list
#               delete_end()                :deletes last item in linked list
#               delete_begin()              :deletes first item in linked list
#
class LinkedList:
    def __init__(self):
        self.head = None

    # used for testing and debugging
    # generates a linked list of length "size"
    # with "data" values set to random ints
    # if elements of the list already exist they will be overwritten
    def gen_list(self, size=1):
        assert size > 0, "cannot generate list smaller than 1"
        if self.is_empty():
            self.head = Node(randint(1,9))
        curr = self.head
        for _ in range(size-1):                 # -1 since head node is already created
            temp = Node(randint(1,9))
            curr.next = temp
            curr = temp


    #############################################
    #   all methods for traversing linked list  #
    #############################################


    # prints the link list "data" elements in order from head to end
    def print_list(self):
        curr = self.head
        if self.is_empty():
            print("print_list(): List is empty")
        else:
            while curr:
                try:
                    print(curr.data, end=" ")
                    curr = curr.next
                except TypeError:
                    print("invalid data type to print")
            print()

    # returns True if empty list
    # returns False if list exist
    def is_empty(self):
        return self.head == None

    # returns "data" at "index" in linked list
    def get_data_index(self, index):
        if index > self.get_len() - 1:
            raise IndexError("insert_index: index out of bounds")
        curr = self.head
        count = 0
        while curr:                                     #traverse list till index
            if count == index:
                return curr.data
            else:
                count += 1
                curr = curr.next

    #returns number of items in list
    def get_len(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    ################################
    #   all methods for insertion  #
    ################################

    #inserts "data" at beginning of linked list
    def insert_begin(self, data):
        new_head = Node(data)
        if self.is_empty():                         # corner case if list is empty
            self.head = new_head
        else:
            new_head.next = self.head               # replace head with data element
            self.head = new_head

    #inserts "data" at end of linked list
    def insert_end(self, data):
        new_end = Node(data)
        if self.is_empty():                         # corner case if list is empty
            self.head = new_end
        else:
            curr = self.head
            while curr.next:                        # traverse linked list
                curr = curr.next                    # till end element
            curr.next = new_end                     # add data element to end of list

    #insert "data" at "index" in linked list
    def insert_index(self, index, data):
        if index > self.get_len() - 1:
            raise IndexError("insert_index: index out of bounds")
        if index == 0:                                      # corner case if index == 0
            self.insert_begin(data)
        else:
            curr_index = 1
            prev = self.head
            curr = prev.next
            while curr:                                     # traverse linked list
                if index == curr_index:                     # till index element
                    temp = Node(data, curr)                 # insert data at index
                    prev.next = temp
                    break
                prev = curr
                curr = curr.next
                curr_index += 1

    #insert "data_insert" after "data_key"
    def insert_after_data(self, data_key,  data_insert):
        curr = self.head
        while curr:                             # begin traversing list from head element down
            if curr.data == data_key:           # when data_key is found
                temp = Node(data_insert)        # data_insert is inserted after
                temp.next = curr.next
                curr.next = temp
                break
            else:
                curr = curr.next
        else:
            raise KeyError("insert_data_after_data: data_key not found")


    #################################
    #   All methods for Deletion    #
    #################################

    # delete beginning element in linked list
    def delete_begin(self):
        if self.is_empty():
            raise exception("delete_begin(): cannot delete from empty list")    # if list is empty
        else:
            self.head = self.head.next                  # delete head node

    # delete end element in linked list
    def delete_end(self):
        assert self.head, "delete_begin(): cannot delete from empty list"
        if not self.head.next:                      # if list is single element
            self.head = None
        else:
            prev = self.head
            curr = self.head.next
            while curr.next:                        # traverse linked list till end of list
                prev = curr
                curr = curr.next
            prev.next = None                        # delete end element

    # delete "data" element from linked list
    def delete_data(self, key):
        assert self.head, "delete_data: cannot delete from empty list"
        curr = self.head
        if curr.data == key:                          # corner case: if key is in head element
            self.delete_begin()
        prev = curr
        curr = curr.next
        while curr:                                     # traverse linked list
            if key == curr.data:                        # till key is found
                prev.next = curr.next                   # delete pointer to "key" element
                break
            prev = curr
            curr = curr.next
        else:
            raise KeyError


# method calls:
#               gen_list(x)                 :generates a linked list of size x
#               print_list()                :prints current linked list data elements
#               is_empty()                  :returns true if linked list is empty
#               get_data_index(index)    :returns data from index in linked list
#               get_len()                   :returns the length of linked list
#
# insert:       insert_begin(data)          :inserts data at beginning of linked list
#               insert_end(data)            :inserts data at the end of linked list
#               insert_index(i, data)       :inserts data at index=i in linked list
#               insert_after_data(key, data):inserts data after key in linked list
#
# delete        delete_data(key)            :deletes key from linked list
#               delete_end()                :deletes last item in linked list
#               delete_begin()              :deletes first item in linked list
def main():
    link_l = LinkedList()
    link_l.gen_list(5)
    link_l.print_list()

if __name__ == "__main__":
    main()