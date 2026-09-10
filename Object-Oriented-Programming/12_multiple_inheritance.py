class Father:
    def father_feature(self):
        print("Good at mathematics")


class Mother:
    def mother_feature(self):
        print("Good at music")


class Child(Father, Mother):
    pass


child = Child()

child.father_feature()
child.mother_feature()
