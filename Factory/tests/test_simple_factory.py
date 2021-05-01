from ..simple_factory import SimpleFactory

class TestSimpleFactory():

    def test_simple_factory(self):
        simple_fac = SimpleFactory()

        product_1 = simple_fac.gen_product('A')
        product_2 = simple_fac.gen_product('B')

        assert 'ConcreteProductA' == product_1.get_product_name()
        assert 'ConcreteProductB' == product_2.get_product_name()
