"""
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
"""

import heapq


def solution(scoville, K):

    heapq.heapify(scoville)
    answer = 0
    if scoville[0] >= K:
        return answer

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1

        min_scoville = heapq.heappop(scoville)
        min2_scoville = heapq.heappop(scoville)

        heapq.heappush(scoville, min_scoville + min2_scoville*2)
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
