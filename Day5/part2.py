# With inspiration from Jonathan Paulsons solution
import sys

#To represent seeds as list of pairs [(seed,range), (seed,range)]
def make_seeds_tuples(seeds):
    new_seeds = []
    for i in range(0,len(seeds),2):
       new_seeds.append((seeds[i], seeds[i+1]))
    return new_seeds

def mapSrcToDest(mapping):
    retval = []
    for elem in mapping: #Iterate over each src-to-dest entry for the given mapping 
        dest, src, rang = elem
        retval.append((dest, src, rang)) #Appends interval
    return retval

#-------PARSING----------
#Open file and initial parsin
input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
seeds = list(map(int,lines[0].split()[1:])) #Parse seeds to list of int

rest = [elem for elem in lines[1:] if elem.strip() != '']
mappings = []
elems = 0
lst = [] 
for element in rest:
    parts = element.split()
    if len(parts) == 3 and all(part.isdigit() for part in parts): #Parses on length and if digit
         lst.append((int(parts[0]), int(parts[1]), int(parts[2])))
    elif len(lst) != 0: 
        mappings.append(lst)
        lst = []
mappings.append(lst) #Append final lst

seeds = make_seeds_tuples(seeds)
#----PARSING done we end up with seeds in a list of pairs [(seed,range), (seed,range)] and
# mappings which is a list of lists of tuples, eg. 
#  [ 
#   [(50, 98, 2), (52, 50, 48)], 
#   [(0, 15, 37), (37, 52, 2), (39, 0, 15)]
#                                           ]

#We will have to perform mappings 7 times, so we encapsulate mapping functionality in a class 
class Mapper:
    def __init__(self, mappings):
        #Save mapping which is a list of (dst,src,range) tuples as class variable
        self.mappings = mappings

    #Given a list of tuples (seed_l, seed_r) containing endpoints of a seed interval, calculate mappings
    #i.e. find the intervals defined as halfopen intervals, that are of interest
    #There are three intervals: An interval for which seed values are not mapped to a new value, 
    #An interval in the middle where they are mapped and lastly an interval where they are not mapped.
    def map_intervals_a_to_intervals_b(self, seed_range_tuple):
        mapped_intervals = []
        for mapping in self.mappings:
            dest, src_l, range = mapping
            src_r = src_l+range
            non_mapped = []
            #Need to process al possible seed intervals that could be relevant, so continue until we have none leff
            while len(seed_range_tuple) > 0:
                (seed_l,seed_r) = seed_range_tuple.pop()
                left = (seed_l,min(seed_r,src_l))
                middle = (max(seed_l, src_l), min(src_r, seed_r))
                right = (max(src_r, seed_l), seed_r)
                if left[1]>left[0]: #We only want nonempty intervals appended!
                    non_mapped.append(left)
                if middle[1]>middle[0]:
                    #Append the mapped interval endpoints in this case
                    #We wont touch the mapped intervals more in the while loop!
                    mapped_intervals.append((middle[0]-src_l+dest, middle[1]-src_l+dest))
                if right[1]>right[0]:
                    non_mapped.append(right)
            seed_range_tuple = non_mapped
        #Returns both mapped and non_mapped intervals, so can return more intervals than it got
        #We view the seed intervals as input and the mapping functions as certain constants
        return mapped_intervals+seed_range_tuple

mappers = [Mapper(m) for m in mappings]

possibles = []
for seed in seeds:
    seed_l, range = seed
    seed_r = seed_l + range-1
    seed_interval = [(seed_l, seed_r)]
    #Apply all mappers to the seed_interval
    for mapper in mappers:
        #Just overwrite variable in each mapping
        seed_interval = mapper.map_intervals_a_to_intervals_b(seed_interval)
    #Append minimum value calculated for than given seed
    possibles.append(min(seed_interval)[0])
print(min(possibles))