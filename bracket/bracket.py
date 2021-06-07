#!.venv/bin/python


# File: bracket.py
# Author: Jonathan Belden
# Description: A small utility to check for the correct
#              amount of brackets (and possibly other
#              formatting irregularities)


import os


def is_valid(input_file):
    return os.path.isfile(input_file)


def count_brackets(input_file, input_bracket, save_profile=False) -> int:
    bracket_types = {"curly": ["{", "}"],
                     "round": ["(", ")"],
                     "square": ["[", "]"]}

    with open(input_file, "r") as file:
        content = file.readlines()

    open_bracket = bracket_types[input_bracket][0]
    close_bracket = bracket_types[input_bracket][1]
    bracket_profile = {open_bracket: 0, close_bracket: 0, "lines": ""}
    if input_bracket == "curly":
        for i, line in enumerate(content):
            if line.strip().startswith("#"):
                continue
            elif open_bracket in line:
                bracket_profile["lines"] += f"{i+1} |  {line.replace(' ', '.')}"
                bracket_profile[open_bracket] += 1
            elif close_bracket in line:
                bracket_profile["lines"] += f"{i+1} |  {line.replace(' ', '.')}"
                bracket_profile[close_bracket] += 1
    else:
        for i, line in enumerate(content):
            if line.strip().startswith("#"):
                continue
            elif open_bracket in line or close_bracket in line:
                open_count = line.count(open_bracket)
                close_count = line.count(close_bracket)
                bracket_profile[open_bracket] += open_count
                bracket_profile[close_bracket] += close_count
                bracket_profile["lines"] += f"{i+1} [{open_count}:{close_count}] |  {line}"

    bracket_count = bracket_profile[open_bracket] + bracket_profile[close_bracket]
    output = ""
    if not bracket_count % 2 == 0:
        output += f"Total Bracket Count: {bracket_count}\n"
        output += f"\t'{open_bracket}': {bracket_profile[open_bracket]}\n"
        output += f"\t'{close_bracket}': {bracket_profile[close_bracket]}\n\n"
        output += bracket_profile["lines"]
        print(output)

    if save_profile:
        if not os.path.isdir(save_profile):
            os.mkdir(save_profile)
        
        file_name = os.path.join(save_profile, f"{os.path.basename(input_file)}_{input_bracket}_bracket_profile.txt")
        with open(file_name, "w") as file:
            file.write(output)

    return bracket_count