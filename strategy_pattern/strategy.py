import types


class StrategyExample:
    def __init__(self, func=None):
        self.name = 'Strategy Example 0'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)


def execute_example1(self):
    print('Executing example 1')


def execute_example2(self):
    print('Executing example 2')

if __name__ == '__main__':
    strategy = StrategyExample()
    strategy.execute()
    strategy1 = StrategyExample(execute_example1)
    strategy1.execute()
    strategy2 = StrategyExample(execute_example2)
    strategy2.execute()
