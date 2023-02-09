class parent_Class:
    def __init__(self, num):
        self.num = num

    def print_num(self):
        print(self.num)

class child_Class(parent_Class):
    pass

obj_num = child_Class(10)
obj_num.print_num()



