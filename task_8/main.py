#first program 

#func get (n) positive numbers
def get_nums(n):
    nums = []
    while len(nums) < n:
        try:
            num = float(input(f"number {len(nums) + 1} => "))
            if num >= 0:
                nums.append(num)
            else:
                print("number is negative,enter a positive number")
        except ValueError:
            print("Invalid input")
    return nums

#func calc average of get nums
def calc_avg(nums):
    return sum(nums) / len(nums)
    

#main
while True:
    try:
        n = int(input("enter the number (n) of positive numbers: "))
        if n > 0:
                break
        else:
            print("Number must be greater than zero.")
    except ValueError:
        print("Invalid input")
        
print(f"enter {n} positive numbers")
nums = get_nums(n)
avg = calc_avg(nums)
print(f"average = {avg}")

#.........................................
#second program

#func categorize nums into: +odd, +even, -odd, and -even.
def categorize_nums():
    positive_odd = []
    positive_even = []
    negative_odd = []
    negative_even = []

    print("enter numbers (use 0 to stop):")

    while True:
        try:
            num = int(input("enter a number: "))

            if num == 0:
                break
            elif num > 0:
                if num % 2 == 0:
                    positive_even.append(num)
                else:
                    positive_odd.append(num)
            else:
                if num % 2 == 0:
                    negative_even.append(num)
                else:
                    negative_odd.append(num)
        except ValueError:
            print("Invalid input")

    print("...........................")
    print("\nsummary:")
    print(f"positive odd numbers: {len(positive_odd)} -> {positive_odd}")
    print(f"positive even numbers: {len(positive_even)} -> {positive_even}")
    print(f"negative odd numbers: {len(negative_odd)} -> {negative_odd}")
    print(f"negative even numbers: {len(negative_even)} -> {negative_even}")

#main
categorize_nums()







