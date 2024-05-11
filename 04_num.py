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

    step_succesed = take_from_bunch(position=int(pos), quantity=int(qua)) #Сделали ход
    if step_succesed:
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('Невозможный ход', color='red', force_color=True)
    if is_gameover():
        break

cprint(f'Выйграл игрок {user_number}', color='red', force_color=True)