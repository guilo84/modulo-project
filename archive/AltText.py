class TriNum:
    def __init__(self, value):
        if value % 3 !=0:
            raise ValueError("The number is not divisible by three")
        self.value = value

class PostTriNum:
    def __init__(self, value):
        if value % 3 + 1 !=0:
            raise ValueError("The number is not divisible by three")
        self.value = value

class PreTriNum:
    def __init__(self, value):
        if value % 3 + 2 !=0:
            raise ValueError("The number is not divisible by three")
        self.value = value
