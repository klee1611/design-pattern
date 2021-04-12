class ProductInterface():
    def get_product_name(self):
        raise RuntimeError(
            f'Virtaul product method. Should not be called directly'
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


class SimpleFactory():
    def gen_product(self, choice=None):
        return {
            'A': ConcreteProductA(),
            'B': ConcreteProductB()
        }.get(choice, None)
