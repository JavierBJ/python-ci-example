# python-ci-example

[![CircleCI](https://circleci.com/gh/JavierBJ/python-ci-example.svg?style=svg&circle-token=07246fe186b625bb95b08c67c5befaf862b41bdd)](https://circleci.com/gh/JavierBJ/python-ci-example)

This is me trying a Continuous Integration setting on a toy machine learning environment. It consists of:

* Classification on the Iris dataset, both taken from scikit-learn.
* Code style checking using flake8.
* Unit testing on the classification model and code coverage, using pytest.
* Automated build of requirements, flake8 and pytest, using CircleCI hosted on a Python 3.7 docker image.
