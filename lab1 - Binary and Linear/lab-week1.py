
# Part 1
def linear_search(needle, haystack):
    for count, item in enumerate(haystack):
        if item == needle:
            return count

    return None

# print(linear_search(9, [6, 2, 8, 4]))

# Part 2
# inspiration https://www.youtube.com/watch?v=s4DPM8ct1pI
def binary_search(needle, haystack):
    start_idx = 0
    end_idx = len(haystack) - 1

    while start_idx <= end_idx:

        mid_idx = int((start_idx + end_idx) // 2)
        print(f"mid-idx: {mid_idx}, value: {haystack[mid_idx]}")

        if haystack[mid_idx] > needle :
            end_idx = mid_idx - 1
        elif haystack[mid_idx] < needle :
            start_idx = mid_idx + 1
        else:
            return mid_idx
    
    return None

# print(binary_search(4, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]))


# Part 3
def linear_search_multi(needle, haystack): 
    list = []

    for count, item in enumerate(haystack):
        if item == needle:
            list.append(count)

    return list


# print(linear_search_multi(8, [6, 2, 8, 4, 8, 7]))

def binary_search_multi(needle, haystack):
    start_idx = 0
    end_idx = len(haystack) - 1
    list = []

    while start_idx <= end_idx:
        
        mid_idx = int((start_idx + end_idx) // 2)
        
        left_idx = mid_idx - 1
        right_idx = mid_idx + 1

        if haystack[mid_idx] == needle:
            
            list.append(mid_idx)

            while left_idx >= start_idx and haystack[left_idx] == needle:
                list.append(left_idx)
                left_idx -= 1
    

            while right_idx <= end_idx and haystack[right_idx] == needle:
                    list.append(right_idx)
                    right_idx += 1

            break

        elif haystack[mid_idx] > needle:
            end_idx = mid_idx - 1

        elif haystack[mid_idx] < needle:
            start_idx = mid_idx + 1


    return sorted(list)

print(binary_search_multi(3, [1, 2, 2, 3, 3, 3, 3, 4, 5]))
print(binary_search_multi(2, [1, 2, 2, 3, 3, 3, 3, 4, 5]))
print(binary_search_multi(6, [1, 2, 2, 3, 3, 3, 3, 4, 5]))