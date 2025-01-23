from random import randint

# object used as element to hold data and pointer
# for the creation of a linked list of data objects
class Node:
    def __init__(self, data=None, next_n=None):
        self.data = data
        self.next = next_n


# creates a head node for a linked list
# method calls:
#               gen_list(x)                 :generates a linked list of size x
#               print_list()                :prints current linked list data elements
#               is_empty()                  :returns true if linked list is empty
#               get_data_at_index(index)    :returns data from index in linked list
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
    def __init__(self, data=None):
        self.head = Node(data)

    #generates a linked list of length "size"
    #with "data" values set to random ints
    def gen_list(self, size=1):
        if size < 1:
            print("cannot generate list smaller than 1")
        curr = self.head
        curr.data = randint(1, 9)
        for _ in range(size-1):
            temp = Node(randint(1,9))
            curr.next = temp
            curr = temp


    #############################################
    #   all methods for traversing linked list  #
    #############################################

    #prints the link list "data" elements in order from head to end
    def print_list(self):
        curr = self.head
        if self.is_empty():
            print("print_list(): List is empty")
        else:
            while curr:
                print(curr.data, end=" ")
                curr = curr.next
            print()

    # returns True if empty list
    # returns False if list exist
    def is_empty(self):
        return self.head.data == False

    # returns "data" at "index" in linked list
    def get_data_at_index(self, index):
        if self.is_empty():                                 # test if empty list
            print("get_data_at_index: List is empty")
        else:
            curr = self.head
            count = 0
            while curr:                                     #traverse list till index
                if count == index:
                    return curr.data
                else:
                    count += 1
                    curr = curr.next
        print("print index: index out of bounds")           #if index out of bounds for list
        return None

    #returns number of items in list
    def get_len(self):
        count = 0
        curr = self.head
        while curr.data:            # the head node still exist as an object even
            count += 1              # if the list is empty the data element is tested
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
            else: print("insert index: index out of bounds")

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
            print("insert data after data: Data not found")


    #################################
    #   All methods for Deletion    #
    #################################

    # delete beginning element in linked list
    def delete_begin(self):
        if self.is_empty():
            print("Delete Begin: Array is empty")       # if list is empty
        else:
            self.head = self.head.next                  # delete head node

    # delete end element in linked list
    def delete_end(self):
        if not self.head.next:                      # if list is single element
            self.head.data = None
        else:
            prev = self.head
            curr = self.head.next
            while curr.next:                        # traverse linked list till curr == end element
                prev = curr
                curr = curr.next
            prev.next = None                        # delete end element

    # delete "data" element from linked list
    def delete_data(self, key):
        curr = self.head
        if not curr:
            print("List is empty")                      # if list is empty
            pass
        if curr.data == key:                            # corner case: if key is in head element
            self.delete_begin()
        prev = curr
        curr = curr.next
        while curr:                                # traverse linked list
            if key == curr.data:                   # till key is found
                prev.next = None                   # delete pointer to "key" element
                break
            curr = curr.next
        else: print("Item not found for deletion")


def main():
    link_l = LinkedList()
    link_l.gen_list(5)
    link_l.print_list()


if __name__ == "__main__":
    main()