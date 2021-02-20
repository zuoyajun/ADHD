# -*- encoding: utf-8 -*-
# pytest命令配置文件
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="deeptables",
                     help="one of: deeptables, gbm")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")
