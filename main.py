#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    Sum1 = list1[0] * list2[0]
    Sum2 = list1[1] * list2[1]
    Sum3 = list1[2] * list2[2]
    FinalSum = Sum1 + Sum2 + Sum3
    return FinalSum


if __name__ == '__main__':
    User1 = input()
    User2 = input()
    UserA = User1.replace(" ","")
    UserB = User2.replace(" ","")
    list1 = [int(x) for x in str(UserA)]
    list2 = [int(x) for x in str(UserB)]

    result = sum_of_products(list1, list2)
    print(result)