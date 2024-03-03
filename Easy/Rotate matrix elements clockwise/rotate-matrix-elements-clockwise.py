#User function Template for python3

class Solution:
    def rotateMatrix(self, M, N, Mat):
        #code here
        sr = 0
        sc = 0
        er = M-1
        ec = N-1
        while sr < er and sc < ec: 
            
            prev = Mat[sr+1][sc]
            
            for j in range(sc, ec+1):
                Mat[sr][j] , prev = prev, Mat[sr][j]
            sr = sr+1
            
            for i in range(sr, er+1):
                Mat[i][ec] , prev = prev, Mat[i][ec]
            ec = ec -1
            
            for j in range(ec, sc-1, -1):
                Mat[er][j] , prev = prev, Mat[er][j]
            er = er-1
            
            for i in range(er, sr-1, -1):
                Mat[i][sc] , prev = prev , Mat[i][sc]
            sc = sc+1
            
        return Mat


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        ans=ob.rotateMatrix(N,M,A)
        for i in range(N):
            for j in range(M):
                print(ans[i][j],end=" ")
            print()    
# } Driver Code Ends