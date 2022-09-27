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
    num = 0
    while True:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        print(f"---------------Loop Number: {num}------------------")
        path = "/Users/brandon/Downloads"
        print(f"deleted text{deleteTxt(path)}")
        print(f"deleted png {deletePng(path)}")
        print(f"deleted jpg {deleteJpg(path)}")
        print(f"deleted jpeg{deleteJpeg(path)}")
        print(f'deleted Brackets {deleteBrackets(path)}')
        print(f'deleted Parentheses {deleteParentheses(path)}')
        sleep(5)
        num += 1


if __name__ == "__main__":
    main()

