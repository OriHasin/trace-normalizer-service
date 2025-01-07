import pytest
import yaml
import os
from main import normalize_trace


def load_test_cases(dir_path):
    print(os.getcwd())
    test_cases = []

    for file_name in os.listdir(dir_path):

        if file_name.endswith(".yaml"):  # process only .yaml files
            with open(os.path.join(dir_path, file_name)) as test_file:

                cases = yaml.safe_load(test_file)  # load entire suites' test cases into memory
                for case in cases:

                    if "expected" in case:  # Valid test cases
                        test_cases.append((case["source"], case["input"], case["expected"]))
                    elif "expected_error" in case:  # Invalid test cases
                        test_cases.append((case["source"], case["input"], case["expected_error"]))

    print(test_cases)

    return test_cases


@pytest.mark.parametrize("source, input_data, expected", load_test_cases("./tests/valid"))
def test_valid_normalization(source, input_data, expected):
    normalized_trace = normalize_trace(source, input_data)
    assert normalized_trace.model_dump() == expected


@pytest.mark.parametrize("source, input_data, expected_error", load_test_cases("./tests/invalid"))
def test_invalid_normalization(source, input_data, expected_error):
    with pytest.raises(Exception, match=expected_error):
        normalize_trace(source, input_data)
