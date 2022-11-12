import argparse
import shutil
import os


def entrypoint():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to copy example file to.")
    args = parser.parse_args()

    dir_path = os.path.dirname(os.path.realpath(__file__))

    if os.path.isdir(args.path):
        dst = os.path.join(args.path, "dumbrute_example.py")
    else:
        dst = args.path

    shutil.copyfile(
        src=f"{dir_path}/example.py",
        dst=dst
    )
