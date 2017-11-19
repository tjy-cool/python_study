
class B:
    def __conn(self):
        print('conn')


class A(B):
    def request(self):
        self.__conn()


obj = A()
obj.request()
