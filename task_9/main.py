# program_1
def multi_table(n=10):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i} x {j} = {i*j}")
        if i < n:
            print("+++++") # separator
    print("____________________________________________________________________________")
#.......................................
# program_2
def vali(id="ABx1234", start="AB", total_len=7, numbers_len=4):
    if (
        id[:2] == start and
        len(id) == total_len and
        id[-numbers_len:].isdigit() and len(id[-numbers_len:]) == numbers_len
    ):
        return "valid ID"
    else:
        return "Invalid ID"

#main
#program_1
while True:
    n = input("Enter size of table default is '10': ") or "10"
    try:
        if int(n) > 0:
            break
        else:
            print("enter positive number ")
    except ValueError:
        print("enter valid number ")
            
multi_table(int(n))
#.......................................
#program_2
id = input("enter ID default is 'ABx1234': ") or "ABx1234"
print(vali(id))








