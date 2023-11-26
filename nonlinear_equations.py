import numpy as np
from sympy import symbols, diff, lambdify, simplify, Poly


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
        self.polynomial = simplify(equations).is_polynomial()

    def method_newton(self, x0, eps=1e-3) -> float:
        '''
        Описание
        --------
        Метод Ньютона

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

    def simplify_newton_method(self, x0, eps=1e-3) -> float:
        '''
        Описание
        --------
        Упрощенный метод Ньютона

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

    def secant_method(self, x0, eps=1e-3, delta=0.1) -> float:
        '''
        Описание
        --------
        Метод секущих

        Параметры
        ----------
        x0 : int
            Начальное приближение
        eps : float
            Точность, с которой мы ищем решение
        delta : float
            Малая положительная величина

        Возвращает
        ----------
        Одно из решений уравнений или же выдает исключение, если задано неправильно начальное приближение
        '''

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

    def method_half(self, a, b, eps=1e-3):
        '''
        Описание
        --------
        Метод половинного деления

        Параметры
        ----------
        a : int
            Левая конечная точка отрезка
        b : int
            Правая конечная точка отрезка   
        eps : float
            Точность, с которой мы ищем решение

        Возвращает
        ----------
        Одно из решений уравнений или же выдает None, если задан неправильно начальный отрезок
        '''
        if (self.f(a) * self.f(b) >= 0):
            return None
        while b-a > eps:
            c = (a+b)/2
            if (self.f(a) * self.f(c) < 0):
                b = c
            elif (self.f(b) * self.f(c) < 0):
                a = c
            x = (a+b)/2
        return x

    def method_chord(self, a, b, eps=1e-3, max_iter=1000):
        '''
        Описание
        --------
        Метод хорд

        Параметры
        ----------
        a : int
            Левая конечная точка отрезка
        b : int
            Правая конечная точка отрезка
        eps : float
            Точность, с которой мы ищем решение
        max_iter : int
            Максимальное количество итераций

        Возвращает
        ----------
        Одно из решений уравнений или же выдает исключение
        '''
        i = 0
        while i < max_iter:
            i += 1
            c = b - ((self.f(b) * (a - b)) / (self.f(a) - self.f(b)))

            if abs(c - b) <= eps:
                return c

            a = b
            b = c

        raise Exception("Метод хорд не сошелся")

    def theorem_edges_root(self) -> list:
        '''
        Описание
        --------
        Теорема о границах расположения корней алгебраического уравнения

        Возвращает
        ----------
        Список из верхней и нижней границы
        '''

        if (self.polynomial == False):
            raise ValueError("Не является алгебраическим уравнением")

        poly = Poly(self.equations, self.x).all_coeffs()
        A = np.max(np.abs(poly[1:]))
        B = np.max(np.abs(poly[:-1]))

        r = 1 / (1 + B / abs(poly[-1]))
        R = 1 + A / abs(poly[0])

        return [r, R]
    
    def theorem_descartes(self) -> list:
        '''
        Описание
        --------
        Теорема Декарта о количестве действительных корней

        Возвращает
        ----------
        Список из двух чисел, число положительных и отрицательных корней
        '''

        if (self.polynomial == False):
            raise ValueError("Не является алгебраическим уравнением")
        
        poly = Poly(self.equations, self.x).all_coeffs()

        def change_signs(coeff):
            coeff[1:-1] = [-k if i % 2 == 0 else k for i, k in enumerate(coeff[1:-1])]
            return coeff

        positive = 0
        for i in range(len(poly) - 1):
            if poly[i] * poly[i+1] < 0:
                positive += 1

        negative = 0
        change_poly = change_signs(poly)

        for i in range(len(change_poly) - 1):
            if change_poly[i] * change_poly[i+1] < 0:
                negative += 1

        return [positive, negative]

    def theorem_gua(self) -> bool:
        '''
        Описание
        --------
        Теорема Гюа о необходимом условии действительности всех корней алгебраического уравнения

        Возвращает
        ----------
        True, если все корни действительные, False в противном случае.
        '''

        if (self.polynomial == False):
            raise ValueError("Не является алгебраическим уравнением")
        
        poly = Poly(self.equations, self.x).all_coeffs()

        return all(poly[i] ** 2 > poly[i - 1] * poly[i + 1] for i in range(1, len(poly) - 1))
    
    def is_between(self, x, eps=1e-3) -> bool:
        '''
        Описание
        --------
        Проверяет находится ли корень в окресности нуля

        Параметры
        ----------
        x : int
            Корень нелинейного уравнения
        eps : float
            Точность, с которой мы ищем решение

        Возвращает
        ----------
        True, если корень находится в окресности нуля, False в противном случае.
        '''

        return -eps < self.f(x) < eps