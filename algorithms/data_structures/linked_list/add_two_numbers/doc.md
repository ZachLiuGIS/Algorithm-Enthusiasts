# Add Two Numbers Represented by LinkedList

Two non-negative numbers are represented by LinkedList. The algorithm should add the two numbers and return it
as a LinkedList

## The numbers are in natural order: single digit is at the tail

e.g 3->4->4 + 2->5->7 = 6->0->1 

344 + 257 = 601

The approach is two convert the two LinkedLists into numbers and add them together

Then return the sum as LinkedList 

3->4->4 can be converted by (3 * 10 + 4) * 10 + 4



## The numbers are in reverse order: single digit is at the head

e.g 3->4->4 + 2->5->7 = 5->9->1->1

443 + 752 = 1195

The approach is similar in approach. 

The difference is how to convert LinkedList into numbers and convert back

3->4->4 can be converted by 3 + 4 * 10 + 4 * 10^2
