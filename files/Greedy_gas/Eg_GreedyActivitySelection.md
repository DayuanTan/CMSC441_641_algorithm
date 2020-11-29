<a href="../../README.md#3.2.1">Return to main page.</a>

### 3.2.1 Greedy Activity Selection

<i>// This question comes form <a href="https://www.csee.umbc.edu/~chang/cs441/hw/hw8.shtml">Dr. Chang's website for 2018FALL CMSC441 HW8. </a> </i>

<P>
Let <i>S</i> be a schedule of <i>n</i> activities, each with a start time <i>s<sub>i</sub></i> and finish time <i>f<sub>i</sub></i>. Two activities <i>i</i> and <i>j</i> overlap if <i>s<sub>i</sub></i> ≤ <i>s<sub>j</sub></i> < <i>f<sub>i</sub></i> or <i>s<sub>j</sub></i> ≤ <i>s<sub>i</sub></i> < <i>f<sub>j</sub></i>. That is, one starts then the other one starts before the first one finishes. We want to select a subset of activities that do not overlap — let’s call such a subset <i>a proper itinerary</i>. We want to find a proper itinerary that has the largest number of activities.
</P>

We use the following greedy algorithm:
1. Pick the activity with the earliest (smallest) finish time.
2. Remove activities that overlap with the activity selected in Step 1. 
3. Repeat the process with the remaining activities.

### <a href="./Eg_GreedyActivitySelection.pdf">Solution and Proof.</a>

<a href="../../README.md#3.2.1">Return to main page.</a>
