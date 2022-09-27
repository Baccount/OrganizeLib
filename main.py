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
    path = input("Path: ")
    images = input("Delete jpeg, jpg, png? (y/n): ")
    txt = input("Delete txt's? (y/n): ")
    bp = input("Delete brackets and parentheses? (y/n): ")
    
    if images.lower() == "y":
        deleteJpeg(path)
        deleteJpg(path)
        deletePng(path)
    if txt.lower() == "y":
        deleteTxt(path)
    if bp.lower() == "y":
        deleteBrackets(path)
        deleteParentheses(path)


if __name__ == "__main__":
    main()
