class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        time = defaultdict(list)

        for i in range(len(access_times)):
            access_times[i][1] = int(access_times[i][1])

        access_times.sort(key = lambda x: x[1])
        res = []

        for emp, t in access_times:
            time[emp].append(t)
        
        for emp in time:
            l = 0
            for r in range(len(time[emp])):
                while time[emp][r] - time[emp][l] > 99:
                    l += 1
                if (r - l + 1) == 3:
                    res.append(emp)
                    break
        
        return res