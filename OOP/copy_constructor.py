class Myclass:

    def __init__(self,attr1,attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def __copy__(self):
        new_obj = type(self)(self.attr1,self.attr2)

        return new_obj
    


original_obj = Myclass('Hello','dev')

copied_obj = original_obj.__copy__()

print("Original object attributes are {} and {}".format(original_obj.attr1,original_obj.attr2))
print("Copied object attributes are {} and {}".format(copied_obj.attr1,copied_obj.attr2))
