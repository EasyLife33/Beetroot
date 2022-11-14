#Task 1
def double_bubble_sort(seq):
    swapped = True
    start = 0
    end = len(seq) - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        for i in range(end-1, start-1, -1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        start += 1


seq = [3, 5, 9, 6, 8, 2, 11, 0]
double_bubble_sort(seq)
print(seq)


#Task 2
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2  
        left_half = [array[i] for i in range(0, len(array)) if i % 2 == 0]  
        right_half = [array[i] for i in range(0, len(array)) if i % 2 == 1]  
        print(left_half, right_half)
        merge_sort(left_half) 
        merge_sort(right_half)  

        i = 0  
        j = 0  
        k = 0  
        while i < len(left_half) and j < len(right_half):  
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1
        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1


l = [5, 8, 6, 4, 7, 0, 3, 1]
merge_sort(l)
print(l)
