# squares:list[str] = []
squares:list[int] = []

for value in range(1,11):
    square:int =  value ** 2
    squares.append(square)

print(squares)


from typing import Union



alien_0:dict[str, Union[str, int]] = {'color': 'green', 'points': 5}
alien_1:dict[str, Union[str, int]] = {'color': 'yellow', 'points': 10}
alien_2:dict[str, Union[str, int]] = {'color': 'red', 'points': 15}


aliens:list[dict[str, Union[str, int]]] = [alien_0, alien_1, alien_2]