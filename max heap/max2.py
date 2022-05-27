def max_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2
def insert(A, k):
    size = len(A)
    if size == 0:
        A.append(k)
    else:
        A.append(k)
        for i in range(size - 1, -1, -1):
            max_heapify(A, i)
def display(A):
    print("Max-heap array: " + str(A))
    print()


arr = []

insert(arr, 9)
insert(arr, 12)
insert(arr, 1)
insert(arr, 20)
insert(arr, 13)
display(arr)


