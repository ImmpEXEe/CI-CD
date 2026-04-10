import pytest
from main import read_data, sort_by_area, sort_by_population

@pytest.fixture
def sample_data():
    return [
        {'country': 'Країна А', 'area': 100.0, 'population': 500},
        {'country': 'Країна Б', 'area': 300.0, 'population': 100},
        {'country': 'Країна В', 'area': 200.0, 'population': 1000}
    ]

@pytest.mark.parametrize("expected_first, expected_last", [
    ('Країна Б', 'Країна А')
])
def test_sort_by_area(sample_data, expected_first, expected_last):
    result = sort_by_area(sample_data)
    assert result[0]['country'] == expected_first
    assert result[-1]['country'] == expected_last

@pytest.mark.parametrize("expected_first, expected_last", [
    ('Країна В', 'Країна Б')
])
def test_sort_by_population(sample_data, expected_first, expected_last):
    result = sort_by_population(sample_data)
    assert result[0]['country'] == expected_first
    assert result[-1]['country'] == expected_last