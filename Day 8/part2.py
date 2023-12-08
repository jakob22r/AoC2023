import sys
import math

input = open(sys.argv[1]).read().strip()
pattern, lines = input.split('\n\n')
lines = lines.split('\n')

currs = []
#Utilize dict as lookup time i O(1), so we preprocess all mappings into a dict, put all startswith A into our currs dict
lookup_dict = {}
for line in lines:
    curr, next = line.split('=')
    L, R = next[2:-1].split(',')
    L = L.strip()
    R = R.strip()
    curr = curr.strip()
    if curr.endswith('A'):
        currs.append(curr)
    next = (L,R)
    lookup_dict.update({curr: next})

#Algorithm from part 1
def solve(num):
    curr = num
    nexts = lookup_dict.get(curr)
    i = 0
    while(not(curr.endswith('Z'))):
        decision = pattern[i % len(pattern)]
        if decision == 'L': next = nexts[0]
        elif decision == 'R': next = nexts[1]
        else: break
        curr = next
        nexts = lookup_dict.get(curr, None)
        if nexts == None or len(next) != 3 or len(curr) != 3:
            break
        i+=1     
    return i

#Generic LCM function
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

#Get LCM of all in the lst
def lcm_of_list(numbers):
    result = 1
    for number in numbers:
        result = lcm(result, number)
    return result

#Calculate solution steps for all entries in currs, and find the LCM of these
solutions = []
for c in currs:
    solutions.append(solve(c))
print(lcm_of_list(solutions))

