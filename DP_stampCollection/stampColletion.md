<a href="../README.md#2.5.3">Return to main page.</a>

### 2.5.3 Stamp Collection

<i>// This question comes form <a href="https://www.csee.umbc.edu/~chang/cs441/hw/hw7.shtml">Dr. Change's website for 2018FALL CMSC441 HW7. </a> </i>

<P>
You decide to write an actual letter to your grandmother --- you know, the
physical kind on real piece of paper. After detailing your latest
exploits, you discover that you don't actually have any stamps. 
You hop over to a nearby convenient store, which you seem to recall
sells stamps. You figured out that you need <i>n</i> cents of postage,
but the store only has stamps in denominations of 
<i>x</i><sub>1</sub>,
<i>x</i><sub>2</sub>,
<i>x</i><sub>3</sub>, 
...,
<i>x</i><sub><i>m</i></sub>. 
Fortunately, <i>x</i><sub>1</sub> is a 1 cent stamp, so you know you can 
definitely make <i>n</i> cents out of these stamps.
However, you want to cobble together as few stamps as possible.
</P>

<P>
Describe a dynamic programming algorithm that selects the fewest number
of stamps that make up <i>n</i> cents.
</P>


<P>
<i>Notes:</i>

<UL>
<LI> You want to make exactly <i>n</i> cents of postage --- i.e.,
do not go over <i>n</i> cents.
                
<LI> Assume the store has an adequate supply of each stamp, so
you won't run out.

<LI> Example: Suppose <i>n</i> = 14,
<i>x</i><sub>1</sub> = 1,
<i>x</i><sub>2</sub> = 4 and
<i>x</i><sub>3</sub> = 6. You can make up 14 cents using two 4-cent
stamps and one 6-cent stamp. If you tried the biggest-first strategy,
you would end up with two 6-cent stamps and two 1-cent stamps. That's
a worse solution because it uses four stamps instead of three.
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


### ***Solution：***



<a href="../README.md#2.5.3">Return to main page.</a>