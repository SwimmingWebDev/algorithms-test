Your task is to implement DFS, two different ways, or arguably three, depending on how you look at it.

None of your implementations should use recursion. Yes, recursion is a good approach, and we'll cover that after the midterm. But part of learning about recursion is learning about how to do without it, so even if you're more comfortable with recursion, please avoid it for this lab. Instead, you should do everything with stacks and probably a while-loop.

I've given you a Tree class, very similar to last week's lab, but notice one weird thing: I have commented out the code to give each node a value for .parent, because you do not need .parent for this lab, and you should not use it. Other than that, the Tree class is very simple.

I've also given you a Stack class, also very simple. I recommend you use this Stack class, but you are welcome to choose to not use it, and build your own Stack, if you're so inclined.

dfs_stack_of_pairs
First, you should implement it where each record on the stack is a pair-of-facts:

the node that has children
the index of how far we are through visiting the children of that node.
In this representation, every time you go deeper past a node, you put that node on the stack so that you can come back to it. And when you come back to it, you need to not-repeat any children, so you've gotta have recorded somewhere something about that.

dfs_todos_badorder
This is a separate implementation strategy. The stack won't hold any index-of-children-visited, because it doesn't need to. Every time you visit a node, you put all of its children on the stack.

The thing that's a bit weird about this is that the simplest way to do it has this kinda backwards result. So probably you'll end up with that backwards result.

If you think you've achieved the right thing, but the test says it's not matching yet, maybe you just skipped ahead to the next part by mistake. Which is fine, if that happens, just figure out if it's what's really happening.

dfs_todos_goodorder
This is 95% a copy-paste from the previous one. Start by copy-pasting. And then figure out... what's the simplest thing I can do to fix the order, so that it's the same output as the dfs_stack_of_pairs function?
