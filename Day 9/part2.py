import sys

def preprocess(line):
    vals = line.split()
    vals = [int(v) for v in vals]
    retval = []
    retval.append(vals)

    while True:
        checksum = 0
        newvals = []
        for i in range(len(vals)-1):
            newval = vals[i+1] - vals[i]
            checksum += newval
            newvals.append(newval)
        retval.append(newvals)
        vals = newvals
        if checksum == 0:
            break
    return retval

def extrapolate(values):
    extp = 0 #Extrapolated val in each iteration
    for i in range(len(values)-2,-1,-1): #Iterate backwards to fill in extrapolated vals
        increasing = (values[i])[0] #first elem
        #print(f"To the right {increasing}, below {extp}, sum {increasing - extp}")
        extp = increasing - extp
    return extp 

input = open(sys.argv[1]).read().strip()
lines = input.split('\n')

sum = 0
for l in lines:
    ret = preprocess(l)
    sum += extrapolate(ret)

print(sum)



