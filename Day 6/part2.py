import sys

#Given a time and the current best distance, what are the possible number of ways to beat this:
def num_ways_to_win_linear(time,dist):
    cnt = 0
    for i in range(time+1):
        traveled = i*(time-i)
        if traveled > dist:
            cnt += 1
    return cnt

def num_ways_to_win_bin(time, dist):
    # i*(time-i) will be in the middle and this is here we find our op solution
    # Assume winner solution in the middle, i.e. i = int(t/2) exists
    traveled = lambda i: i * (time - i)
    #Find first occurence on left side of optimal solution which is a winn
    l = 0
    r = int(t/2) #This is the optimal solution which we know must exist
    while l <= r:
        m = int(l+(r-l)/2) #To avoid overflows
        if traveled(m) >= dist:
            r = m - 1
        else:
            l = m + 1
    #This is the 'lowest' index for a valid win
    lowest = l
    #Assumming symmetry, we can figure out the highest index for a valid win
    middle = int(time/2) #This is the index for which we are certain there is a valid win
    last = middle + (middle-lowest)
    return (last-lowest) + 1


# --- PARSING ---
input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
t  = int(''.join(filter(str.isdigit, lines[0])))
d  = int(''.join(filter(str.isdigit, lines[1])))

print(num_ways_to_win_bin(t, d))
print(num_ways_to_win_linear(t, d))

