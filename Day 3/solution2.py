import sys
import re


def does_num_count(match, line, line_prior, line_after):
    adjacents = 0
    mult = 1
    star = match.group()
    start_index, end_index = match.span()

    pattern_num = re.compile(r'\d+')

    #Three cases, same line below or above
    line_cur_symbols = pattern_num.finditer(line) #Finds numbers in current line, i.e. simple adj case
    line_prior_symbols = pattern_num.finditer(line_prior)
    line_after_symbols = pattern_num.finditer(line_after)

    for num in line_cur_symbols:
        number = num.group()
        s_idx, e_idx = num.span() #Use only start idx
        e_idx -= 1
        #Check if adj on same line
        num_width = e_idx-s_idx+1
        if abs(start_index-s_idx) <= 1 or abs(start_index-e_idx) <= 1:
            adjacents += 1
            mult *= int(number)
            print(f"Symbol {star} on the same line adj to {number}")

    for num in line_prior_symbols:
        number = num.group()
        s_idx, e_idx = num.span() 
        e_idx -= 1

        #Check diagonal condition
        num_width = e_idx-s_idx+1
        if (abs(s_idx - start_index) <= num_width)  and abs(s_idx - start_index)  <= 1 or abs(start_index - e_idx) <= 1:
            print(f"Symbol {star} is below/adj to {number}")
            adjacents += 1
            mult *= int(number)

    for num in line_after_symbols:
        number = num.group()
        s_idx, e_idx = num.span() 
        e_idx -= 1

        #Check diagonal condition
        num_width = e_idx-s_idx+1
        if (abs(s_idx - start_index) <= num_width) and abs(s_idx - start_index) <= 1 or abs(start_index - e_idx) <= 1:
            print(f"Symbol {star} above is diagonal/adj to {number}")
            adjacents += 1
            mult *= int(number)

    if adjacents == 2:
        print(f"Sum increased by {mult}")
        return mult
    else:
        return 0

pattern = re.compile(r'[*]')
input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
sum = 0
for i,line in enumerate(lines):

    emptystr = '.' * len(line)

    # Finds all numbers on the line
    matches = pattern.finditer(line)

    for match in matches:

        #First line
        if (i == 0):
            sum += does_num_count(match, line, emptystr, lines[i+1])
        #Standard case
        elif (i>0 and i<len(lines) - 1):
            sum += does_num_count(match, line, lines[i-1], lines[i+1])
        #Last line
        else:
            sum += does_num_count(match, line, lines[i-1], emptystr)

print(sum)

