SECTION A

1.	Bubble Sort
The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs. If there are n items in the list, then there are n−1 pairs of items that need to be compared on the ﬁrst pass. It is important to note that once the largest value in the list is part of a pair, it will continually be moved along until the pass is complete. At the start of the second pass, the largest value is now in place. There are n−1 items left to sort, meaning that there will be n−2 pairs. Since each pass places the next largest value in place, the total number of passes necessary will be n−1. After completing the n−1 passes, the smallest item must be in the correct position with no further processing required. The code below shows the complete bubble_sort function. It takes the list as a parameter, and modiﬁes it by exchanging items as necessary.
def bubble_sort(a_list): 
for pass_num in range(len(a_list) - 1, 0, -1):
 for i in range(pass_num): if a_list[i] > a_list[i + 1]: 
temp = a_list[i]
 a_list[i] = a_list[i + 1]
 a_list[i + 1] = temp
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20] 
bubble_sort(a_list) 
print(a_list)
The exchange operation, sometimes called a “swap,” is slightly different in Python than in most other programming languages. Typically, swapping two elements in a list requires a temporary storage location (an additional memory location). A code fragment such as
temp = a_list[i] 
a_list[i] = a_list[j]
a_list[j] = temp
will exchange the ith and jth items in the list. Without the temporary storage, one of the values would be overwritten. In Python, it is possible to perform simultaneous assignment. The statement a, b = b, a will result in two assignment statements being done at the same time (see Figure 5.14). Using simultaneous assignment, the exchange operation can be done in one statement. Lines5–7in the bubble_sort function perform the exchange of the I and (i+1)th items using the three-step procedure described earlier. Note that we could also have used the simultaneous assignment to swap the items. To analyze the bubble sort, we should note that regardless of how the items are arranged in the initial list, n−1 passes will be made to sort a list of size n. The total number of comparisons is the sum of the ﬁrst n−1 integers. Recall that the sum of the ﬁrst n integers is 1 2n2 + 1 2n. The sum of the ﬁrst n − 1integers is 1 2n2 + 1 2n−n, which is 1 2n2− 1 2n. This is still O(n2) comparisons. In the best case, if the list is already ordered, no exchanges will be made. However, in the worst case, every comparison will cause an exchange. On average, we exchange half of the time. A bubble sort is often considered the most inefﬁcient sorting method since it must exchange items before the ﬁnal location is known. These “wasted” exchange operations are very costly. However, because the bubble sort makes passes through the entire unsorted portion of the list,
Pass Comparisons 1 n−1 2 n−2 3 n−3 ... ... n−1 1 Table 5.6: Comparisons for Each Pass of Bubble Sort
it has the capability to do something most sorting algorithms cannot. In particular, if during a pass there are no exchanges, then we know that the list must be sorted. A bubble sort can be modiﬁed to stop early if it ﬁnds that the list has become sorted. This means that for lists that require just a few passes, a bubble sort may have an advantage in that it will recognize the sorted list and stop. The code below shows this modiﬁcation, which is often referred to as the short bubble.
def short_bubble_sort(a_list):
 exchanges = True
 pass_num = len(a_list) – 1
 while pass_num > 0 and exchanges: 
exchanges = False
 for i in range(pass_num):
 if a_list[i] > a_list[i + 1]:
 exchanges = True
 temp = a_list[i]
 a_list[i] = a_list[i + 1] 
a_list[i + 1] = temp
pass_num = pass_num - 1
a_list=[20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
 short_bubble_sort(a_list)
 print(a_list)

Insertion Sort
The insertion sort, although still O(n2), works in a slightly different way. It always maintains a sorted sub list in the lower positions of the list. Each new item is then “inserted” back into the previous sub list such that the sorted sub list is one item larger. Figure5.16showstheinsertionsortingprocess. The shaded items represent the ordered sub lists as the algorithm makes each pass. We begin by assuming that a list with one item (position 0) is already sorted. On each pass, one for each item 1 through n−1, the current item is checked against those in the already sorted sub list. As we look back into the already sorted sub list, we shift those items that are greater to the right. When we reach a smaller item or the end of the sub list, the current item can be inserted. The implementation of insertion_sort shows that there are again n−1 passes to sort n items. The iteration starts at position 1 and moves through position n−1, as these are the items that need to be inserted back into the sorted sub lists. Line 8 performs the shift operation that moves a value up one position in the list, making room behind it for the insertion. Remember that this is not a complete exchange as was performed in the previous algorithms. Themaximumnumberofcomparisonsforaninsertionsortisthesumoftheﬁrstn−1integers. Again, this is O(n2). However, in the best case, only one comparison needs to be done on each pass. This would be the case for an already sorted list. One note about shifting versus exchanging is also important. In general, a shift operation requires approximately a third of the processing work of an exchange since only one assignment is performed. In benchmark studies, insertion sort will show very good performance.
def insertion_sort(a_list): 
for index in range(1, len(a_list)):
current_value = a_list[index] position = index
while position > 0 and a_list[position - 1] > current_value:
 a_list[position] = a_list[position - 1] 
position = position - 1
a_list[position] = current_value
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
 insertion_sort(a_list) 
print(a_list)


2. CODE FOR BUBBLE SORT:

def bubble_sort(myList):
    for a in range(0, len(myList)-1):
        for i in range(0, len(myList)-1-a):
            if myList[i] > myList[i+1]:
                temp = myList[i]
                myList[i] = myList[i+1]
                myList[i+1] = temp
myList = [4,23,33,24,20]
bubble_sort(myList)
print(myList)


CODE FOR INSERTION SORT:

def selection_sort(input_list):
   
        for i in range(len(input_list)):
            m = i
            
            for j in range(i+1, len(input_list)):
               if input_list[m] > input_list[j]:
                m = j
            input_list[i], input_list[m] = input_list[m], input_list[i]

input_list = [19, 2, 31, 45, 30, 11, 121, 27]
selection_sort(input_list)
print(input_list)


SECTION B:
1. def solution(N):
    max_gap = 0
    current_gap = 0
    # Skip the tailing zero(s)
    while N > 0 and N%2 == 0:
        N //= 2
    while N > 0:
        remainder = N%2
        if remainder == 0:
            # Inside a gap
            current_gap += 1
        else:
            # Gap ends
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                current_gap = 0
        N //= 2
    return max_gap


2. def solution(A, K):     
   if K == 0 or len(A)/K ==0:
      return A
   if K > len(A):
      K = K/len(A)
   A = A[len(A)-K:len(A)] + (A[0:len(A)-K])
   return A


3. def solution(A):     
    if len(A) == 1:
         return A[0]
    A = sorted(A)
    for i in range(0 , len (A) , 2):
         if i+1 == len(A):
             return A[i]
         if A[i] != A[i+1]:
             return A[i]

            
