import argparse

def single_letter(value):
    if len(value) != 1 or not value.isalpha():
        raise argparse.ArgumentTypeError(f"{value} is not a single letter A-Z")
    return value.upper()

def contest_id(value):
    # TODO: Check the validity of the contestId
    value = int(value)
    if value < 0:
        raise argparse.ArgumentError(f"{value} is not a vaild contest id")
    return value

def problems_count(value):
    value = int(value)
    if value > 26 or value < 1:
        raise argparse.ArgumentError(message=f"{value} is not a vaild number of problems")
    return value
