"""
파이썬에서는 힙 기능을 위해 heapq 라이브러리를 제공
heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용됨.
코딩테스트 환경에서는 PriorityQueue 보다 heapq가 더 빠름.
파이썬의 heap은 Min Heap 이므로 오름차순 정렬 시간복잡도는 O(NlogN)
삽입 : heapq.heappush(iterable)
삭제 : heapq.heappop(iterable)
-----------
heapsort2() 는 Max Heap을 구현하여 오름차순 힙 정렬을 구현한 예시
"""
import heapq


def heapsort(iterable):
    """
    Min Heap sort
    :param iterable: iterable data type
    :return: Sorted list
    """
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽임
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

def heapsort2(iterable):
    """
    Max Heap sort
    :param iterable: iterable data type
    :return: Sorted list
    """
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입 - Max Heap을 구현하기 위해 부호를 반대로 바꿈
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
result2 = heapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result2)
'''
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
'''
