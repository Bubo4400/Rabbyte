import math

def AdotB(A, B):
    length = len(A)
    total = 0 
    for i in range(length):
        total += A[i]*B[i]

    return total

def magnitude(A):
    total = 0
    for a in A:
        total += a**2

    return math.sqrt(total)

def cosineSimilarity(A, B):
    return AdotB(A, B)/(magnitude(A) * magnitude(B))


def similarity(word1, word2, model):
    vector1 = model.encode(word1)
    vector2 = model.encode(word2)

    return cosineSimilarity(vector1, vector2)
