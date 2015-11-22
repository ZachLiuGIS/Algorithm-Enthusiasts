# Find Intersection of two LinkedLists

Two linked lists have intersection if they have a common node and thus all subsequent nodes are common.

The purpose of the algorithm is to detect if two input LinkedLists have intersection and return the intersection if so,
return None otherwise.

e.g. lst1: 4->5->2->10->4->3->1->2
     lst2:        3->7->4->3->1->2
     
note: the common nodes are based on reference not value

## Track common nodes backwards

Based on observation, if two lists have intersection, their last node will be the same

this solution find the last nodes of both lists, if they are different, return None.

If the last nodes are the same, extra nodes from longer list will be dropped, and then the two lists will be 
traversed one by one at the same time to find the first common node and return the intersection list.

O(N)