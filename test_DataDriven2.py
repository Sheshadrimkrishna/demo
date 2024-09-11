import openpyxl
import pytest

from Utilities import ExcelReader


@pytest.mark.parametrize("username,password",ExcelReader.get_data("ExcelFile/TutorialsNinja.xlsx","LoginTest"))
def test_login(username,password):
    print("Logged in using username: "+username+" and password" +password)



