DIGITS_STR = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

if __name__ == "__main__":
    with open("part2/input.txt", 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    rst = 0
    for line in lines:
        first = None
        last = None
        for i in range(len(line)):
            for d in range(len(DIGITS_STR)):
                if line[:i].__contains__(DIGITS_STR[d]):
                    first = d + 1
                    break
            if first is not None:
                break
            if line[i].isnumeric():
                first = int(line[i])
                break
        for i in range(1, len(line) + 1):
            for d in range(len(DIGITS_STR)):
                if line[len(line)-i:].__contains__(DIGITS_STR[d]):
                    last = d + 1
                    break
            if last is not None:
                break
            if line[-i].isnumeric():
                last = int(line[-i])
                break
        if first is not None and last is not None:
            rst += first * 10 + last
    print(f"Calibration value: {rst}.")
