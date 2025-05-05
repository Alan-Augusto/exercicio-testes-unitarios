from test_framework import TestCase, TestResult

class MyTest(TestCase):

    def set_up(self):
        pass
        #print('set_up')

    def tear_down(self):
        pass
        #print('tear_down')

    def test_a(self):
        pass
        #print('test_a')

    def test_b(self):
        pass
        #print('test_b')

    def test_c(self):
        pass
        #print('test_c')



result = TestResult()

test = MyTest('test_a')
test.run(result)

test = MyTest('test_b')
test.run(result)

test = MyTest('test_c')
test.run(result)

print(result.summary())