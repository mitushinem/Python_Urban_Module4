from random import randint

MAX_BUNCHES = 5

_holder = []

def put_stones():
    """
    Разложить камни
    :return:
    """
    global _holder
    _holder = []

    for i in range(MAX_BUNCHES):
        _holder.append(randint(1 ,20))


def take_from_bunch(position, quantity):
    """
    Взять из кучи
    :param position: позиция
    :param quantity: количество
    :return:
    """
    if 1 <= position <= len(_holder):
        _holder[position - 1] -= quantity



def get_banches():
    """
    получить позиции камней
    :return:
    """
    return _holder

def is_gameover():
    """ Если конец игры """
    return sum(_holder) == 0