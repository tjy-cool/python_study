class A(object):
    def request(self):
        print('A.request')

    def finish(self):
        print('A.finish')


class C(A):
    def request(self):
        self.process()
        print('C.request')

    def finish(self):
        print('C.finish')


class B(object):
    def request(self):
        print('B.request')

    def process(self):
        print('B.process')
        self.finish()

    def finish(self):
        print('B.finish')


class D(C, B):
    pass


obj = D()
obj.request()
