from time import sleep

from functions.functions import (
    deleteBrackets,
    deleteJpeg,
    deleteJpg,
    deleteParentheses,
    deletePng,
    deleteTxt,
)


def main():
    while True:
        path = "/Users/brandon/Downloads"
        print(f"deleted text{deleteTxt(path)}")
        print(f"deleted png {deletePng(path)}")
        print(f"deleted jpg {deleteJpg(path)}")
        print(f"deleted jpeg{deleteJpeg(path)}")
        print(deleteBrackets(path))
        print(deleteParentheses(path))
        sleep(5)
        print("---------------------------------")


if __name__ == "__main__":
    main()

