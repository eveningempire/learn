class number:
    def __init__(self, value):
        self.value = value

    def is_even(self):
        return self.value % 2 == 0

    def is_odd(self):
        return self.value % 2 != 0

    def __str__(self):
        return str(self.value)