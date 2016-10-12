# Max Intersected Segment

Given a list of segment, find the max intersected segment.

e.g. [1, 3], [2, 4], [7, 8], [4, 5] should return [2, 4] because it intersects [1, 3] and [4, 5]

## Solution

sort segments by starting number, then loop through them

keep an active_segment (a hashmap) to keep track of how many intersections each segment have. When adding a segment, 
all segments currently in active_segments should be added 1 if they intersect the added segments. The segments don't 
intersect the added segment will be dropped because the rest segments won't intersect it either, so they have reached 
max number of intersections. Before drop each passed segment, compare its number with the max intersections, if larger
than max_intersection, we find a new max intersection segment.


> source: FB
