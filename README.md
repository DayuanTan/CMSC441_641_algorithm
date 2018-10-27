
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>


# CMSC441_algorithm

This is a private place where I record my review, thinking and reorganizaiton for "Algorithm" course. 



# 1. Sorting


<table>
<tr>
    <th>Time</th>
    <th><a href="https://www.codecogs.com/eqnedit.php?latex=$$\Theta(n^2)$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$\Theta(n^2)$" title="$\Theta(n^2)$" /></a> </th>
    <th><a href="https://www.codecogs.com/eqnedit.php?latex=$$\Theta(n^2)$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$\Theta(nlogn)$" title="$\Theta(n^2)$" /></a></th>
</tr>

<tr>
    <th rowspan = "3">Sorting Algorithms</th>
    <td rowspan = "2" style="border:solid 1px"><a href="./insertsort">Insert Sort (sort in place)</a></td>
    <td style="border:solid 1px"><a href="./mergesort">Merge Sort</a></td>
</tr>

<tr>
    <td style="border:solid 1px"><a href="./heapsort">Heap Sort (sort in place)</a></td>
</tr>

<tr>
    <td style="border:solid 1px"><a href="./quicksort">Quick Sort (Worst)</a></td>
    <td style="border:solid 1px"><a href="./quicksort">Quick Sort (Avg) (sort in place)</a></td>
</tr>

</table>

# 2. Dynamic Programming
“Programming” in this context refers to a tabular method, not to writing computer code.

## 2.1 Divide-and-conquer VS Dynamic progrmming alg
<table>
<tr>
    <td style="border:0px;background-color:LightGray">Divide-and-conquer alg </td>
    <td style="border:0px;background-color:LightGray" >(Solve subproblems recursively)</td>
    
</tr>

<tr>
    <td style="border:0px;background-color:LightGray"></td>    
    <td style="border:solid 1px">Dynamic Programming alg (Solve common subproblems once)</td>
</tr>
</table>


## 2.2 Four steps for Dynamic Programming alg:
1. Characterize the structure of an optimal solution.

2. Recursively deﬁne the value of an optimal solution.

3. Compute the value of an optimal solution, typically in a bottom-up fashion.

4. Construct an optimal solution from computed information.