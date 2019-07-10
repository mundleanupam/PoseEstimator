import allure
import pytest
from PoseEstimate.PoseEstimator import PoseEstimate
from PoseEstimateTests.conftest import data_provider


data = data_provider()


@allure.title("Parameterized Test of PoseEstimate.estimate")
@pytest.mark.parametrize('data', data)
def test_estimate(data):

    # Initialize the parameterized data
    current_time = data[0]
    steering_angle = data[1]
    encoder_ticks = data[2]
    angular_velocity = data[3]
    last_time = data[7]

    x = data[4]
    y = data[5]
    th = data[6]

    output = PoseEstimate.estimate(float(current_time),
                                   float(steering_angle),
                                   int(encoder_ticks),
                                   float(angular_velocity),
                                   float(last_time))
    compare_results(x, output[0], y, output[1], th, output[2])


@allure.step
def compare_results(actual_x, expected_x, actual_y, expected_y, actual_th, expected_th):
    assert float(actual_x) == float(expected_x)
    assert float(actual_y) == float(expected_y)
    assert float(actual_th) == float(expected_th)
