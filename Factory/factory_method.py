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


class ProductFactory():
    def gen_product(self):
        raise RuntimeError(
            'Virtual factory method. Should not be called directly'
        )

    def get_product_name(self):
        product = self.gen_product()
        product_name = product.get_product_name()
        return product_name


class ProductAFactory(ProductFactory):
    def gen_product(self):
        print('Generate product A')
        return ConcreteProductA()


class ProductBFactory(ProductFactory):
    def gen_product(self):
        print('Generate product B')
        return ConcreteProductB()
