def subarrayXor(self, arr, k):
        mp = {}
        ans = 0
        xor = 0
        for i in range(len(arr)):
            xor ^= arr[i]
            if xor==k:
                ans+=1
            
            if xor^k in mp:
                ans += mp[xor^k]
            
            if xor not in mp:
                mp[xor]=1
            else:
                mp[xor]+=1
        return ans
        
arr = [4, 2, 2, 6, 4]
k = 6
result = subarrayXor(arr,k)
print(result)