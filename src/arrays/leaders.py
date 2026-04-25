from utils.helper import max


class Leaders:

    def __init__(self):
        pass

    def leaders_array(self, arr):
        # Step 1: Edge Case: If arr is empty return 
        if not arr:
            return []

        res = []
        n = len(arr)
        right_max = [-1] * n
        right_max[-1] = arr[-1] # last value will be max in that pos

        # Step 2: build right max array
        for i in range(n-2,-1,-1):
            right_max[i] = max(arr[i], right_max[i+1])

        # print(right_max)

        # Step 3: If Array element and right max are same, append to res
        for i in range(n):
            if(arr[i] == right_max[i]):
                res.append(arr[i])
        
        return res


        
