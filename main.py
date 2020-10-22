import SearchAlgorithm.digitalSearchTree
import SearchAlgorithm.radixSearchTrie
import SearchAlgorithm.patriciaTree
import random, time
from matplotlib import pyplot as plt

if __name__ == '__main__':
    N = int(input("만들 배열의 갯수 설정 : "))

    key = list(range(1, N + 1))
    s_key = list(range(1, N + 1))
    key.sort(reverse=False)
    d = SearchAlgorithm.digitalSearchTree.Dict()
    for i in range(N):
        d.insert(key[i])

    start_time = time.time()
    for i in range(N):
        result = d.search(s_key[i])
        if result == -1 or result != s_key[i]:
            print('탐색 오류')
    endtimeBinaryTree = time.time() - start_time

    print('디지털 탐색 수행 시간(N = %d) : %0.3f' % (N, endtimeBinaryTree))

    key = list(range(1, N + 1))
    s_key = list(range(1, N + 1))
    key.sort(reverse=False)

    d = SearchAlgorithm.radixSearchTrie.Dict()
    for i in range(N):
        d.insert(key[i])

    start_time = time.time()
    for i in range(N):
        result = d.search(s_key[i])
        if result.get() == -1 or result.get() != s_key[i]:
            print('탐색 오류')

    endtimeRedBlackTree = time.time() - start_time

    print('기수 트라이 탐색 수행 시간(N = %d) : %0.3f'%(N, endtimeRedBlackTree))

    key = list(range(1, N + 1))
    s_key = list(range(1, N + 1))
    random.shuffle(key)
    key.sort(reverse=False)
    d = SearchAlgorithm.patriciaTree.Dict()
    for i in range(N):
        d.insert(key[i])

    start_time = time.time()
    for i in range(N):
        result = d.search(s_key[i])
        if result.get() == -1 or result.get() != s_key[i]:
            print('탐색 오류')

    endtimeAVLTree = time.time() - start_time
    print('패트리샤 트리 탐색 수행 시간(N = %d) : %0.3f'%(N, endtimeAVLTree))

    timeAboutTree = [endtimeBinaryTree, endtimeRedBlackTree, endtimeAVLTree]

    ax = plt.subplot()
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(['digitalSearch', 'radixSearchTrieTree', 'patriciaTree'], rotation=30)

    plt.bar(range(len(timeAboutTree)), timeAboutTree)

    plt.show()


