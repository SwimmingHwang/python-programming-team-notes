"""
삽입정렬 : 특정한 데이터를 적절한 위치에 삽입
시간복잡도 : O(N^2), 정렬이 거의 되어 있는 상황에서는 O(N)이며 퀵 정렬 알고리즘보다 더 강력함.
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱수 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
