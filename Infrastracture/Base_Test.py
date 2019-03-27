import pytest
from Infrastracture.WebDriverWrapper import DriverWrapper
@pytest.mark.usefixtures("driver_init")
class BaseTest:
    driver = DriverWrapper
