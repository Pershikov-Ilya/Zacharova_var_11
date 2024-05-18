import numpy as np
from numba import njit

def f_1_1(x): return np.sqrt(x)

def f_1_2(x): return np.sqrt(x)

def f_1_3(x): return -np.sqrt(x)

def f_1_4(x): return -np.sqrt(x)

def f_2_1(x): return x**2

def f_2_2(x): return -(x**2)

# функция для вычисления интегралов
def simpson(f, a, b, k):
    h = (b - a) / k
    x = [a + i * h for i in range(k + 1)]
    fx = [f(xi) for xi in x]
    s = fx[0] + fx[-1] + 4 * np.sum(fx[1:-1:2]) + 2 * np.sum(fx[2:-1:2])
    return s * h / 3

# Функция для проверки(находится ли точка внутри фигуры)
@njit
def is_real_number(num): return isinstance(num, (int, float))


def point_inside_shape(x, y, f_1_1, f_1_2, f_1_3, f_1_4, f_2_1, f_2_2):
    f_1_1_result = f_1_1(x)
    f_1_2_result = f_1_2(x)
    f_1_3_result = f_1_3(x)
    f_1_4_result = f_1_4(x)
    f_2_1_result = f_2_1(x)
    f_2_2_result = f_2_2(x)

    if all(map(is_real_number, [f_1_1_result, f_1_2_result, f_1_3_result, f_1_4_result, f_2_1_result, f_2_2_result])):
        if ((y <= f_1_1_result) and (y >= f_2_1_result)):
            return True
    return False

def point_inside_shape_1(x, y): return point_inside_shape(x, y, f_1_1, f_1_2, f_1_3, f_1_4, f_2_1, f_2_2)

def point_inside_shape_2(x, y): return point_inside_shape(-x, -y, f_1_1, f_1_2, f_1_3, f_1_4, f_2_1, f_2_2)

def point_inside_shape_3(x, y): return point_inside_shape(x, -y, f_1_1, f_1_2, f_1_3, f_1_4, f_2_1, f_2_2)

def point_inside_shape_4(x, y): return point_inside_shape(-x, y, f_1_1, f_1_2, f_1_3, f_1_4, f_2_1, f_2_2)

# Функция для подсчета количества точек внутри фигуры
def count_point_1(N_points, point_inside_shape_1):
    count = 0
    for _ in range(N_points):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if point_inside_shape_1(x, y): count += 1
    return count

def count_point_2(N_points, point_inside_shape_2):
    count = 0
    for _ in range(N_points):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if point_inside_shape_2(x, y): count += 1
    return count

def count_point_3(N_points, point_inside_shape_3):
    count = 0
    for _ in range(N_points):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if point_inside_shape_3(x, y): count += 1
    return count

def count_point_4(N_points, point_inside_shape_4):
    count = 0
    for _ in range(N_points):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if point_inside_shape_4(x, y): count += 1
    return count

def main():
    # (k) - количество подоотрезков для аппроксимации в функции simpson
    k = 10000
    # (pl) - площадь области, в которой находится наша фигура
    pl = 4

    # фактическая площадь фигуры
    square_of_our_figure = (simpson(f_1_1, 0, 1, k) - (simpson(f_2_1, 0, 1, k))) * 4
    print("Our square:", square_of_our_figure)

    N_points = 10
    while N_points <= 1000000:
         points = count_point_1(N_points, point_inside_shape_1) + count_point_2(N_points, point_inside_shape_2) + count_point_3(N_points, point_inside_shape_3) + count_point_4(N_points, point_inside_shape_4)
         Square = pl * points / N_points
         print(f"N = {N_points}")
         print(f"ПЛОЩАДЬ = {Square}")
         print(f"ПОГРЕШНОСТЬ = {abs(Square - square_of_our_figure) / square_of_our_figure}\n")
         N_points *= 10


if __name__ == "__main__":
    main()
