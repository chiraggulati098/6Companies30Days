class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        s = set(list(s))
        s = sorted(s, key = lambda x: freq[x], reverse = True)

        res = ''
        for c in s:
            res += c * freq[c]
        
        return res