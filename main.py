#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    if len(list1) == len(list2):
        total = 0
        for i in range(len(list1)):
            total = total + (list1[i] * list2[i])
            i += 1
        print(total)
    
    else:
        print("error")


if __name__ == '__main__':
    User1 = input()
    User2 = input()
    UserA = User1.replace(" ","")
    UserB = User2.replace(" ","")
    list1 = [int(x) for x in str(UserA)]
    list2 = [int(x) for x in str(UserB)]

    result = sum_of_products(list1, list2)