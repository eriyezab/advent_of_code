import re
import time 

#filename = "test_input.txt"
filename = "input.txt"

def power(red, green, blue):
    return red * green * blue

def main():
    with open(filename) as f:
        line = f.readline()
        res = 0
        while line:
            # find red matches
            #print(line)
            counts = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            for count, color in re.findall("(\d+) (red|blue|green)", line):
                if int(count) > counts[color]:
                    counts[color] = int(count)
            line = f.readline()
            res += power(**counts)
        return res

if __name__ == "__main__":
    start = time.time()
    print(main())
    print(time.time() - start)
