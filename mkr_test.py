import pytest
from mkr1_nikitin import read_population_data, calculate_population_change

@pytest.fixture
def sample_population_data():
    data = {
        "Ukraine": [(1960, 42), (2000, 49), (2022, 38)],
        "Britania": [(1960, 52), (2000, 58), (2022, 66)]
    }
    return data

def test_read_population_data(sample_population_data):
    population_data = read_population_data("population.txt")
    assert population_data == sample_population_data

@pytest.mark.parametrize("input_data, expected_output", [
    ({"Ukraine": [(1960, 42), (2000, 49), (2022, 38)]}, [("Ukraine", 2000, '+'), ("Ukraine", 2022, '-')]),
    ({"Britania": [(1960, 52), (2000, 58), (2022, 66)]}, [("Britania", 2000, '+'), ("Britania", 2022, '+')])
])
def test_calculate_population_change(input_data, expected_output):
    changes = calculate_population_change(input_data)
    assert changes == expected_output
