import numpy as np
from sympy import symbols, diff, lambdify


class Nonlinear_equations:
    '''
    Описание
    ---------
    Класс для решения нелинейних уравнение
    '''

    def __init__(self, equations):
        '''
        Описание
        --------
        Конструктор класса для иницилизации данных

        Параметры
        ----------
        equations : str
            Функция, для которой мы пытаемся аппроксимировать решение f(x)=0
        '''

        self.x = symbols('x')
        self.equations = equations
        self.f = lambdify(self.x, equations)
        self.df = lambdify(self.x, diff(self.equations, self.x))

    def method_newton(self, x0, eps=1e-6):
        '''
        Описание
        --------
        Метод ньютона

        Параметры
        ----------
        x0 : int
            Начальное приближение
        eps : float
            Точность, с которой мы ищем решение

        Возвращает
        ----------
        Одно из решений уравнений или же выдает исключение, если задано неправильно начальное приближение
        '''

        max_iter = 1000
        i = 0
        while i < max_iter:
            i += 1
            x1 = x0 - (self.f(x0) / self.df(x0))
            if abs(x1 - x0) <= eps:
                return x1
            x0 = x1
        raise Exception("Метод Ньютона не сошелся")

    def simplify_newton_method(self, x0, eps=1e-6):
        df_value = self.df(x0)

        max_iter = 1000
        i = 0
        while i < max_iter:
            i += 1
            x1 = x0 - (self.f(x0) / df_value)
            if abs(x1 - x0) <= eps:
                return x1
            x0 = x1
        raise Exception("Упрощенный метод Ньютона не сошелся")

    def secant_method(self, x0, eps=1e-6, delta=0.1):
        df0_value = (self.f(x0)-self.f(x0-delta))/delta
        x1 = x0 - self.f(x0)/df0_value
        max_iter = 1000
        i = 0
        while i < max_iter:
            i += 1
            xk = x1 - (self.f(x1) / (self.f(x1)-self.f(x0))) * (x1-x0)
            if abs(xk - x1) <= eps:
                return x1
            x0 = x1
            x1 = xk

    def is_between(self, x, eps=1e-6):
        return -eps < self.f(x) < eps