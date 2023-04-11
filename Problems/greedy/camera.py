def solution(routes):
    routes.sort(key=lambda x: x[1])

    answer = 0
    camera_pos = -30001

    for route in routes:
        if camera_pos < route[0]:
            answer += 1
            camera_pos = route[1]

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
