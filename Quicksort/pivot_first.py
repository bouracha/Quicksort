def QuickSort(A, l, r):
    num_comparisons = 0
    if (l >= r):
        #print "end of tree"
        return A, num_comparisons
    else:
        #print "QuickSorting: ", A, " from ", l, " to ", r
        p = A[l]
        #print "pivot is ", p, " at position ", l
        i = l + 1
        j = l + 1
        while j <= r:
            if A[j] > p:
                j += 1
            else:
                lefttoright = A[i]
                righttoleft = A[j]
                A[i] = righttoleft
                A[j] = lefttoright
                i += 1
                j += 1
        lefttoright = p
        righttoleft = A[i-1]
        A[l] = righttoleft
        A[i-1] = lefttoright

        #print i, j

        A, x = QuickSort(A, l, i-2)
        A, y = QuickSort(A, i, j-1)
        num_comparisons = x+y+(r-l)
        #print "Runnning sum of comparisons: ", num_comparisons

        return A, num_comparisons