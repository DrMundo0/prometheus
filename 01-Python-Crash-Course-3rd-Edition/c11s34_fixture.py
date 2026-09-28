# 学习夹具

import pytest
from c09s21_class import Car

# 这是Python中的注解语法，标明pytest.fixture的为夹具，夹具相当于Java中的BeforeTest
@pytest.fixture
def car_survey():
    print("What's your favorite car?")
    car_survey = Car("一汽大众", "CC", "2026")
    return car_survey

def test_1(car_survey: Car):
    assert car_survey.make is not None

def test_2(car_survey: Car):
    assert "一汽大众" == car_survey.make
