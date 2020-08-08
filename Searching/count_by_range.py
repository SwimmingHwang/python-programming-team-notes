"""
정렬된 리스트에서 값이 [left_value, right_value] 에 속하는 데이터의 개수를 반환하는 함수
이진 탐색을 이용해 O(logN)의 속도로 범위에 해당하는 원소의 개수를 빠르게 계산 할 수 있음.
"""
from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    '''
    Count the number of frequencies of elements whose value is between [left, right] in a sorted array.
    :param a: input list
    :param left_value: In a sorted array, range's start value
    :param right_value: In a sorted array, range's end value
    :return: count
    '''
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


# input list
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# Output number of data with value 4
print(count_by_range(a, 4, 4))
'''
2
'''
# Output number of data with value between -1 and 3
print(count_by_range(a, -1, 3))
'''
6
'''