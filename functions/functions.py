import os
import re


def deleteTxt(path) -> list:
    deleted = []
    for file in os.listdir(path):
        if file.endswith(".txt"):
            os.remove(os.path.join(path, file))
            deleted.append(file)
    return deleted


def deletePng(path) -> list:
    deleted = []
    for file in os.listdir(path):
        if file.endswith(".png"):
            os.remove(os.path.join(path, file))
            deleted.append(file)
    return deleted


def deleteJpg(path) -> list:
    deleted = []
    for file in os.listdir(path):
        if file.endswith(".jpg"):
            os.remove(os.path.join(path, file))
            deleted.append(file)
    return deleted


def deleteJpeg(path) -> list:
    deleted = []
    for file in os.listdir(path):
        if file.endswith(".jpeg"):
            os.remove(os.path.join(path, file))
            deleted.append(file)
    return deleted


def deleteBrackets(path) -> list:
    # rename files removing the text in brackets using regex
    # ex: [www.Crunchyr0ll.com] One Pi3ce - 001 [1080p].mkv
    #     One Pi3ce - 001.mkv
    renamed = []
    for file in os.listdir(path):
        newFile = re.sub(r"\[.*?\]", "", file)
        newFile = newFile.strip()
        if newFile != file:
            renamed.append(newFile)
            os.rename(os.path.join(path, file), os.path.join(path, newFile))
    return renamed


def deleteParentheses(path) -> list:
    # rename files removing the text in parentheses using regex
    # ex: One Pi3ce - 001 (1080p).mkv
    #     One Pi3ce - 001.mkv
    renamed = []
    for file in os.listdir(path):
        newFile = re.sub(r"\(.*?\)", "", file)
        newFile = newFile.strip()
        if newFile != file:
            renamed.append(newFile)
            os.rename(os.path.join(path, file), os.path.join(path, newFile))
    return renamed

