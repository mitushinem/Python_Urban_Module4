from num_engine import get_banches, put_stones, take_from_bunch, is_gameover
from termcolor import cprint, colored



put_stones()
user_number = 1

while True:
    cprint('Текущая позиция', color='green', force_color=True)
    cprint(get_banches(), color='green', force_color=True)
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint(f'Ход игрока {user_number}', color=user_color, force_color=True)
    pos = input(colored('Откуда берем? ', color=user_color, force_color=True))
    qua = input(colored('Сколько берем? ', color=user_color, force_color=True))

    take_from_bunch(position=int(pos), quantity=int(qua)) #Сделали ход

    if is_gameover():
        break

    user_number = 2 if user_number == 1 else 1

cprint(f'Выйграл игрок {user_number}', color='red', force_color=True)