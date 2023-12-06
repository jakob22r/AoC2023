import sys

#Given a time and the current best distance, what are the possible number of ways to beat this:
def num_ways_to_win(time,dist):
    #Count number of ways to beat currect best
    cnt = 0
    # I is how many millisecs we hold the button for, actuall
    for i in range(time+1):
        speed = i #pr millisecond
        time_to_move = time-i
        traveled = speed * time_to_move
        if traveled > dist:
            cnt += 1
    return cnt

# --- PARSING ---
input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
times  = list(map(int,lines[0].split()[1:]))
dists  = list(map(int,lines[1].split()[1:]))

mult = 1
for t, d in zip(times,dists):
    mult *= num_ways_to_win(t, d)
print(mult)
