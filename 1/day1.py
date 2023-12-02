filename = "input.txt"
def find_first(line):
    for c in line:
        if c in '1234567890':
            return c

def find_last(line):
    for c in line[::-1]:
        if c in '1234567890':
            return c

def main():
    with open(filename) as f:
        res = 0
        line = f.readline()
        while line:
            first = find_first(line)
            last = find_last(line)
            res += int(first + last)
            line = f.readline()
        return res

            
    
if __name__ == "__main__":
    print(main())
