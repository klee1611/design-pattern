from design_pattern.src.singleton import Singleton


class TestSingleton():

    def test_singleton(self):
        singleton_1 = Singleton(1, 2)
        singleton_2 = Singleton(3, 4)

        assert id(singleton_1) == id(singleton_2)

        assert singleton_1.x == singleton_2.x
        print(f'singleton_1.x: {singleton_1.x}, singleton_2.x: {singleton_2.x}')

        assert singleton_1.y == singleton_2.y
        print(f'singleton_1.y: {singleton_1.y}, singleton_2.y: {singleton_2.y}')
