def QuickSort(A, l, r):
    num_comparisons = 0
    if (l >= r):
        #print "end of tree"
        return A, num_comparisons
    else:
        #print "QuickSorting: ", A, " from ", l, " to ", r
        k = l + (r-l)//2    #middle element
        B = [A[l], A[k], A[r]]
        for a in range(0, 3):
            for b in range(0, 3):
                if B[a] > B[b]:
                    higher = B[a]
                    lower = B[b]
                    B[a] = lower
                    B[b] = higher
        if B[1] == A[l]:
            p_indice = l
        if B[1] == A[k]:
            p_indice = k
        if B[1] == A[r]:
            p_indice = r
        p = A[p_indice]
        righttoleft = p
        lefttoright = A[l]
        A[l] = righttoleft
        A[p_indice] = lefttoright
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