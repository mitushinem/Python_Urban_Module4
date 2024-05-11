from random import randint

MAX_BUNCHES = 5
MAX_BUNCHES_SIZE = 20

_holder = {}
_sorted_key = None


def put_stones():
    """
    Разложить камни
    :return:
    """
    global _holder, _sorted_key
    _holder = {}

    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = randint(1, MAX_BUNCHES_SIZE)
    _sorted_key = sorted(_holder.keys())


def take_from_bunch(position, quantity):
    """
    Взять из кучи
    :param position: позиция
    :param quantity: количество
    :return:
    """
    if position in _holder:
        _holder[position] -= quantity
        return True
    else:
        return False


def get_banches():
    """
    получить позиции камней
    :return:
    """
    res = []
    for key in _sorted_key:
        res.append(_holder[key])
    return res

def is_gameover():
    """ Если конец игры """
    return sum(_holder.values()) == 0