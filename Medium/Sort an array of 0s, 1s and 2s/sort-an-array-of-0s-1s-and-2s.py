#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        start = 0
        end = n-1
        mid = 0
        while mid <= end:
            if arr[mid] == 2:
                arr[mid], arr[end] = arr[end], arr[mid]
                end = end - 1 
                
            elif arr[mid] == 0:
                arr[mid], arr[start] = arr[start], arr[mid]
                start = start+1
                mid = mid+1
                
            else:
                mid = mid+1
                
        return arr
                
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends