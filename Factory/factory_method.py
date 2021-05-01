class ProductInterface():
    def get_product_name(self):
        raise RuntimeError(
            'Virtaul product method. Should not be called directly'
        )


class ConcreteProductA(ProductInterface):
    def get_product_name(self):
        name = type(self).__name__
        print(f'name: {name}')
        return name


class ConcreteProductB(ProductInterface):
    def get_product_name(self):
        name = type(self).__name__
        print(f'name: {name}')
        return name


class FactoryInterface():
    def gen_product(self):
        raise RuntimeError(
            'Virtual factory method. Should not be called directly'
        )


class ProductAFactory(FactoryInterface):
    def gen_product(self):
        print('Generate product A')
        return ConcreteProductA()


class ProductBFactory(FactoryInterface):
    def gen_product(self):
        print('Generate product B')
        return ConcreteProductB()
