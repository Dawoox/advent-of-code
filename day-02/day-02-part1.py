import re


def is_round_possible(game: list[str]) -> bool:
    for x in range(len(game)):
        nbr_blue = re.findall(r"[0-9]+?(?= blue)", game[x])
        nbr_blue = int(nbr_blue[0]) if nbr_blue else 0
        nbr_red = re.findall(r"[0-9]+?(?= red)", game[x])
        nbr_red = int(nbr_red[0]) if nbr_red else 0
        nbr_green = re.findall(r"[0-9]+?(?= green)", game[x])
        nbr_green = int(nbr_green[0]) if nbr_green else 0
        if nbr_red > 12:
            return False
        if nbr_green > 13:
            return False
        if nbr_blue > 14:
            return False
    return True


if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    games = dict()
    rst = 0
    for line in lines:
        game_number = int(re.findall(r"[0-9]*=?(?=:)", line)[0])
        games[game_number] = line.split(':')[1][1:].split("; ")
    for i in range(1, 1 + len(games.keys())):
        if is_round_possible(games[i]):
            rst += i
    print(f"The sum of id of the possible games is {rst}")
