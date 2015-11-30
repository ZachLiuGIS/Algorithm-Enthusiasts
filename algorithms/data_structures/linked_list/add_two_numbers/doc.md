# Add Two Numbers Represented by LinkedList

Two non-negative numbers are represented by LinkedList. The algorithm should add the two numbers and return it
as a LinkedList

## The numbers are in natural order: single digit is at the tail

e.g 3->4->4 + 2->5->7 = 6->0->1 

344 + 257 = 601

The approach is two convert the two LinkedLists into numbers and add them together

Then return the sum as LinkedList 

3->4->4 can be converted by (3 * 10 + 4) * 10 + 4

O(m + n)



## The numbers are in reverse order: single digit is at the head

e.g 3->4->4 + 2->5->7 = 5->9->1->1

443 + 752 = 1195

The approach is similar in approach. 

The difference is how to convert LinkedList into numbers and convert back

3->4->4 can be converted by 3 + 4 * 10 + 4 * 10^2

O(m + n)


## Adding up digits - reverse order

This can be done without converting between numbers and LinkedLists.

Because the single digits need to be added first, the input need to be reversed first

loop through digits of the two LinkedLists and build the digit

if the sum of a single digit if 10 or more, add 1 to the next digit

if both lists have no more digits and no more 1 added from previous digit, it is finished

return the list


## Adding up digits - reverse order

loop through digits of the two LinkedLists and build the digit

if the sum of a single digit if 10 or more, add 1 to the next digit

if both lists have no more digits and no more 1 added from previous digit, it is finished

the result need to be reversed





