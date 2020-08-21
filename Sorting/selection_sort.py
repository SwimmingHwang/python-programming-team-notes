"""
선택 정렬 : 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정 반복
시간복잡도 : O(N^2)
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    # i 이후 데이터들 중 가장 작은 값 찾기
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # 가장 작은 값이랑 i자리 값이랑 바꾸기 -> 제일 작은 값이 i자리에 차지
    array[i], array[min_index] = array[min_index], array[i]  # swap
