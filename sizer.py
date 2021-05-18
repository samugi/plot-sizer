import argparse
import config as c

klist = (c.k32,c.k33,c.k34,c.k35)
ktlist = (c.k32t,c.k33t,c.k34t,c.k35t)
disk_size_bytes = c.disk_size_bytes
temp_disk_size_bytes = c.temp_disk_size_bytes

def main():
    parser = argparse.ArgumentParser()   
    parser.add_argument("-d", "--disksize", help="use this disk size (bytes)", required=False) 
    parser.add_argument("-t", "--tempsize", help="temporary disk size (bytes)", required=False)
    args = parser.parse_args()

    global disk_size_bytes, temp_disk_size_bytes
    if args.disksize:
        disk_size_bytes = int(args.disksize)
    if args.tempsize:
        temp_disk_size_bytes = int(args.tempsize)

    get_combinations(disk_size_bytes, temp_disk_size_bytes)

def sort_by_wasted(element):
    return element["wasted"]

def get_combinations(disk_size, tmp_size):
    print("Calculating plots combinations for a disk of size: "+str(disk_size)+" bytes")
    maxs = [disk_size//el if tmp_size > ktlist[i] else 0 for i, el in enumerate(klist)]
    combinations = []

    for k32m in range(maxs[0]+1):
        for k33m in range(maxs[1]+1):
            for k34m in range(maxs[2]+1):
                for k35m in range(maxs[3]+1):
                    total = k32m*c.k32+k33m*c.k33+k34m*c.k34+k35m*c.k35
                    if total <= disk_size and total > disk_size - c.k32:
                        valid_combi_str = "%4d %4d %4d %4d" % (k32m, k33m, k34m, k35m)
                        wasted = disk_size - total
                        combinations.append({"combi_str": valid_combi_str, "wasted": wasted})
    combinations.sort(key=sort_by_wasted)
    combinations = combinations[:100]

    print("Valid combinations:\n K32  k33  k34  k35     Wasted (MB)")
    for co in combinations:
        print(str(co["combi_str"]+"     "+str(co["wasted"]/1000000)))

if __name__ == "__main__":
    main()