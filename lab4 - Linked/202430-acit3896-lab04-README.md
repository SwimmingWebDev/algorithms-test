

This lab is about implementing the LinkedList.

We need a thing to hold onto for the individual nodes of our LinkedList, and once we build those we more or less do not need a container for the whole list, so your assignment is just to create a LinkedListNode class.

Part 2 is graded, part 3 is optional.


## Part 1 : LinkedListNode


In the file `part1_lln.py`, implement the LinkedListNode class.  I would do the methods in the following order:

1. initialiser
    * this takes one argument, some "contents"
2. check that the `__repr__` is doing something somewhat sane
    * this is for your own benefit, so that if you `print(node)` for some lln, you'll get something useful
    * you might want to come back to this as you work on other methods
3. insertAfter, to create additional nodes linked to the first
    * if I have a LinkedList that has two nodes, first holding `1`, second holding `3`, and right now `n1` is a reference to the node that holds the `1`, and I do `n1.insertAfter(2)`, I should end up with a list with 3 nodes, `1` and then `2` and then `3`
    * what is the argument to insertAfter?
        * I recommend just supplying the contents for the new node
        * there are other ways to do it, but if you do it another way, you'll have to change the tests
    * the tricky part of this one is making sure that you can add new nodes in the middle of the overall list, withing messing up anything else
4. toList, to allow you to debug the whole linkedlist
    * this returns a regular Python list
    * if you do `node.toList()` on the first node, that returns all the nodes
    * if you do `node.toList()` on a node partway through, it ignores the nodes before itself, but continues to the end
5. findLast, this is a good warmup for the next one
    * this returns a reference to the last node in the current linked list
    * if `node` is the last in its list, then `node.findLast() == node`, which might feel weird
6. findAfter, this is sort of a linear search
    * that means it needs to take a `needle` as an argument
    * if no match is found, raise a KeyError, like dictionary
    * if a match IS found, return the LLN that contains the match
    * it's findAfter, not findHereOrAfter, so it never finds itself

In `part1_lln.py`, I included a long `main()` function that demonstrates what your class would do if it was finished.



## Part 2 : DoublyLinkedListNode

Okay, let's step it up.  Part 1 should have mostly been covered in lecture, but Part 2 you're going to need to go beyond.

A *doubly-linked list* is like a linked-list, but with extra links.  Not only is there a link to the *next* node, there's also a link to the *previous* node.  (Just as the next-node-link should contain `None` for the last node, so too the previous-node-link should contain `None` for the first node.)  So copy-and-paste your class from `part1_lln.py` into `part2_dlln.py`, and add some new methods, and modify the existing methods where appropriate.

1. First figure out how to modify the initialiser
2. Then figure out how to modify `insertAfter` so that they work fully, and then your other methods.
3. Then start adding other methods:
    1. `insertBefore` is the mirror of `insertAfter`
    2. `findFirst` is the mirror of `findLast`
    3. `findBefore` is the mirror of `findAfter`
    4. `toList` doesn't need a mirror






## Part 3 : reversing

This one goes back to the non-double LinkedList from Part 1.


For this you're going to write a stand-alone function, not another method.  This function takes in a single linked-list node, the first one of a linked-list (if it's given a non-first node, then probably a mess is created).  It then *modifies* all the nodes in the linked-list so that the links all point in the opposite direction.  Note that it **does not** create any *new* nodes, and it does not mess with the contents of the nodes, it only rearranges the links.

