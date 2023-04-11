"""
정수로 이루어진 배열 numbers가 있습니다. 
배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
정수 배열 numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 
단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.
"""


def solution(numbers):
    answer = [-1] * len(numbers)  # answer 배열을 -1로 초기화
    stack = []  # 스택 초기화

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:  # 스택의 top과 현재 숫자를 비교
            top = stack.pop()
            answer[top] = numbers[i]  # top의 뒷 큰수를 현재 숫자로 갱신

        stack.append(i)  # 현재 숫자의 인덱스를 스택에 추가

    return answer


print(solution([2, 3, 3, 5]))
