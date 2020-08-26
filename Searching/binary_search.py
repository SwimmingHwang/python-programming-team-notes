"""
이진 탐색 : 반으로 쪼개면서 탐색하기
시간복잡도 : O(logN)
- 데이터가 정렬되어 있어야만 사용할 수 있다.
- 탐색 범위를 절반씩 좁혀가며 데이터를 탐색한다.
- 절반씩 데이터를 줄어들도록 만든다는 점에서 퀵 정렬과 공통점이 있다.
- 구현방법
    1) 재귀 함수를 이용
    2) 반복문 이용
"""


def binary_search_recursive(array, target, start, end):
    """
    재귀함수를 이용한 이진탐색 구현

    :param array: 정렬되어 있는 리스트
    :param target: 찾고자 하는 값
    :param start: array의 시작점 인덱스
    :param end: array의 끝점 인덱스
    :return: 찾고자 하는 값의 인덱스
    """
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:  # 찾고자 하는 값이 중간값인 경우
        return mid
    elif array[mid] > target:  # 찾고자 하는 값이 왼쪽파트인 경우
        return binary_search_recursive(array, target, start, mid - 1)
    else:  # 찾고핮 하는 값이 오른쪽 파트인 경우
        return binary_search_recursive(array, target, mid + 1, end)


def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

if __name__ == '__main__':
    # n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
    n, target = list(map(int, input().split()))
    # 전체 원소 입력 받기
    array = list(map(int, input().split()))

    # 이진 탐색 수행 결과 출력
    result1 = binary_search_recursive(array, target, 0, n - 1)
    result2 = binary_search_loop(array, target, 0, n - 1)

    if result1 == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result1 + 1)
