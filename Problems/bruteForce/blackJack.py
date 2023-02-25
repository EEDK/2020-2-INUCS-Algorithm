import itertools


def blackJack(target, cards):

    answer = 0

    cardCombi = list(itertools.combinations(cards, 3))
    sumCard = list()
    for com in cardCombi:
        if sum(com) <= int(target):
            sumCard.append(sum(com))

    return max(sumCard)


n, target = input().split()
numlist = list(map(int, input().split()))


print(blackJack(target, numlist))
