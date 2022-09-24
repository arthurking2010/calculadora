from calculadora.utils import obtener_fracciones


def resta(a, b):
    minuendo = obtener_fracciones(a)
    sustraendo = obtener_fracciones(b)
    return minuendo - sustraendo


def suma(a, b):
    sumando_a = obtener_fracciones(a)
    sumando_b = obtener_fracciones(b)
    return sumando_a + sumando_b


def multiplica(a, b):
    multiplicando = obtener_fracciones(a)
    multiplicador = obtener_fracciones(b)
    return multiplicando * multiplicador


def division(a, b):
    dividendo = obtener_fracciones(a)
    divisor = obtener_fracciones(b)
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return "Division entre cero"
