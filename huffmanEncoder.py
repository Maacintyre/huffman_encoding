from huffmanTree import *
from letterCounter import letterCounter


# Create a new file and store the Huffman translation table at the start of
# the file

def write_trans_table(fileName, codeDict):
    with open(fileName, 'w') as file:
        limit = len(codeDict)
        i = 0
        for key, value in codeDict.iteritems():
            file.write('{},{}'.format(key, value))
            if i < limit - 1:
                file.write(',')
            i += 1
        file.write('\n')


# Read the Huffman translation table from the beggining of a file

def read_trans_table(fileName):
    huffTable = {}
    writeKey = True

    with open(fileName, 'r') as file:
        line = file.readline()

    for value in line.split(','):
        if writeKey:
            key = value
        else:
            huffTable[key] = value
        writeKey = not writeKey
    return huffTable


# Turn 8 character bin string into an 8 bit character

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
            byte = 0
        else:
            state -= 1
    return text


def compress(fileName, huff_table):
    comp_text = ''
    with open(fileName, 'r') as file:
        char_buffer = file.read(1)
        while char_buffer != '':
            comp_text = '{}{}'.format(
                comp_text,
                huff_table[node.clear_char_output(char_buffer)]
            )
            char_buffer = file.read(1)
    padding = 8 - (len(comp_text) % 8)
    if padding != 8:
        comp_text = '{}{}'.format(comp_text, '1' * padding)
    # return comp_text
    return string_bin_to_norm_string(comp_text)


def test():
    nodeList = []
    letterList = letterCounter('test.txt')

    # Create list of character nodes for processing
    for i in range(len(letterList)):
        if i == 0:  # If horizontal tabs
            nodeList.append(node(chr(9), letterList[i]))
        elif i == 1:  # If newline
            nodeList.append(node(chr(10), letterList[i]))
        else:  # All other printable characters
            nodeList.append(node(chr(i + 30), letterList[i]))

    nodeList = clip_blank_nodes(nodeList)
    nodeList = sort_nodes(nodeList)

    # Create Huffman Tree
    while len(nodeList) > 1:  # while tree still has hanging branches
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
    huff_table = nodeList[0].encode_tree()

    # print huff_table
    write_trans_table('comp.txt', huff_table)

    huff_table = read_trans_table('comp.txt')

    # print huff_table
    print compress('test.txt', huff_table)
    # print string_bin_to_norm_string('00111111')


if __name__ == '__main__':
    test()
