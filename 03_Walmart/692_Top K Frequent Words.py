class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)

        for word in words:
            freq[word] += 1
        
        return sorted(set(words), key = lambda x: [-freq[x], x])[:k]