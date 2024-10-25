from pathlib import Path
import time
import random
import statistics


r = random.random()

list_1 = [i for i in range(10)]
list_2 = [i for i in range(1000000)]

dict_1 = {i: i for i in range(10)}
dict_2 = {i: i for i in range(1000000)}

# 1-4 insert vs append
def task_1():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 1. add one number to the beginning of a list that already has 10 numbers in it?
        list_1.insert(0, r)
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

def task_2():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 2. add one number to the beginning of a list that already has 1,000,000 numbers in it?
        list_2.insert(0, r)
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

def task_3():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 3. add one number to the end of a list that already has 10 numbers in it?
        list_1.append(r)
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

def task_4():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 4. add one number to the end of a list that already has 1,000,000 numbers in it?
        list_2.append(r)
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)


# 5-8 remove vs pop
def task_5():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 5.remove one number from the beginning of a list that already has 10 numbers in it?
        list_1.remove(list_1[0])
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

def task_6():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 6.remove one number from the beginning of a list that already has 1,000,000 numbers in it?
        list_2.remove(list_2[0])
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

def task_7():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 7.remove one number from the end of a list that already has 10 numbers in it?
        list_1.pop()
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

def task_8():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # remove one number from the end of a list that already has 1,000,000 numbers in it?
        list_2.pop()
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

# 9-12 check value in list
def task_9():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
         # 9. check for the presence of a number in a list of 10 numbers, using if x in l syntax, if the number is in the list
        check_number = []
        if r in list_1:
            check_number.append(r)
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

def task_10():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 10. check for the presence of a number in a list of 1,000,000 numbers, using if x in l syntax, if the number is in the list
        check_number = []
        if r in list_2:
            check_number.append(r)
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

def task_11():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 11. check for the presence of a number in a list of 10 numbers, using if x in l syntax, if the number is not in the list
        check_number = []
        if r not in list_1:
            check_number.append(r)
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

def task_12():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 12. check for the presence of a number in a list of 1,000,000 numbers, using if x in l syntax, if the number is not in the list
        check_number = []
        if r not in list_2:
            check_number.append(r)
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

# 13-16 check key in dict
def task_13():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 13. check for the presence of a key in a dict of 10 key-value-pairs, using if x in d syntax, if the key is in the dict
        check_number = []
        if r in dict_1:
            check_number.append(r)
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

def task_14():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 14. check for the presence of a key in a dict of 1,000,000 key-value-pairs, using if x in d syntax, if the key is in the dict
        check_number = []
        if r in dict_2:
            check_number.append(r)
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

def task_15():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 15. check for the presence of a key in a dict of 10 key-value-pairs, using if x in d syntax, if the key is not in the dict
        check_number = []
        if r not in dict_1:
            check_number.append(r)
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)

def task_16():
   
    deltas = []
    
    for i in range(1000):
        before = time.perf_counter()
        # 16. check for the presence of a key in a dict of 1,000,000 key-value-pairs, using if x in d syntax, if the key is not in the dict
        check_number = []
        if r not in dict_2:
            check_number.append(r)
        after = time.perf_counter()
        delta = after - before
    
        deltas.append((delta) * 1000000)

    return statistics.mean(deltas)


def main():

    # create a folder
    new_directory = Path("./lab_week2_results")
    new_directory.mkdir(exist_ok=True)
    
    # test
    results = []
    
    results.append(task_1())
    results.append(task_2())
    results.append(task_3())
    results.append(task_4())
    results.append(task_5())
    results.append(task_6())
    results.append(task_7())
    results.append(task_8())
    results.append(task_9())
    results.append(task_10())
    results.append(task_11())
    results.append(task_12())
    results.append(task_13())
    results.append(task_14())
    results.append(task_15())
    results.append(task_16())

    results_file = new_directory.joinpath("lab2_results.txt")

    # add average value into file
    with open(results_file, "w") as file:
       for index, result in enumerate(results, start=1):
           file.write(f"task {index}: {result}\n")


if __name__ == "__main__":
    main()
        




