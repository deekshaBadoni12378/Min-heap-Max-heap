def min_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def insert(A,  k):
    size = len(A)
    if size == 0:
        A.append(k)
    else:
        A.append(k)
        for i in range(size - 1, -1, -1):
           min_heapify(A, i)
def min_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def insert(A,  k):
    size = len(A)
    if size == 0:
        A.append(k)
    else:
        A.append(k)
        for i in range(size - 1, -1, -1):
           min_heapify(A, i)
def display(A):
    print("Min-heap array: " + str(A))
    print()


arr = []

insert(arr, 23)
insert(arr, 18)
insert(arr, 19
insert(arr, 24)
insert(arr, 45)
display(arr)

arr = []

insert(arr, 23)
insert(arr, 18)
insert(arr, 19
insert(arr, 24)
insert(arr, 45)
display(arr)