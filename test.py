from unit_test_framework import equal_to
from math import math
class test(math):
  def test_factorial(self, number, result):
    print("-:factorial-Test:-")
    equal_to(self.factorial(number), result)

  def test_is_prime(self, number, result):
    print("-:is_prime-Test:-")
    equal_to(self.is_prime(number), result)

  def test_gcd(self, number1, number2, result):
    print("-:GCD-Test:-")
    equal_to(self.gcd(number1, number2), result)

test_obj = test()
test_obj.test_factorial(5, 120)
test_obj.test_is_prime(7, True)
test_obj.test_gcd(4, 8, 4)
