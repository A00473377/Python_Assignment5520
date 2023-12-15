#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:07:58 2023
Description: SOLUTION FOR QUESTION1
    stack - This function takes multiple arguments, then based on provided arguments, it either adds the element like a stack
            removes the element from the stack.
    queue - This function similarly takes multiple arguments but instead behaves like a queue.
@author: zaidshaikh
"""

"""

performs the operation mentioned in one of the argument. It tries to resembles stack. 
"""
def stack(our_list, operation_name, new_element=None):
    if operation_name == 'add':
        our_list.insert(0, new_element) if new_element is not None else print("NO ELEMENT PROVEDED TO ADD")
    elif operation_name == 'remove':
        if not our_list:
            print("List is empty, cannot remove.")
        else:
            our_list.pop(0)
    else:
        print("Invalid operation for Stack method")
    return our_list

def queue(our_list, operation_name, new_element=None):
    if operation_name == 'add':
        our_list.append(new_element) if new_element is not None else print("NO ELEMENT PROVEDED TO ADD")
    elif operation_name == 'remove':
        if not our_list:
            print("List is empty, cannot remove.")
        else:
            our_list.pop(0)
    else:
        print("Invalid operation for queue method")
    return our_list

new_list =[1,2,3,4]
new_list2 =[6,7,8,9]

#Calling the stack method to add the element to the list
new_list = stack(new_list,'add',0)
print(new_list)

#calling the queue method to add element to the list
new_list2 = queue(new_list2,'add',0)
print(new_list2)

#calling the stack method to remove the element from the list
new_list =stack(new_list,'remove')
print(new_list)

#calling the queue method to remove the element from the list
new_list2 =queue(new_list2,'remove')
print(new_list2)
