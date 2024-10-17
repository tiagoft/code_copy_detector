def bubble_sort(X):
    N = len(X)
    for idx in range(N):
        for idx2 in range(0, N-idx-1):
            if X[idx2] > X[idx2+1]:
                X[idx2], X[idx2+1] = X[idx2+1], X[idx2]
    return X
