#!/usr/bin/python3

# File: test_bracket.py
# Author: Jonathan Belden
# Description: Unit tests for `bracket.py`


import os
import pytest
from bracket import bracket
from bracket import __version__


@pytest.fixture()
def source_code_file():
    proj_dir = os.path.abspath("</project/dir")
    return os.path.join(proj_dir, "<source_file>")



def test_version():
    assert __version__ == '0.1.0'


def test_0_validate_file(source_code_file):
    assert os.path.isfile(bracket.is_valid(source_code_file))


def test_1_check_angle_brackets(source_code_file):
    assert bracket.analyze(source_code_file, "angle", save_profile="output") % 2 == 0


def test_2_check_curly_brackets(source_code_file):
    assert bracket.analyze(source_code_file, "curly", save_profile="output") % 2 == 0


def test_3_check_round_brackets(source_code_file):
    assert bracket.analyze(source_code_file, "round", save_profile="output") % 2 == 0


def test_4_check_square_brackets(source_code_file):
    assert bracket.analyze(source_code_file, "square", save_profile="output") % 2 == 0


def test_5_check_single_quotes(source_code_file):
    assert bracket.analyze(source_code_file, "single", save_profile="output") % 2 == 0


def test_6_check_double_quotes(source_code_file):
    assert bracket.analyze(source_code_file, "double", save_profile="output") % 2 == 0