from part1_lln import LLN


def reverse(lln):
    prev = None
    current = lln
    
    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the current node's pointer
        prev = current  # Move prev and current one step forward
        current = next_node
    
    # Now prev is the new head of the reversed list
    return prev


def main():
    first = LLN("one")
    second = first.addAfter("two")
    third = first.findLast().addAfter("three")
    fourth = first.findLast().addAfter("four")

    print("before we reverse the list, starting at first:", first.toList())
    newBegin = reverse(first)
    print("now that we have reversed, the list from first is very short: ", first.toList())
    print("but the list from the new beginning is longer:", newBegin.toList())
    print("and since newBegin is fourth, here it is again:", fourth.toList())

    ### Here's the output:
    """
    before we reverse the list, starting at first: ['one', 'two', 'three', 'four']
    now that we have reversed, the list from first is very short:  ['one']
    but the list from the new beginning is longer: ['four', 'three', 'two', 'one']
    and since newBegin is fourth, here it is again: ['four', 'three', 'two', 'one']
    """


if __name__ == "__main__":
    main()
