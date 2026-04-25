class AlternateElement:

    def __init__(self):
        pass

    def get_alternate_element(self, arr):

        # list of alternative elements
        # return arr[::2] 
        
        alternate_arr = []
        # Traverse through alternative elements and append them
        for i in range (0, len(arr),2):
            alternate_arr.append(arr[i])

        return alternate_arr

    def get_alternate_element_rec(self, arr, res, idx = 0):
        # Step 1: Check the index exceeds the arr length 
        if(idx >= len(arr)):
            return res
        
        # Step 2: Append the res arr with arr[idx]
        res.append(arr[idx])

        # Step 3: Call the same func by incre the idx by 2 
        return self.get_alternate_element_rec(arr, res, idx + 2)
    

        
