import SearchAlgorithm.Search

class node:
    def __init__(self, key=None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self, searchKey):
        SearchAlgorithm.Search.sequentialSearch(self, searchKey, 10)

    def insert(self, v):
        Dict.a
