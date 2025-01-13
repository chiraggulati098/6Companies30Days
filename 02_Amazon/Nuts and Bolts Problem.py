class Solution:

	def matchPairs(self, n, nuts, bolts):
		# code here
		value = {'!': 1, '#': 2, '$': 3, '%': 4, '&': 5, '*': 6, '?': 7, '@': 8, '^': 9}
		
		nuts.sort(key = lambda x: value[x])
		bolts.sort(key = lambda x: value[x])