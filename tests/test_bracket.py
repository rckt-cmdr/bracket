#!/usr/bin/python3

# File: test_bracket.py
# Author: Jonathan Belden
# Description: Unit tests for `bracket.py`


import os
import pytest
from bracket import bracket
from bracket import __version__


@pytest.fixture()
def afsim_file():
    proj_dir = os.path.abspath("/mnt/d/ws/afsim/abad-ccm")
    return os.path.join(proj_dir, "trbec/processors/behaviors/pursue_tracks_set_dist.txt")



def test_version():
    assert __version__ == '0.1.0'


def test_0_validate_file(afsim_file):
    assert os.path.isfile(bracket.is_valid(afsim_file))


def test_1_check_curly_brackets(afsim_file):
    brackets = ["curly", "round", "square"]
    for item in brackets:
        assert bracket.count_brackets(afsim_file, item, save_profile="output") % 2 == 0