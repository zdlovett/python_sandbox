#  You are given an array of integers of length n, where each element ranges
#  from 0 to n - 2, inclusive.  --> if there are n numbers but only n-2 choices for the numbers there must be AT LEAST one set of duplicates
#  
#  Prove that at least one  duplicate element must exist, 
#  and give an O(n)-time, O(1)-space algorithm for finding some duplicated element. 
# 
#  -> O(n) time means that you only get to walk the list once
#  -> O(1) space means that there is a fixed number of additional registers that are needed in order to find a dupe
#  --> there *might* be something that makes use of an integer being a member of a fixed range of numbers?
# 
#  You must not modify the array elements during this 
#  process.

# Example input: [ 1,9,7,8,6,8,4,7,3,2 ]
# Example output: [ (7,7), (8,8) ]
#

def find_dup(N):
    "Assuming that only one duplicate exists in the set, return the duplicated value"
    s = 0 # sum of the elements of N
    l = 0 # length of N

    for n in N: # this is the O(n) part of the process
        s += n
        l += 1
    
    s_p = l*( (l-1)/2 )
    return int( l - (s_p - s) - 1 )

if __name__ == "__main__":    
    "Since we only have n-2 options but we have n values we know that there is at least one duplicate."
    
    # generate the lists to test
    n = 100
    for d in range(n-1):#set which value to repeat
        N = []
        for i in range(n-1):#build N
            if len(N) == d:
                N.append(i)
                print( f"dupe:{i}")
            N.append(i)
        
        # run the tests to see if we return thes correct number
        print( f"Duplicate is:{find_dup(N)} (should be:{d})" )
        assert( find_dup(N) == d )