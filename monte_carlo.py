import numpy as np
from scipy.integrate import quad


def monte_carlo(num_points):
    random_x = np.random.uniform(a, b, num_points)
    random_y = np.random.uniform(0, f(b), num_points)
    points_under_curve = sum(random_y <= f(random_x))
    area_ratio = points_under_curve / num_points
    total_area = (b - a) * f(b)
    integral_value = total_area * area_ratio
    return integral_value


def f(x):
    return x ** 3


a = 0
b = 2
num_points = [10000, 20000, 50000, 10, 100, 1000]
analytical_solution_quad, _ = quad(f, a, b)

for points in num_points:
    estimate = monte_carlo(points)
    error = np.abs(estimate - analytical_solution_quad)
    print(f"Кількість точок: {points}, інтеграл: {estimate}, помилка: {error}")
