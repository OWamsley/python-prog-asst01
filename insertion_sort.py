# Python program for implementation of Insertion Sort
# Acknowledgement: InteractivePython


def insertion_sort(alist):
    # goes through values of 1 to the length of the list
    for index in range(1, len(alist)):
#index is the number that goes through the range
        current_value = alist[index]
        position = index

#when the current value is less than the value of the lower cell the under code is used
        while position > 0 and alist[position - 1] < current_value:
            #the cell takes the value of the cell one lower
            alist[position] = alist[position - 1]
            position = position - 1

        #the lower cell gets the higher cell's value
        alist[position] = current_value
        print(alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]


insertion_sort(alist)
print(alist)
