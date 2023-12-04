import re
import time 

#filename = "test_input.txt"
filename = "input.txt"
maxes = {
        "red" : 12,
    "green" : 13,
    "blue" : 14,
}

def main():
    with open(filename) as f:
        line = f.readline()
        res = 0
        total = 0
        bad = 0
        i = 1
        while line:
            # find red matches
            #print(line)
            total += int(re.search("(Game) (\d+)", line).group(2))
            for count, color in re.findall("(\d+) (red|blue|green)", line):
                #print(re.search("(Game) (\d)", line))
                # print(count, color, maxes[color])
                if int(count) > maxes[color]:
                    #print(i)
                    # print(count, color)
                    # print(re.search("(Game) (\d+)", line).group(2))
                    bad += int(re.search("(Game) (\d+)", line).group(2))
                    break
            line = f.readline()
            i += 1
        return total - bad

if __name__ == "__main__":
    start = time.time()
    print(main())
    print(time.time() - start)
