Your task is to implement BFS, and dabble in the usage of the deque class from the collections library.

None of your implementations should use recursion. Yes, recursion is a good approach, and we'll cover that after the midterm. But part of learning about recursion is learning about how to do without it, so even if you're more comfortable with recursion, please avoid it for this lab. Instead, you should do everything with stacks and probably a while-loop.

I've given you a Tree class, very similar to last week's lab, but notice one weird thing: I have commented out the code to give each node a value for .parent, because you do not need .parent for this lab, and you should not use it. Other than that, the Tree class is very simple.

I've also given you a Queue class, also very simple. Notice how little work I did, relative to the Stack class from last week. My laziness is a marvel.

bfs_badqueue
Implement BFS, using the Queue class I gave you. Yes, it's sub-optimal, but do it anyway.

Every time you visit a node, put all of its children into the queue.

bfs_deque
Copy-and-paste your implementation from bfs_badqueue, and then replace the bad queue with a collections.deque.

dfs_deque
Copy-and-paste your implementation from last week's dfs_todos_goodorder, and then modify it to use the collections.deque instead. Compare and contrast with bfs_deque.

deque vs the badqueue (optional)
This is optional, but it'd be interesting to try to get a feel for whether it's worth it to use collections.deque. You could try timing some of the following things:

for various values of n, try adding n things to a queue and then removing all n things
for various values of n, try repeating the following n times: add 1 thing to the queue and then remove it
for various values of n, for j from 1 to n, add j things and then remove all the things
Does it even matter? How large does n need to be before it matters? I honestly have no idea, so if you figure it out, let me know!
