from huffmanTree import (node, huffmanTree)
from letterCount import letterCounter


def main():
    letterList = letterCounter('test.txt')
    nodeList = []

    for i in range(len(letterList)):
        if i == 0:
            nodeList.append(node(chr(9), letterList[i]))
        elif i == 1:
            nodeList.append(node(chr(10), letterList[i]))
        else:
            nodeList.append(node(chr(i + 30), letterList[i]))


if __name__ == '__main__':
    main()
