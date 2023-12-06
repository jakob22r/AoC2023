import sys

#Maps a list of sources to a list of destinations. Returns a list of touples containing mappings (src_l, src_r, dest_l, dest_r)
def mapSrcToDest(mapping):
    retval = []
    for elem in mapping: #Iterate over each src-to-dest entry for the given mapping 
        dest, src, rang = elem
        retval.append((src,src+rang-1,dest,dest+rang-1)) #Appends interval
    return retval

#Maps a seed to final location in a recursive manner
def mapseed(seed, mappings, i):
    if i == len(mappings): #Base case, done mapping, stop
        return seed
    else:
        mapping = mappings[i]
        for elem in mapping:
            src_l, src_r, dest_l, dest_r = elem
            #Means seed is in interval for which we have a mapping
            if src_l <= seed and seed <= src_r:
                #Find dest and call recursively
                dest = (seed-src_l) + dest_l
                return mapseed(dest,mappings,i+1) #If mapping return mapping
        return mapseed(seed,mappings,i+1) #If no mapping return itseld

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
seeds = list(map(int,lines[0].split()[1:])) #Parse seeds to list of ints

rest = [elem for elem in lines[1:] if elem.strip() != ''] #Everything except seeds
mappings = [] #List of lists of touples with data for each mapping

elems = 0
lst = [] 

#Lst is a temp var, this results in a list of lists of tuples so we have data grouped properly
for element in rest:
    parts = element.split()
    if len(parts) == 3 and all(part.isdigit() for part in parts): #This must mean a number
         lst.append((int(parts[0]), int(parts[1]), int(parts[2])))
    elif len(lst) != 0: 
        mappings.append(lst)
        lst = []
mappings.append(lst) #Append final lst

#Computes mapping intervals
final_mappings = [mapSrcToDest(elem) for elem in mappings]
result = min([mapseed(seed,final_mappings,0) for seed in seeds])
print(result)