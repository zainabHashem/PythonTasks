#first func
def fizz_buzz(n=15):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

#.......................................
#second func
def is_prime(x):
    if x < 2:
        return f"{x} ->not prime"
    for i in range(2, int(x/2)+1): #dividing by 2 reduces checking to half of nums
        if x % i == 0:
            return f"{x} -> not prime"
    return f"{x} -> prime"

#.......................................
#third func
def primes_n(p=100):
    for i in range(2, p):
        result = is_prime(i)
        if result == f"{i} -> prime":
            print(i)

#.......................................
#fourth func
def union(l1, l2):
    result = []
    for item in l1 + l2:
        if item not in result:
            result.append(item)
    return result

#.......................................
#fifth func
def flatten(l_s):
    flattened = []
    for sublist in l_s:
        for item in sublist:
            flattened.append(item)
    return flattened

#.......................................
#sixth func
def prefix(l1, l2):
    if len(l1) > len(l2):
        return False
    return l1 == l2[:len(l1)]


#.......................................

#main
#first func usage
while True:
    n = input("FizzBuzz for n default is '15': ") or "15"
    try:
        if int(n) > 0:
            break
        else:
            print("enter positive number ")
    except ValueError:
        print("enter valid number ")
#call func
fizz_buzz(int(n))
#.......................................
#second func usage
while True:
    x = input("enter number to check if it's prime: ") 
    try:
        if int(x) > 0:
            break
        else:
            print("enter positive number ")
    except ValueError:
        print("enter valid number ")
#call func
print(is_prime(int(x)))

#.......................................
#third func usage
while True:
    p = input("enter num_size to check if prime: ") or "100"
    try:
        if int(p) > 0:
            break
        else:
            print("enter positive number ")
    except ValueError:
        print("enter valid number ")
print(f"\nPrimes less than {p}:")
#call func
primes_n(int(p))

#.......................................
#fourth func usage
print("\nunion of two lists:")
l1 = input("enter the first list(use space to separate): ").split()
l2 = input("Enter the second list(use space to separate): ").split()
#convert str to int
l1 = [int(x) for x in l1]
l2 = [int(x) for x in l2]
#call func
result = union(l1,l2)
print("union:", result)

#.......................................
#fifth func usage
ll = input("enter list of lists(use space to sparate elemnts & use ',' to separate sublists ): ")

#Split sublists
sublists = ll.split(",")
# Convert sublist to a list of int
l_s = []
for sublist in sublists:
    nums = sublist.split()
    l_s.append([int(num) for num in nums])
#call func
print(f"flatten[{ll}] returns {flatten(l_s)}")

#.......................................
#sixth func usage
#enter first list 
print("\nchecks if list1 is a prefix of list2:")
l1 = input("enter the first list(use space to separate): ").split()
l2 = input("Enter the second list(use space to separate): ").split()
#convert str to int
l1 = [int(x) for x in l1]
l2 = [int(x) for x in l2]
#call func
print(f"prefix({l1},{l2}) returns {prefix(l1,l2)}")






