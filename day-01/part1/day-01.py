if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    rst = 0
    for line in lines:
        first = None
        last = None
        for i in range(len(line)):
            if line[i].isnumeric():
                first = int(line[i])
                break
        for i in range(1, len(line) + 1):
            if line[-i].isnumeric():
                last = int(line[-i])
                break
        if first is not None and last is not None:
            rst += first * 10 + last
    print(f"Calibration value: {rst}.")
