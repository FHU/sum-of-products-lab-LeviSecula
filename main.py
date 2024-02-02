#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    if len(list1) == len(list2):
        total = 0
        for i in range(len(list1)):
            total = total + (list1[i] * list2[i])
            i += 1
        return(total)
    
    else:
        return("error")


if __name__ == '__main__':
    User1 = input().split()
    User2 = input().split()
    list1 = [int(x) for x in User1]
    list2 = [int(x) for x in User2]

    result = sum_of_products(list1, list2)
    print(result)