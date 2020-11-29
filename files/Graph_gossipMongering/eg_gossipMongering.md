<a href="../../README.md#4.4.3">Return to main page.</a>

### 4.4.3 Gossip Mongering

<i>// This question comes form <a href="https://www.csee.umbc.edu/~chang/cs441/hw/hw10.shtml">Dr. Chang's website for 2018FALL CMSC441 HW10. </a> </i>

We represent a group of <i>n</i> people as a directed graph
<i>G</i> = (<i>V</i>, <i>E</i>) where an edge (<i>u</i>, <i>v</i>)
means that <i>u</i> will tell a "secret" to <i>v</i>. Since
it might be the case that <i>u</i> tells secrets to <i>v</i> but
<i>v</i> will not tell secrets to <i>u</i>, there may or may
not be an edge (<i>v</i>, <i>u</i>) in the other direction.

<P>
Suppose that you wanted to start some sort of rumor, something like
"They are giving away free pizza on third floor of ITE." You want
everyone to find out, but to reduce the chance of getting caught
spreading baseless rumors, you want to tell as few people as possible
yourself.  Thus, you want to identify a subset <i>C</i> of the vertices
such that for every vertex <i>v</i> in <i>G</i> there is a directed
<i>path</i> from some vertex <i>u</i> &isin; <i>C</i> to <i>v</i>.  Your
assumption is that if you tell every <i>u</i> &isin; <i>C</i> about
the free pizza, then every <i>v</i> &isin; <i>V</i> will eventually
hear the rumor (possibly through intermediaries).  Note that if <i>C</i>
is as small as possible, then there cannot be paths between two vertices
in <i>C</i>. (You didn't have to tell the rumor to one of them and
everyone would still find out.)

<OL>
   <LI TYPE="a"> Devise an algorithm to find the smallest
       set <i>C</i> with the properties described above. Describe
       your algorithm at a high level (try to avoid pseudocode).
       For full credit your algorithm should run in <i>O</i>(<i>V</i>
       &plus; <i>E</i>) time.

   <LI TYPE="a"> Argue that your algorithm is correct. That is, argue
       that for every <i>v</i> &isin; <i>V</i>, there exists <i>u</i> &isin; <i>C</i>
       such that there is a directed path from <i>u</i> to <i>v</i> in <i>G</i>.
       Then, argue that the <i>C</i> produced by your algorithm is the
       smallest possible.

   <LI TYPE="a"> State and briefly justify the running time of your
       algorithm.
</OL>

<P>
<i>Hint:</i> First, devise an algorithm for acyclic graphs. Then, generalize
your algorithm to work with graphs that may contain cycles.

<P>
<i>Note:</i> the graph does not include yourself. In particular, you do
have the option of spreading the rumor by personally telling every
vertex in the graph. However, the only case where this is the smallest
set of people to tell is when the graph has no edges at all.

<BR><HR>


</OL>

### ***Solution：***


<a href="../../README.md#4.4.3">Return to main page.</a>
