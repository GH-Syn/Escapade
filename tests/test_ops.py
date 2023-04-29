import os


def test_path_exists():
    assert os.path.exists(os.path.join('devops', 'coverage.sh')) == True
