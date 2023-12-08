import sys

input = open(sys.argv[1]).read().strip()
pattern, lines = input.split('\n\n')
lines = lines.split('\n')
currents = []
nexts = []

#Utilize dict as lookup time i O(1), so we preprocess all mappings into a dict
lookup_dict = {}
for line in lines:
    curr, next = line.split('=')
    L, R = next[2:-1].split(',')
    L = L.strip()
    R = R.strip()
    curr = curr.strip()
    next = (L,R)
    lookup_dict.update({curr: next})

#Now, we run the query algorithm
#Initialization step
curr = 'AAA'
nexts = lookup_dict.get(curr)
i = 0
while(curr != 'ZZZ'):
    decision = pattern[i % len(pattern)]
    if decision == 'L': next = nexts[0]
    elif decision == 'R': next = nexts[1]
    else: break
    curr = next
    nexts = lookup_dict.get(curr, None)
    if nexts == None or len(next) != 3 or len(curr) != 3:
        break
    i+=1     
print(i)    