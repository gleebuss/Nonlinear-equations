import unittest
import json
from nonlinear_equations import Nonlinear_equations


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
            result = A.is_between(root, 1e-6)
            self.assertTrue(result)
    
    def tests_incorrect(self):
        pass

    def tests_exceptionst(self):
        pass


class Test_simplify_newton(unittest.TestCase):
    '''
    Тесты для упрощенного метода ньютона
    '''
    
    def test_correct(self):
        pass
    
    def test2(self):
        pass

    def test3(self):
        pass


class Secant_method(unittest.TestCase):
    '''
    Тесты для метода секущих
    '''

    def test_correct(self):
        pass

    def tests_incorrect(self):
        pass

    def tests_exceptionst(self):
        pass


class Method_half(unittest.TestCase):
    '''
    Тесты для метода половинного деления
    '''

    def test_correct(self):
        pass

    def tests_incorrect(self):
        pass

    def tests_exceptionst(self):
        pass


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


