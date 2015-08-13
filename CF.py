__author__ = 'zhangruichang'


def distance(useri, userj, type):
    n = len(useri)
    dis = 0
    if type == 'euclidean':
        for i in range(n):
            dis = dis + (useri[i] - userj[i]) * (useri[i] - userj[i])
    return dis


# matrix is m*n, m users and n items
def get_topk(matrix, k, useri):
    m = len(matrix)
    if m <= 0:
        return [0]*k
    n = len(matrix[0])
    similarity = []
    for i in range(m):
        if i == useri:
            continue
        similarity.append([distance(matrix[useri], matrix[i], 'euclidean'), i])
    similarity.sort(reverse=True)
    topk = [x[1] for x in similarity[0:k]]
    return topk


def reccomend(topk, useri, matrix):
    for i in range(len(topk)):
        for j in range(n):
            if matrix[useri][j] == 0 and matrix[topk[i]][j] != 0:
                matrix[useri][j] = matrix[topk[i]][j]


if __name__ == "__main__":
    f = open('UserItem.txt', 'r')
    # for line in f:
    m, n, useri, k = [int(i) for i in f.readline().split()]
    #f.next()
    matrix = []
    for line in f:
        matrix.append([int(i) for i in line.split()])
    topk = get_topk(matrix, k, useri)
    reccomend(topk, useri, matrix)
    for i in matrix:
        print i
