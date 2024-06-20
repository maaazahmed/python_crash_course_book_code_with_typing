squares:list[int] = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

from typing import Union

# alien_0:dict[str, Union[str, int]] = {"color":"green", "points":5}

# print(alien_0["color"])
# print(alien_0["points"])



# Typss = dict[str, Union[str, int]]

# alien_0:Typss = {'color': 'green', 'points': 5}
# alien_1:Typss = {'color': 'yellow', 'points': 10}
# alien_2:Typss = {'color': 'red', 'points': 15}


# aliens:list[Typss] = [alien_0, alien_1, alien_2]

number = input("Enter a number, and I'll tell you if it's even or odd: ")

print(number)