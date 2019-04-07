def insertionSort(alist):
    for index in range(1, len(alist)):
        position = index
        while position>0 and alist[position-1]>alist[position]:
            temp = alist[position-1]
            alist[position-1] = alist[position]
            alist[position] = temp
            position = position-1 

# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

input_int = input("Please enter some numbers and separated by space! \n")
alist = input_int.split()

print("Number before sort: \n " + str(alist))
insertionSort(alist)
print("Number after sorted: \n " + str(alist))