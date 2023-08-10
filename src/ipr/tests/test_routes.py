import numpy as np
import pytest


@pytest.fixture
def generate_data_for_tests():
    return {
        "p_res": np.random.uniform(200, 300),
        "wct": np.random.uniform(0, 100),
        "pi": np.random.uniform(0.5, 3),
        "pb": np.random.uniform(50, 300),
    }


def test_calc_model_success(api_client, generate_data_for_tests):
    response = api_client.post("ipr/calc", json=generate_data_for_tests)
    assert response.status_code == 200
    result = response.json()
    assert result
    assert result["q_liq"]
    assert result["p_wf"]
