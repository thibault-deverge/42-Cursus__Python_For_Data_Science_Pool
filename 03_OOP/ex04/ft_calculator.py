class calculator:
    '''Class for performing vector operations'''

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        '''Calculate and print the dot product of two vectors'''
        result = []
        for i in range(len(V1)):
            result.append(V1[i] * V2[i])
        result = sum(result)
        print(f"Dot product is : {result}")

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        '''Calculate and print the addition of two vectors'''
        result = []
        for i in range(len(V1)):
            result.append(float(V1[i] + V2[i]))
        print(f"Add Vector is : {result}")

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        '''Calculate and print the substraction of two vectors'''
        result = []
        for i in range(len(V1)):
            result.append(float(V1[i] - V2[i]))
        print(f"Add Vector is : {result}")
