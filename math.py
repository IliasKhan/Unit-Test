MAX = 7
class math:
  def factorial(self, number):
    result = 1
    for num in range(1, number+1):
      result = result * num
    return result

  def is_prime(self, number):
    for num in range(2, number):
      if number%num == 0:
        return False
    return True

  def gcd(self, number1, number2):
    if number2 == 0:
      return number1
    return self.gcd(number2, number1%number2)


math_obj = math()
math_obj.factorial(MAX)
math_obj.is_prime(MAX)
math_obj.gcd(MAX, MAX+1)