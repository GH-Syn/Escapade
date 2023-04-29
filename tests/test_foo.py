import sys, os, pytest
sys.path.insert(0, os.getcwd())
from game import main

def test_foo():
    assert main.foo() == "bar"
