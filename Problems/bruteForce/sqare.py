def solution(sizes):
    Width = []
    Height = []

    for size in sizes:
        if size[0] > size[1]:
            Width.append(size[0])
            Height.append(size[1])

        else:
            Width.append(size[1])
            Height.append(size[0])

    return max(Width) * max(Height)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
