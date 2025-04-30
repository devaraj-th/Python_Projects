class MathUtils:
    @staticmethod
    def square(num):
        return num * num
    @staticmethod
    def factorial(num):

        if num ==0 or num ==1:
            return 1
        else:
            return num * MathUtils.factorial(num - 1)
        

print(MathUtils.square(5))
print(MathUtils.factorial(5))