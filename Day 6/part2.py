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
t  = int(''.join(filter(str.isdigit, lines[0])))
d  = int(''.join(filter(str.isdigit, lines[1])))

print(num_ways_to_win(t, d))

