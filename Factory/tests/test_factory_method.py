from ..factory_method import ProductAFactory, ProductBFactory


class TestFactoryMethod():

    def test_factory_method(self):
        factory_a = ProductAFactory()
        factory_b = ProductBFactory()

        product_a_name = factory_a.get_product_name()
        product_b_name = factory_b.get_product_name()

        assert 'ConcreteProductA' == product_a_name
        assert 'ConcreteProductB' == product_b_name
