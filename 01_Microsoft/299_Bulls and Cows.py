class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        n = len(secret)

        done = set()
        secretHash = defaultdict(int)

        for i in range(n):
            if secret[i] == guess[i]:
                a += 1
                done.add(i)
            else:
                secretHash[secret[i]] += 1
        
        for i in range(n):
            if i not in done:
                if secretHash[guess[i]] > 0:
                    b += 1
                    secretHash[guess[i]] -= 1

        return f'{a}A{b}B'