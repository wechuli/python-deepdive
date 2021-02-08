def fair_index_single(A: list) -> set:
    total_sum = sum(A)
    left_side_array_sum = A[0]
    right_side_array_sum = total_sum - A[0]
    fair_set = []
    for i in range(1, len(A)):

        if left_side_array_sum == right_side_array_sum:
            fair_set.append(i)
        left_side_array_sum += A[i]
        right_side_array_sum -= A[i]

    return set(fair_set)


a = fair_index_single([0, 4, -1, 0, 3])
b = fair_index_single([0, -2, 5, 0, 3])

intersec = a.intersection(b)
print(len(intersec))


# Get the fair index for individual list

def fair_index_single(A: list) -> set:
    total_sum = sum(A)
    left_side_array_sum = A[0]
    right_side_array_sum = total_sum - A[0]
    fair_set = {}
    for i in range(1, len(A)):

        if left_side_array_sum == right_side_array_sum:
            fair_set.append(i)
        left_side_array_sum += A[i]
        right_side_array_sum -= A[i]
    # make it into a set to make it easier to get intersection
    return set(fair_set)


def solution(A, B):
    # write your code in Python 3.6
    A_set = fair_index_single(A)
    B_set = fair_index_single(A)
    return(len(A_set.intersection(B_set)))


print(fair_index_single([4, -1, 0, 3]))
print(fair_index_single([-2, 6, 0, 4]))
