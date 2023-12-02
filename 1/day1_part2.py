filename = "input.txt"
#filename = "test_input.txt"
numbers = '1234567890'
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
three = {
    'one': '1',
    'two': '2',
    'six': '6'
}
four = {
    #'zero': '0',
    'four': '4',
    'five': '5',
    'nine': '9'
}
five = {
    'three': '3',
    'seven': '7',
    'eight': '8'
}

def find_first(line):
    for i,c in enumerate(line):
        # print(i,c)
        if c in numbers:
            return c
        else:
            if i >= 2:
                word = line[i-2:i+1]
                if word in three:
                    return three[word]
            if i >= 3:
                word = line[i-3:i+1]
                if word in four:
                    return four[word]
            if i >= 4:
                word = line[i-4:i+1]
                if word in five:
                    return five[word]

def find_last(line):
    line = line[::-1]
    for i,c in enumerate(line):
        if c in numbers:
            return c
        else:
            if i >= 2:
                word = line[i-2:i+1][::-1]
                if word in three:
                    return three[word]
            if i >= 3:
                word = line[i-3:i+1][::-1]
                if word in four:
                    return four[word]
            if i >= 4:
                word = line[i-4:i+1][::-1]
                if word in five:
                    return five[word]

def main():
    with open(filename) as f:
        res = 0
        line = f.readline()
        while line:
            #print(line)
            first = find_first(line)
            #print(first)
            last = find_last(line)
            #print(last)
            print(int(first + last))
            res += int(first + last)
            line = f.readline()
        return res


            
    
if __name__ == "__main__":
    print(main())
