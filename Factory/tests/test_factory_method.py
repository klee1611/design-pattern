from ..factory_method import ProductAFactory, ProductBFactory

class TestSimpleFactory():

    def test_simple_factory(self):
        factory_a = ProductAFactory()
        factory_b = ProductBFactory()

        product_a = factory_a.gen_product()
        product_b = factory_b.gen_product()

        assert 'ConcreteProductA' == product_a.get_product_name()
        assert 'ConcreteProductB' == product_b.get_product_name()
