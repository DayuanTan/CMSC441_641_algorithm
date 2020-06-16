<a href="../README.md#3.2.4">Return to main page.</a>

### 3.2.4 Unit-length intervals (Exercise 16.2-5, page 428)

<i>// This question comes form <a href="https://www.csee.umbc.edu/~chang/cs441/hw/hw8.shtml">Dr. Chang's website for 2018FALL CMSC441 HW8. </a> </i>

### 16.2-5 
Describe an efﬁcient algorithm that, given a set <i>{x<sub>1</sub>, x<sub>2</sub>, ... , x<sub>n</sub>}</i> of points on the real line, determines the smallest set of unit-length closed intervals that contains all of the given points. Argue that your algorithm is correct.

### Solution:
1. Sort all points by the value, we ger a new array {<i>y<sub>1</sub>, y<sub>2</sub>, ... , y<sub>n</sub></i>}.
2. The first unit-length internal will be [<i>y<sub>1</sub>, y<sub>2</sub></i>].
3. For the following point, if <i>y<sub>i</sub></i> is the leftmost point not contained in any existing unit-length interval, then the next unit-length interval is [<i>y<sub>i</sub>, y<sub>i+1</sub></i>] and so forth. 

<a href="../README.md#3.2.4">Return to main page.</a>