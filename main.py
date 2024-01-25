#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    Sum1 = list1[0] * list2[0]
    Sum2 = list1[1] * list2[1]
    Sum3 = list1[2] * list2[2]
    FinalSum = Sum1 + Sum2 + Sum3
    return FinalSum

User1 = input()
User2 = input()

list1 = [int(x) for x in str(User1)]
list2 = [int(x) for x in str(User2)]

result = sum_of_products(list1, list2)
print(result)
if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    pass
