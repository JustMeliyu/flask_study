# encoding:utf-8


class Student(object):
    def __init__(self, name):
        self.name = name

    def study(self):
        n = self.name
        print("studing : {0}".format(self.name))


class Score(Student):
    def __init__(self, name):
        print name
        super(Score, self).__init__(name)

    def study(self):
        # print(getattr(super(Score, self).study, "n"))
        print "ss"
        super(Score, self).study()


try:
    1 / 1
except ValueError:
    print "aa"
finally:
    print "finally"
