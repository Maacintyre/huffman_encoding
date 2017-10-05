from huffmanTree import *
from letterCount import letterCounter


def main():
    nodeList = []
    letterList = letterCounter('test.txt')

    for i in range(len(letterList)):
        if i == 0:  # If horizontal tabs
            nodeList.append(node(chr(9), letterList[i]))
        elif i == 1:  # If newline
            nodeList.append(node(chr(10), letterList[i]))
        else:  # All other printable characters
            nodeList.append(node(chr(i + 30), letterList[i]))

    nodeList = clip_blank_Nodes(nodeList)
    nodeList = sortNodes(nodeList)
    node.recursive_print = False
    for i in nodeList:
        print str(i)
    print(ord('\t'))


if __name__ == '__main__':
    main()
