#!.venv/bin/python


# File: bracket.py
# Author: Jonathan Belden
# Description: A small utility to check for the correct
#              amount of brackets (and possibly other
#              formatting irregularities)


import bracket
import os
from icecream import ic
ic.configureOutput(includeContext=True)


def is_valid(input_file):
    return os.path.isfile(input_file)


def analyze(input_file, input_bracket, save_profile=False) -> int:
    with open(input_file, "r") as file:
        content = file.readlines()

    open_bracket = f"{input_bracket}_left"
    close_bracket = f"{input_bracket}_right"
    if input_bracket == "curly":
        ic(input_bracket)
        analysis_profile = count_curly_brackets(content)
        bracket_count = analysis_profile[open_bracket] + analysis_profile[close_bracket]
        description = "bracket"
    
    elif input_bracket == "single" or input_bracket == "double":
        analysis_profile = count_quotes(content, input_bracket)
        bracket_count = analysis_profile[f"{input_bracket}_quotes"]
        description = "quotes"
    
    else:
        analysis_profile = count_in_line_brackets(content, input_bracket)
        bracket_count = analysis_profile[open_bracket] + analysis_profile[close_bracket]
        description = "bracket"

    output = ""
    if not bracket_count % 2 == 0 or save_profile:
        output += f"Total {input_bracket} quote count: {bracket_count}\n" if input_bracket == "single" or input_bracket == "double" else f"Total {input_bracket} bracket count: {bracket_count}\n"
        try:
            output += f"\t'{open_bracket}': {analysis_profile[open_bracket]}\n"
            output += f"\t'{close_bracket}': {analysis_profile[close_bracket]}\n"
        except KeyError:
            pass
        output += f"=====================================================\n\n"
        output += analysis_profile["lines"]
        print(output)

    if save_profile:
        ic(save_profile)
        ic(output)
        if not os.path.isdir(save_profile):
            os.mkdir(save_profile)
        
        file_name = os.path.join(save_profile, f"{input_bracket}-{description}-profile_{os.path.basename(input_file)}")
        with open(file_name, "w") as file:
            file.write(output)

    return bracket_count


def count_curly_brackets(content) -> dict:
    bracket_profile = {"curly_left": 0, "curly_right": 0, "lines": ""}
    for i, line in enumerate(content):
            if line.strip().startswith("#") or line.strip().startswith("//"):
                continue
            elif "{" in line:
                bracket_profile["lines"] += f"{i+1} |  {line.replace(' ', '.')}"
                bracket_profile["curly_left"] += 1
            elif "}" in line:
                bracket_profile["lines"] += f"{i+1} |  {line.replace(' ', '.')}"
                bracket_profile["curly_right"] += 1
    return bracket_profile


def count_in_line_brackets(content, bracket_type) -> dict:
    in_line_brackets = {"angle": ["<", ">"],
                        "round": ["(", ")"],
                        "square": ["[", "]"]}
    left_bracket = in_line_brackets[bracket_type][0]
    right_bracket = in_line_brackets[bracket_type][1]
    bracket_profile = {f"{bracket_type}_left": 0, f"{bracket_type}_right": 0, "lines": ""}
    for i, line in enumerate(content):
        if line.strip().startswith("#") or line.strip().startswith("//"):
            continue
        elif left_bracket in line or right_bracket in line:
            left_count = line.count(left_bracket)
            right_count = line.count(right_bracket)
            bracket_profile[f"{bracket_type}_left"] += left_count
            bracket_profile[f"{bracket_type}_right"] += right_count

            if left_count != right_count:
                bracket_profile["lines"] += f"{i+1} [{left_count}:{right_count}]* |   {line}"
            else:
                bracket_profile["lines"] += f"{i+1} [{left_count}:{right_count}]  |   {line}"
    return bracket_profile


def count_quotes(content, input_quote) -> dict:
    quote_types = {"double": "\"", "single": "'"}
    quotes_profile = {f"{input_quote}_quotes": 0, "lines": ""}
    for i, line in enumerate(content):
        if line.strip().startswith("#") or line.strip().startswith("//"):
            continue
        elif quote_types[input_quote] in line:
            qoute_count = line.count(quote_types[input_quote])
            quotes_profile[f"{input_quote}_quotes"] += qoute_count

            if qoute_count % 2 != 0:
                quotes_profile["lines"] += f"{i+1} [{qoute_count}]* |   {line}"
            else:
                quotes_profile["lines"] += f"{i+1} [{qoute_count}]  |   {line}"
    return quotes_profile