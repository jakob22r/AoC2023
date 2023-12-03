import sys
import re


def does_num_count(match, line, line_prior, line_after):
    adjacents = 0
    mult = 1

    pattern_sym = re.compile(r'[^0-9.]')
    number = match.group()
    start_index, end_index = match.span()
    end_index -= 1
    #Simple case adjacent
    if start_index != 0:
        if line[start_index-1] != '.': 
            return True

    if end_index < len(line)-1:
        if line[end_index+1] != '.': 
            return True
        
    line_prior_symbols = pattern_sym.finditer(line_prior)
    line_after_symbols = pattern_sym.finditer(line_after)

    for sym in line_prior_symbols:
        symbol = sym.group()
        s_idx, e_idx = sym.span() #Use only start idx

        #Check diagonal condition
        num_width = end_index-start_index+1
        if (abs(s_idx - start_index) <= num_width)  and abs(s_idx - start_index)  <= 1 or abs(s_idx - end_index) <= 1:
            print(f"Symbol {symbol} below is diagonal/adj to {number}")
            adjacents += 1
            mult *= number

    for sym in line_after_symbols:
        symbol = sym.group()
        s_idx, e_idx = sym.span() #Use only start idx

        #Check diagonal condition
        num_width = end_index-start_index+1
        if (abs(s_idx - start_index) <= num_width) and abs(s_idx - start_index) <= 1 or abs(s_idx - end_index) <= 1:
            print(f"Symbol {symbol} above is diagonal/adj to {number}")
            adjacents += 1
            mult *= number


    if adjacents == 2:
        print(f"Sum increased by {mult}")
        return mult
    else:
        return 0

pattern = re.compile(r'\d+')
input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
sum = 0
for i,line in enumerate(lines):

    emptystr = '.' * len(line)

    # Finds all numbers on the line
    matches = pattern.finditer(line)

    for match in matches:
        counts = False

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


