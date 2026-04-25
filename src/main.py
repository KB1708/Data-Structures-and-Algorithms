from arrays.alternate_element import AlternateElement 
from arrays.leaders import Leaders 

if __name__ == "__main__":

    lead = Leaders()
    arr = [1, 2, 3, 4, 5, 2]
    res = lead.leaders_array(arr)
    print(res)