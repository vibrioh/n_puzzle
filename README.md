# N-puzzle solver

### This is an implementation of search algorithms for solving N-puzzle problem.


## USEAGE

```$ python3 driver.py <method> <board>```

```<method>```:
* bfs (Breadth-First Search) 
* dfs (Depth-First Search) 
* ast (A-Star Search)
* ida (IDA-Star Search)

```<board>```:

0,8,7,6,5,4,3,2,1 indicates a 3*3 board:
```
0 8 7
6 5 4
3 2 1
```

e.g. ```$ python3 driver.py bfs 0,8,7,6,5,4,3,2,1``` will generate an 'output.txt' showing:

```path_to_goal: ['down', 'right', 'down', 'right', 'up', 'up', 'left', 'down', 'down', 'right', 'up', 'up', 'left', 'down', 'down', 'left', 'up', 'up', 'right', 'down', 'down', 'left', 'up', 'right', 'down', 'right', 'up', 'left', 'up', 'left']
cost_of_path: 30
nodes_expanded: 181423
fringe_size: 16
max_fringe_size: 24048
search_depth: 30
max_search_depth: 31
running_time: 7.56677500
max_ram_usage: 66.02734375
```


## SCRIPT

* Run

```chmod 700 script.sh```

```./script.sh```

* Test cases will show:

```===========
Test case:3,1,2,0,4,5,6,7,8
===========
bfs cmp to bfs1.txt
1c1
< path_to_goal: ['up']
---
> path_to_goal: ['Up']
8,9c8,9
< running_time: 0.00021300
< max_ram_usage: 0.01953125
---
> running_time: 0.00000000
> max_ram_usage: 0.00000000
dfs cmp to dfs1.txt
1c1
< path_to_goal: ['up']
---
> path_to_goal: ['Up']
7,9c7,9
< max_search_depth: 0
< running_time: 0.00017900
< max_ram_usage: 0.01562500
---
> max_search_depth: 1
> running_time: 0.00000000
> max_ram_usage: 0.00000000
ast cmp to ast1.txt
1c1
< path_to_goal: ['up']
---
> path_to_goal: ['Up']
8,9c8,9
< running_time: 0.00031500
< max_ram_usage: 0.01953125
---
> running_time: 0.00000000
> max_ram_usage: 0.00000000
ida cmp to ida1.txt
1c1
< path_to_goal: ['up']
---
> path_to_goal: ['Up']
8,9c8,9
< running_time: 0.00071700
< max_ram_usage: 0.01953125
---
> running_time: 0.00000000
> max_ram_usage: 0.00000000
===========
Test case:1,2,5,3,4,0,6,7,8
===========
bfs cmp to bfs2.txt
1c1
< path_to_goal: ['up', 'left', 'left']
---
> path_to_goal: ['Up', 'Left', 'Left']
8,9c8,9
< running_time: 0.00114700
< max_ram_usage: 0.04687500
---
> running_time: 0.00000000
> max_ram_usage: 0.00000000
dfs cmp to dfs2.txt
1c1
< path_to_goal: ['up', 'left', 'left']
---
> path_to_goal: ['Up', 'Left', 'Left']
8,9c8,9
< running_time: 7.07642500
< max_ram_usage: 74.79687500
---
> running_time: 0.00000000
> max_ram_usage: 0.00000000
ast cmp to ast2.txt
1c1
< path_to_goal: ['up', 'left', 'left']
---
> path_to_goal: ['Up', 'Left', 'Left']
8,9c8,9
< running_time: 0.00048400
< max_ram_usage: 0.01953125
---
> running_time: 0.00000000
> max_ram_usage: 0.00000000
ida cmp to ida2.txt
1c1
< path_to_goal: ['up', 'left', 'left']
---
> path_to_goal: ['Up', 'Left', 'Left']
8,9c8,9
< running_time: 0.00150000
< max_ram_usage: 0.01953125
---
> running_time: 0.00000000
> max_ram_usage: 0.00000000
```