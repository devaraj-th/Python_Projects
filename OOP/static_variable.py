class Myclass:

    static_variable =0

    def __init__(self,value):
        self.value = value
        Myclass.static_variable +=1


print(Myclass.static_variable)
        

class NewClass:

    @staticmethod
    def my_static_method():
        print('This is a static method')
        return 'hello'


print(NewClass.my_static_method())