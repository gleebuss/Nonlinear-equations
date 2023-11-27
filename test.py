import unittest
import json
from nonlinear_equations import Nonlinear_equations
from sympy import symbols, diff, lambdify, simplify, Poly


class Test_newton(unittest.TestCase):
    '''
    Тесты для метода ньютона
    '''

    def test_correct(self):
        with open("./equations.json", 'r') as f:
            data = json.load(f)

        for i in data["correct"]["newton"]:
            equ, x0 = i
            A = Nonlinear_equations(equ)
            root = A.method_newton(int(x0))
            result = A.is_between(root)
            self.assertTrue(result, f"Ошибка в примере: уравнение='{equ}', начальное приближение={x0}, корень={root}")
    
    def tests_incorrect(self):
        with open("./equations.json", 'r') as f:
            data = json.load(f)

        for i in data["incorrect"]["newton"]:
            equ, x0 = i
            A = Nonlinear_equations(equ)
            with self.assertRaises(Exception, msg="Метод Ньютона не сошелся"):
                root = A.method_newton(int(x0))
                result = A.is_between(root)
                self.assertFalse(result, f"Исключение в примере: уравнение='{equ}', начальное приближение={x0}, корень={root}")


class Test_simplify_newton(unittest.TestCase):
    '''
    Тесты для упрощенного метода ньютона
    '''
    
    def test_correct(self):
        with open("./equations.json", 'r') as f:
            data = json.load(f)

        for i in data["correct"]["simplify_newton"]:
            equ, x0 = i
            A = Nonlinear_equations(equ)
            root = A.simplify_newton_method(int(x0))
            result = A.is_between(root)
            self.assertTrue(result, f"Ошибка в примере: уравнение='{equ}', начальное приближение={x0}, корень={root}")

    
    def test_incorrect(self):
        with open("./equations.json", 'r') as f:
            data = json.load(f)

        for i in data["incorrect"]["simplify_newton"]:
            equ, x0 = i
            A = Nonlinear_equations(equ)
            with self.assertRaises(Exception, msg="Метод Ньютона не сошелся"):
                root = A.simplify_newton_method(int(x0))
                result = A.is_between(root)
                self.assertTrue(result, f"Исключение в примере: уравнение='{equ}', начальное приближение={x0}, корень={root}")
                # assertTrue вызывает исключение (тк ответ неверный) и благодаря assertRaises все работает


class Secant_method(unittest.TestCase):
    '''
    Тесты для метода секущих
    '''

    def test_correct(self):
        with open("./equations.json", 'r') as f:
            data = json.load(f)

        for i in data["correct"]["secant_method"]:
            equ, x0 = i
            A = Nonlinear_equations(equ)
            root = A.secant_method(int(x0))
            result = A.is_between(root)
            self.assertTrue(result, f"Ошибка в примере: уравнение='{equ}', начальное приближение={x0}, корень={root}")

    def tests_incorrect(self):
        with open("./equations.json", 'r') as f:
            data = json.load(f)

        for i in data["incorrect"]["secant_method"]:
            equ, x0 = i
            A = Nonlinear_equations(equ)
            with self.assertRaises(Exception, msg="Метод секущихся не сошелся"):
                root = A.secant_method(int(x0))
                result = A.is_between(root)
                self.assertTrue(result, f"Исключение в примере: уравнение='{equ}', начальное приближение={x0}, корень={root}")
                # assertTrue вызывает исключение (тк ответ неверный) и благодаря assertRaises все работает


class Method_half(unittest.TestCase):
    '''
    Тесты для метода половинного деления
    '''

    @staticmethod
    def find_interval_endpoints(equation, step=1.0, max_iterations=100):
        x = symbols('x')
        f = lambdify(x, equation)
        a, b = 0, step
        iterations = 0

        while f(a) * f(b) >= 0:
            a, b = b, b + step
            iterations += 1
            if iterations > max_iterations:
                raise Exception(f"Не удалось найти конечные точки интервала {equation}")
        return a, b

    def test_correct(self):
        with open("./equations.json", 'r') as f:
            data = json.load(f)

        for i in data["correct"]["method_half"]:
            equ, x0 = i
            A = Nonlinear_equations(equ)
            a, b = self.find_interval_endpoints(equ)
            root = A.method_half(a, b)
            result = A.is_between(root)
            self.assertTrue(result, f"Ошибка в примере: уравнение='{equ}', крайние точки={a,b}, корень={root}")

    def tests_incorrect(self):
        with open("./equations.json", 'r') as f:
            data = json.load(f)

        for i in data["incorrect"]["method_half"]:
            equ, x0 = i
            A = Nonlinear_equations(equ)
            with self.assertRaises(Exception, msg="Не удалось найти конечно точки интервала"):
                a, b = self.find_interval_endpoints(equ)
                root = A.method_half(a, b)
                result = A.is_between(root)
                self.assertTrue(result, f"Исключение в примере: уравнение='{equ}', крайние точки={a,b}, корень={root}")


class Method_chord(unittest.TestCase):
    '''
    Тесты для метода хорд
    '''

    def test_correct(self):
        pass

    def tests_incorrect(self):
        pass

    def tests_exceptionst(self):
        pass



class Theorem_edges_root(unittest.TestCase):
    '''
    Тесты для теоремы о границах расположения корней алгебраического уравнения
    '''

    def test_correct(self):
        pass

    def tests_incorrect(self):
        pass

    def tests_exceptionst(self):
        pass



class Theorem_descartes(unittest.TestCase):
    '''
    Тесты для Теоремы Декарта о количестве действительных корней
    '''

    def test_correct(self):
        pass

    def tests_incorrect(self):
        pass

    def tests_exceptionst(self):
        pass



class Theorem_gua(unittest.TestCase):
    '''
    Тесты для теоремы Гюа о необходимом условии действительности всех корней алгебраического уравнения
    '''

    def test_correct(self):
        pass

    def tests_incorrect(self):
        pass

    def tests_exceptionst(self):
        pass


if __name__ == '__main__':
    unittest.main()


