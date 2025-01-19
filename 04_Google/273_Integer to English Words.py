class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        digits = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 
        10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen',
        18:'Eighteen', 19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy',
        80:'Eighty', 90:'Ninety'}
        
        res = ''
        suffix = ['', ' Thousand ', ' Million ', ' Billion ', ' Trillion ']

        def helper(x, i):
            s = ''

            if x == 0:
                return ''
                
            if x > 99:
                h = x//100
                s += digits[h] + ' Hundred '
                
            h = x % 100
            if h == 0:
                return s.strip() + suffix[i]
                    
            if h in digits.keys():
                s += digits[h]
                return s.strip() + suffix[i]

            h = (x // 10) % 10
            if h != 0:
                s += digits[h * 10] + ' '
                    
            h = x % 10
            if h != 0:
                s += digits[h] + ' '
            return s.strip() + suffix[i]

        if num == 0:
            return 'Zero'
        
        temp = num
        i = 0
        
        while temp > 0:
            res = helper(temp % 1000, i) + res
            res = res.strip()
            temp = temp // 1000
            i += 1
        
        return res