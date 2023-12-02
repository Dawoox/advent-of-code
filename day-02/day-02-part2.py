import math
import re


def find_lowest_nbr_cubes(game: list[str]) -> tuple[int, int, int]:
    max_red, max_green, max_blue = 0, 0, 0
    for x in range(len(game)):
        nbr_blue = re.findall(r"[0-9]+?(?= blue)", game[x])
        nbr_blue = int(nbr_blue[0]) if nbr_blue else 0
        nbr_red = re.findall(r"[0-9]+?(?= red)", game[x])
        nbr_red = int(nbr_red[0]) if nbr_red else 0
        nbr_green = re.findall(r"[0-9]+?(?= green)", game[x])
        nbr_green = int(nbr_green[0]) if nbr_green else 0
        if nbr_red > max_red:
            max_red = nbr_red
        if nbr_green > max_green:
            max_green = nbr_green
        if nbr_blue > max_blue:
            max_blue = nbr_blue
    return max_red, max_green, max_blue


if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    games = dict()
    rst = 0
    for line in lines:
        game_number = int(re.findall(r"[0-9]*=?(?=:)", line)[0])
        games[game_number] = line.split(':')[1][1:].split("; ")
    for i in range(1, 1 + len(games.keys())):
        rst += math.prod(find_lowest_nbr_cubes(games[i]))
    print(f"The sum of powers of the minimal number of cubes is {rst}")
