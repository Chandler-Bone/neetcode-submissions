class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj_map = defaultdict(set)

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                sword = word[:i] + "*" + word[i+1:]
                adj_map[sword].add(word)

        queue = deque()
        for i in range(len(endWord)):
            queue.append((endWord[:i] + "*" + endWord[i+1:], 1))
        
        visited = set()
        while queue:
            # print(queue)
            sword, count = queue.popleft()

            visited.add(sword)
            for word in adj_map[sword]:
                if word == beginWord:
                    return count + 1
                for i in range(len(word)):
                    sword = word[:i] + "*" + word[i+1:]
                    if sword not in visited:
                        queue.append((sword, count + 1))

        return 0

