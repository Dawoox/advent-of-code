import re


with open("input.txt", 'r') as file:
    lines = [line.strip().split(":")[1].split("|")[:] for line in file.readlines()]
points = 0
for card in lines:
    card_point, nbr_of_win_nbrs = 0, 0
    win_nbrs = [int(nbr) for nbr in re.findall(r"[0-9]*", card[0]) if nbr != '']
    my_nbrs = [int(nbr) for nbr in re.findall(r"[0-9]*", card[1]) if nbr != '']
    for nbr in my_nbrs:
        if nbr in win_nbrs:
            nbr_of_win_nbrs += 1
    while nbr_of_win_nbrs > 0:
        nbr_of_win_nbrs -= 1
        if card_point == 0:
            card_point = 1
            continue
        else:
            card_point *= 2
    points += card_point
print(points)
