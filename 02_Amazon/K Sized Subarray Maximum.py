class Solution:
    #Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self, arr, k):
        # code here
        res = []
        q = deque()
        
        for r in range(k):
            while q and arr[q[-1]] <= arr[r]:
                q.pop()
            q.append(r)
            
        for i in range(k, len(arr)):
            res.append(arr[q[0]])
            
            while q and q[0] <= i - k:
                q.popleft()
            
            while q and arr[q[-1]] <= arr[i]:
                q.pop()
            q.append(i)
        
        res.append(arr[q[0]])
        
        return res