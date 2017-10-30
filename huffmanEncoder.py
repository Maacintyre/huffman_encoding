from huffmanTree import *
from letterCount import letterCounter


def writeCode(fileName, codeDict):
    with open(fileName, 'w') as file:
        limit = len(codeDict)
        i = 0
        for key, value in codeDict.iteritems():
            file.write('{}{}'.format(key, value))
            if i < limit - 1:
                file.write('\n\t')
            i += 1
        file.write('\n')


def readCode(fileName):
    with open(fileName, 'r') as file:
        codeDict = {}
        terminated = False
        key = ''
        code = ''
        state = 0
        char_buffer = file.read(1)
        while not terminated:
            char = node.usefull_char(char_buffer)
            # print 'Current Char: {} Current State: {}'.format(char, state)
            if state == 0:
                key = char_buffer
                char_buffer = file.read(1)
                state = 1
            elif state == 1:
                code += char_buffer
                char_buffer = file.read(1)
                if char_buffer == '\n':
                    state = 2
                else:
                    state = 1
            elif state == 2:
                # print 'Key: {} Code: {}'.format(key, code)
                codeDict[key] = code
                code = ''
                char_buffer = file.read(1)
                if char_buffer == '\t':
                    state = 0
                    char_buffer = file.read(1)
                else:
                    terminated = True

        return codeDict


def string_bin_to_norm_string(bin_string):
    byte = 0
    text = ''
    state = 7
    for bit in bin_string:
        if state == 7 and bit == '1':
            byte += 128
        elif state == 6 and bit == '1':
            byte += 64
        elif state == 5 and bit == '1':
            byte += 32
        elif state == 4 and bit == '1':
            byte += 16
        elif state == 3 and bit == '1':
            byte += 8
        elif state == 2 and bit == '1':
            byte += 4
        elif state == 1 and bit == '1':
            byte += 2
        elif state == 0 and bit == '1':
            byte += 1

        if state == 0:
            text = '{}{}'.format(text, chr(byte))
            state = 7
        else:
            state -= 1
    return text


def compress(fileName, codeDict):
    with open(fileName, 'r') as file:
        char_buffer = file.read(1)
        while char_buffer != '':
            compressed_text = compressed_text + codeDict[char_buffer]
    padding = 8 - (len(compressed_text) % 8)
    if padding != 8:
        '{}{}'.format(compressed_text, 0 * padding)
    compressed_text = string_bin_to_norm_string(compressed_text)
    return compressed_text


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

    # tempNodeList = []
    # while tree still has hanging branches
    while len(nodeList) > 1:
        j = 0
        while j < len(nodeList) - 1:
            newNode = node()
            newNode.addLeft(nodeList[j])
            nodeList.pop(j)
            newNode.addRight(nodeList[j])
            nodeList[j] = newNode
            newNode = None
            j += 1

    # node.recursive_print = True
    # print nodeList[0].full_print()
    # print encode(nodeList[0])
    dict1 = encode(nodeList[0])

    # print dict1
    writeCode('comp.txt', dict1)

    dict2 = readCode('comp.txt')

    # print dict2
    # print string_bin_to_norm_string('00111111')


if __name__ == '__main__':
    main()
