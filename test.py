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


if __name__ == '__main__':
    unittest.main()
