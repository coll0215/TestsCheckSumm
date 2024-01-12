import pytest
import re 
from src.testingdata import TESTGPSDATA
from src.testingdata import TESTIMUDATA
from src.estimator import EstimatorCS

def csres(data):
    cmd_list = data.split(",*")
    result_string = ''.join(c if c.isdigit() else ' ' for c in cmd_list[1]).split()
    result = list(map(int, result_string))
    return result[0]

@pytest.mark.parametrize(
        "cmd, result",
        [
            (TESTGPSDATA[0], csres(TESTGPSDATA[0])),
            (TESTGPSDATA[1], csres(TESTGPSDATA[1])),
            (TESTGPSDATA[2], csres(TESTGPSDATA[2])),
            (TESTGPSDATA[3], csres(TESTGPSDATA[3])),
            (TESTGPSDATA[4], csres(TESTGPSDATA[4])),
            (TESTGPSDATA[5], csres(TESTGPSDATA[5])),
            (TESTGPSDATA[6], csres(TESTGPSDATA[6])),
            (TESTGPSDATA[7], csres(TESTGPSDATA[7])),
            (TESTGPSDATA[8], csres(TESTGPSDATA[8])),
            (TESTGPSDATA[9], csres(TESTGPSDATA[9])),
            (TESTGPSDATA[10], csres(TESTGPSDATA[10])),
            (TESTGPSDATA[11], csres(TESTGPSDATA[11])),
            (TESTGPSDATA[12], csres(TESTGPSDATA[12])),
            (TESTGPSDATA[13], csres(TESTGPSDATA[13])),
            (TESTGPSDATA[14], csres(TESTGPSDATA[14])),
            (TESTGPSDATA[15], csres(TESTGPSDATA[15])),
            (TESTGPSDATA[16], csres(TESTGPSDATA[16])),
            (TESTGPSDATA[17], csres(TESTGPSDATA[17])),
        ]
        )
def test_GPS(cmd, result):
    GPS_CS = EstimatorCS()
    assert GPS_CS.get_CS(cmd) == result

@pytest.mark.parametrize(
        "cmd, result",
        [
            (TESTIMUDATA[0], csres(TESTIMUDATA[0])),
            (TESTIMUDATA[1], csres(TESTIMUDATA[1])),
            (TESTIMUDATA[2], csres(TESTIMUDATA[2])),
            (TESTIMUDATA[3], csres(TESTIMUDATA[3])),
            (TESTIMUDATA[4], csres(TESTIMUDATA[4])),
            (TESTIMUDATA[5], csres(TESTIMUDATA[5])),
            (TESTIMUDATA[6], csres(TESTIMUDATA[6])),
            (TESTIMUDATA[7], csres(TESTIMUDATA[7])),
            (TESTIMUDATA[8], csres(TESTIMUDATA[8])),
            (TESTIMUDATA[9], csres(TESTIMUDATA[9])),
            (TESTIMUDATA[10], csres(TESTIMUDATA[10])),
            (TESTIMUDATA[11], csres(TESTIMUDATA[11])),
            (TESTIMUDATA[12], csres(TESTIMUDATA[12])),
            (TESTIMUDATA[13], csres(TESTIMUDATA[13])),
            (TESTIMUDATA[14], csres(TESTIMUDATA[14])),
            (TESTIMUDATA[15], csres(TESTIMUDATA[15])),
            (TESTIMUDATA[16], csres(TESTIMUDATA[16])),
            (TESTIMUDATA[17], csres(TESTIMUDATA[17])),
        ]
        )
def test_IMU(cmd, result):
    IMU_CS = EstimatorCS()
    assert IMU_CS.get_CS(cmd) == result