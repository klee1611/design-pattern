class Singleton():
    _single = None

    def __new__(cls, *args, **kwargs):
        if None is cls._single:
            cls._single = super().__new__(cls)
        return cls._single

    def __init__(self, x, y):
        self.x = x
        self.y = y
