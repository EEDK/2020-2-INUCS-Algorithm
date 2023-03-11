def solution(board, moves):
    answer = 0

    lst = [0]

    for target in moves:
        for j in range(len(board)):
            if board[j][target-1] != 0:
                lst.append(board[j][target-1])
                board[j][target-1] = 0

                tmp1 = lst.pop()
                tmp2 = lst.pop()
                if tmp1 == tmp2:
                    answer += 2
                else:
                    lst.append(tmp2)
                    lst.append(tmp1)

                break
            elif board[j][target-1] == 0:
                continue

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
