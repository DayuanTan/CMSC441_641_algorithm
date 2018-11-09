<a href="../README.md#3.2.2">Return to main page.</a>

### 3.2.2 Greedy Trick or Treat

<i>// This question comes form <a href="https://www.csee.umbc.edu/~chang/cs441/hw/hw8.shtml">Dr. Chang's website for 2018FALL CMSC441 HW8. </a> </i>

<P>
Consider the following Trick-or-Treat problem.  You live on a
street with <i>n</i> houses.  You have a bag to carry your Halloween
candy, but your bag can carry at most <i>K</i> ounces of candy.
You are given for each house <i>i</i>, an integer weight
integer <i>w<sub>i</sub></i> (in ounces) of the candy that the
people in house <i>i</i> are handing out.  Each house gives out
one piece of candy.  You can visit each house at most once.  Your
problem is to collect the largest number of pieces of candy from
the <i>n</i> houses without exceeding the capacity of your bag.
</P>

<P>
Now consider the following greedy algorithm. Sort the houses
according to the weight of the candy they are providing. Collect
candy from the houses starting from the house that provides the
<em>lightest</em> candy, then the next lightest, ... until your
bag is full.
</P>

<P>
Prove by induction that this greedy strategy results in an 
optimum solution to the Trick-or-Treat problem described above.
</P>

### Solution:

#### Proof (by induction):

We induct on *n*, the number of houses, each of which provides one piece of candies, in set of houses *T* . 

<b><ins>Induction Hypothesis *P(n)*:</ins></b> The greedy alg finds the route which can collect the largest number of pieces of candies from *n* houses without exceeding the capacity of our bag.

<b><ins>Base Case: </ins></b> When we have only one house, so the resulting route provided by greedy alg will be only one house. It's obvious it mush be the best route which can collect largest number of pieces of candies.

<b><ins>Induction Step:</ins></b> **Let <i>g<sub>1</sub>, g<sub>2</sub>, g<sub>3</sub> ... g<sub>t</sub></i> be the route slected by greedy alg from set of houses *T* which has *n+1* houses** (or candies since each house provides a piece of candy). This route can collect *t* pieces of candies. 

Supposed by way of contradiction that **there exists a better route which can collect more than *t* pieces of candies from that set of houses *T* which has *n+1* houses: <i>x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub> ... x<sub>t+1</sub> </i>.** 

Without loss of geneality, assume that <i>g<sub>i</sub></i>, where *i* ranges form <i>1 to t</i>, and <i>x<sub>i</sub></i>, where *i* ranges form <i>1 to t+1</i>, are sorted increasingly by the weight of candy they are providing. 

Since <i>g<sub>1</sub></i> was chosen to be the piece of candy which has least weight, we can know <i>weight of g<sub>1</sub></i> ≤ <i>weight of x<sub>1</sub></i>. This means  <i>weight of g<sub>1</sub></i> ≤ <i>weight of x<sub>i</sub></i> for all <i>i</i> range from <i>1 to t+1</i>.

Thus we can know <i>g<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub> ... x<sub>t+1</sub> </i> is also a optimum route for the set of houses *T*. (Swap <i>g<sub>1</sub></i> for <i>x<sub>1</sub></i>.)

**Now, let *T' ⊆ T* be a new route of houses which doesn't include <i>g<sub>1</sub></i>.** Then *T'* will have at most *n* houses. By induction hypothesis, **greedy alg can find a optimum route which collect most pieces of candies (in this case is *t-1* pieces of candies): <i>g<sub>2</sub>, g<sub>3</sub>, g<sub>4</sub> ... g<sub>t</sub></i>.**

Meanwhile, <i>x<sub>2</sub>, x<sub>3</sub> ... x<sub>t+1</sub> </i> are also included in *T'*, and **they should also be a optimunm route for set *T'*.** ***But*** by the knowledge above, we know this route (<i>x<sub>2</sub>, x<sub>3</sub> ... x<sub>t+1</sub> </i>) can collect more than *t-1* pieces of candies, since <i>x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub> ... x<sub>t+1</sub> </i> can collect more than *t* pieces of candies. It collects more pieces of candies than greedy solution (<i>g<sub>2</sub>, g<sub>3</sub>, g<sub>4</sub> ... g<sub>t</sub></i>). **This contradicts the induction hypothesis.**

Therefore, there can't exist an optimum route <i>x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub> ... x<sub>t+1</sub> </i> for that set of houses *T* and <i>g<sub>1</sub>, g<sub>2</sub>, g<sub>3</sub> ... g<sub>t</sub></i> is the optimum route for the set of houses *T*. ***(Proof ends)***

<a href="../README.md#3.2.2">Return to main page.</a>