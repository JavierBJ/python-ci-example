import model


class TestModel:

    def test_is_probability(self):
        assert 0 <= model.evaluate_model() <= 1

    def test_is_float(self):
        assert isinstance(model.evaluate_model(), float)
