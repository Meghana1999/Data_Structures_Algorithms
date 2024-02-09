#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
    
	def reverseInGroups(self, arr, N, K):
	    def revarr(start,end, arr):
	        while start<end:
	            arr[start],arr[end]= arr[end],arr[start]
	            start += 1
	            end -=1
	        return arr
	        
	    x = N//K
	    start = 0
	    end = K-1 
	    while end < N:
	        for i in range(x):  
	            revarr(start,end,arr)
	            start = start+K
	            end = end+K
	    if start < N and end >= N:
	        revarr(start,N-1,arr)
	    return arr
	    
		
		    


#{ 
 # Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends