import collections
import sys
import helper

if __name__=='__main__':
    linked_list = collections.deque()
    linked_list.append('element 0')
    linked_list.append(sys.argv[1])
    linked_list.append('element 2')

    linked_list_copy = linked_list.copy()

    helper.run_cmd(linked_list_copy.popleft())