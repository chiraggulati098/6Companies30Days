class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        for i in range(len(startWords)):
            startWords[i] = ''.join(sorted(startWords[i]))
        
        for i in range(len(targetWords)):
            targetWords[i] = ''.join(sorted(targetWords[i]))
        
        startWords = set(startWords)
        res = 0

        for word in targetWords:
            for i in range(len(word)):
                if (word[:i] + word[i + 1:]) in startWords:
                    res += 1
                    break
        
        return res