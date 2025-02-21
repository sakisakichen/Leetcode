class Solution:
	def shortestDistance(self, s, word1, word2):
		ans = float('inf')
		idx1, idx2 = -1,-1
		
		for i, word in enumerate(s):
		    if word == word1:
		        idx1 = i
		        
		        if idx2 != -1: #來確保在計算最小距離之前，word2 已經出現過 
		            ans = min(ans,abs(idx1 -idx2))
		    elif word == word2:
		        idx2 = i
		        
		        if idx1 != -1: #來確保在計算最小距離之前，word2 已經出現過 
		            ans = min(ans,abs(idx2 -idx1))

        return ans if ans != float('inf') else -1 