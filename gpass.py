#!/usr/bin/env python3

import itertools
import argparse
import os
from datetime import datetime

try:
    from tqdm import tqdm
except ImportError:
    raise ImportError("module tqdm is required.")

def v_path(f_path, w=False):
    """
    Validate if a given path exists and is accessible.
    """
    if w:
        try:
            with open(f_path, "w"):
                pass
        except Exception as e:
            raise ValueError(f"Error writing to file '{f_path}': {e}")
    else:
        if not os.path.isfile(f_path):
            raise FileNotFoundError(f"File '{f_path}' does not exist or is not a file.")
    return f_path


def g_passw(lst, out, _min, _max):
    """
    Generate permutations of given elements within the specified length range
    and write them to the output file.
    """
    t_passw = 0
    with open(out, "w") as out_f:
        if len(lst) >= 11:
            print("[*] This process may take a while...")
        print(f"[*] Started at {datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}")

        for _len in range(_min, _max + 1):
            for cmb in tqdm(itertools.permutations(lst, _len),
                                    desc=f"Generating passwords of length {_len}",
                                    leave=False):
                passw = ''.join(cmb)
                if _min <= len(passw) <= _max:
                    out_f.write(passw + '\n')
                    t_passw += 1

        print(f"[*] Ended at {datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}")

    return t_passw


def main():
    parser = argparse.ArgumentParser(
        description="Generate a dictionary of passwords based on input words."
    )
    parser.add_argument("--min", type=int, required=True, help="Minimum password length.")
    parser.add_argument("--max", type=int, required=True, help="Maximum password length.")
    parser.add_argument("--in", dest="input_file", type=str, required=True,
                        help="Path to the input file containing words (one per line).")
    parser.add_argument("--out", dest="output_file", type=str, required=True,
                        help="Path to the output file where passwords will be saved.")

    args = parser.parse_args()

    # Validate file paths
    in_path = v_path(args.input_file)
    out_path = v_path(args.output_file, w=True)

    # Validate length constraints
    if args.max < args.min:
        raise ValueError("Maximum length cannot be smaller than minimum length.")

    # Load input words
    with open(in_path, "r") as file:
        words = file.read().strip().splitlines()

    if not words:
        raise ValueError(f"Input file '{in_path}' is empty.")

    # Generate passwords
    total = g_passw(words, out_path, args.min, args.max)
    print(f"[*] Success! {total} passwords saved in '{out_path}'.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
