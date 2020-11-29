<a href="../../README.md#4.2.1">Return to main page.</a>

### 4.2.1 Two Coloring

<i>// This question comes form <a href="https://www.csee.umbc.edu/~chang/cs441/hw/hw9.shtml">Dr. Chang's website for 2018FALL CMSC441 HW9. </a> </i>

<P>
You are given a connected undirected graph <i>G</i> = (<i>V</i>,
<i>E</i>&thinsp;) as an adjacency list.  You are asked to assign either the
color red or the color blue to each vertex of the graph except that you
are not allowed to color two vertices the same color if those two
vertices are adjacent (i.e., two vertices that are connected by
an edge must be assigned different colors).


<UL>
<P><LI>
Describe an algorithm that either makes the appropriate color assignments or 
determines that the task is impossible.

<P><LI>
Briefly justify the correctness of your algorithm. That is, argue that
your algorithm will never assign adjacent vertices the same color
<i>and</i> that when your algorithm declares the task is impossible then
it is actually impossible.

<P><LI>
State and briefly justify the running time of your algorithm.

For full credit, your algorithm should run in <i>O</i>(<i>V</i> &plus;
<i>E</i>&thinsp;) time.
</UL>

<BR><HR>

### ***Solution：***

Use Breadth First Search (BFS). // Original BFS running time is O(V+E).
```
For each vertexes:
    1. Get a vertex, color it one color. 
    2. BFS to its 1-degree-distance vertexes:
        If there are any two of them connected directly, then it's impossible. 
        Else, color them another color. 
EndFor. 
```

<img src="graph_2color.jpg">

### ***Proof:***
As shown in above figure. Assume there are two vertexes at same level connected to each other directly. The distance to their common parents is k. Then the perimeter of this three-vertexes-loop will be 2k+1. It is obvious that we cannot two coloring a 2k+1 loop graph.

<a href="../README.md#4.2.1">Return to main page.</a>