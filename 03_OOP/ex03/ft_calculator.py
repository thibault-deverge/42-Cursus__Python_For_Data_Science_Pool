class calculator:
    '''Simple calculator class'''

    def __init__(self, results):
        '''Initialize calculator with number for further operations'''
        self.results = results

    def __add__(self, object) -> None:
        '''Add all items from self.result with the arguments'''
        self.results = [item + object for item in self.results]
        print(self.results)

    def __mul__(self, object) -> None:
        '''Multiply all items from self.result with the arguments'''
        self.results = [item * object for item in self.results]
        print(self.results)

    def __sub__(self, object) -> None:
        '''Substract the argument to all items from self.result'''
        self.results = [item - object for item in self.results]
        print(self.results)

    def __truediv__(self, object) -> None:
        '''Divide all items from self.result with the arguments'''
        if object == 0:
            print('Division by 0 is not possible')
            return float('nan')
        else:
            self.results = [item / object for item in self.results]
            print(self.results)
