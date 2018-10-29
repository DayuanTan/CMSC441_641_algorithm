<a href="../README.md#2.5.2">Return to main page.</a>

### 2.5.2 Car Ownership

<i>// This question comes form <a href="https://www.csee.umbc.edu/~chang/cs441/hw/hw7.shtml">Dr. Change's website for 2018FALL CMSC441 HW7. </a> </i>

<P>
In this question, we consider a problem in car ownership. As a
car gets older, the maintenance costs (fuel costs, repair costs,
insurance costs, etc) for the car may increase to the extent that it
would be advantageous to sell the current car and buy a new car. The
difficulty in this problem is that the prices of new cars change from
year to year, the maintenance costs of cars purchased in different years
may be different and the resale value of a car can change from year to
year as well.</P>

<P>
For this question, you are given the following information:
<UL>
   <LI> <i>p</i>(<i>i</i>) = the price of a new car in year <i>i</i> ,
      for 1 &le; <i>i</i> &le; <i>n</i>.
   <LI> <i>v</i>(<i>i</i>, <i>k</i>) 
   = The resale value of a car purchased in year <i>i</i> and sold
     in year <i>k</i>, for 1 &le; <i>i</i> &le; <i>k</i> &leq; <i>n</i>.
   
   <LI> <i>m</i>(<i> i</i>, <i>k</i>)
    = the maintenance cost during year <i>k</i> of a car purchased in 
    year <i>i</i>, for 1 &le; <i>i</i> &le; <i>k</i> &le; <i>n</i>.
</UL>
</P>

<P>
The problem is to determine the years 
<i>y</i><sub>1</sub>, 
<i>y</i><sub>2</sub>, 
. . . , 
<i>y</i><sub><i>r</i></sub>, 
when you would purchase new cars such that the total cost of car ownership from years 1
through <i>n</i> is minimized. The total cost is the sum of the maintenance
costs for years 1 through <i>n</i> plus the price of each car purchased minus
the resale value of each car sold.
</P>
<P>
For example, if <i>n</i> = 10, 
<i>y</i><sub>1</sub> = 1, 
<i>y</i><sub>2</sub> = 5, 
<i>y</i><sub>3</sub> = 7, 
then this solution
states that you should purchase a new car in year 1, buy the second car
in year 5 and buy the third car in year 7. (You would also sell the
first car in year 5, the second car in year 7 and the third car at the
beginning of year 11.) 
</P>
<P>
In addition, you should make the following assumptions:
</P>
<P>
<UL>
<LI> You buy and sell cars at the beginning of the year.

<LI> You don't have a car before year 1. (Since you have to buy a new car
in year 1, <i>y</i><sub>1</sub> = 1 .)

<LI> You only want to purchase new cars.

<LI>  At the end of <i>n</i> years, you sell your last car for
<i>v</i>(<i>y</i><sub><i>r</i></sub> , <i>n</i> + 1) dollars.
</UL>
</P>

<P>
<i>Additional Instructions:</i> When you are asked to provide a dynamic 
programming algorithm. You <b>must</b> provide the following:
<OL>
   <LI TYPE="a"> Define a function OPT that can be used to solve
   this dynamic programming problem. To do this, you must describe
   the input parameters to OPT and the "return value" using <i>English
   sentences</i>. (Note: you are specifying the input-output relation
   of the function. You should <i>not</i> describe how to compute
   the function.) 

   <LI TYPE="a"> Give a mathematical formula that shows how OPT can
   be computed recursively. Then, explain all the major parts of
   the formula using English sentences. Remember to include the
   base cases.

   <LI TYPE="a"> Describe how OPT can be computed bottom up using
   a dynamic programming table. Be sure to include a description
   of the dimensions of the table and the order that the entries
   of the table are to be filled. Draw a diagram. Which entry has
   the solution to the original problem?

   <LI TYPE="a"> Analyze and justify the running time of your dynamic
   programming algorithm.
</OL>
</P>

<a href="../README.md#2.5.2">Return to main page.</a>