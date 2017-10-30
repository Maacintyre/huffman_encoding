class node:
    recursive_print = False

    def __init__(self, character='', frequency=0):
        self.left = None
        self.right = None
        self.head = None
        self.character = character
        self.frequency = frequency

    def __str__(self):

        character = node.usefull_char(self.character)
        output = 'Character: {} Frequency: {}'.format(character,
                                                      self.frequency)
        return output

    def full_print(self, depth=0):
        output = '{}{}'.format(str(self), '\n')
        depth += 1
        if self.left is not None:
            output = '{}{}'.format(output, '\t' * depth)
            output = '{}{}'.format(output, node.full_print(self.left,
                                                           depth))
        else:
            output = '{}{}'.format(output, '\t' * depth)
            output = '{}{}'.format(output, '-' * 10)

        output = '{}{}'.format(output, '\n')

        if self.right is not None:
            output = '{}{}'.format(output, '\t' * depth)
            output = '{}{}'.format(output, node.full_print(self.right,
                                                           depth))
        else:
            output = '{}{}'.format(output, '\t' * depth)
            output = '{}{}'.format(output, '-' * 10)

        return output

    def addLeft(self, pNode):
        if self.left is None:
            self.left = pNode
            self.frequency += self.left.frequency
            self.head = self
            return True
        else:
            return False

    def addRight(self, pNode):
        if self.right is None:
            self.right = pNode
            self.frequency += self.right.frequency
            self.head = self
            return True
        else:
            return False

    @staticmethod
    def usefull_char(char):
        if char == '\t':
            character = 'Tab'
        elif char == '\n':
            character = 'Nl'
        elif char == ' ':
            character = 'Space'
        elif char == '':
            character = 'NULL'
        else:
            character = char
        return character


class huffmanTree:

    def __init__(self):
        self.head = None
        self.currentNode = None

    def left(self):
        if self.currentNode.left is not None:
            self.currentNode = self.currentNode.left
            return True
        else:
            return False

    def right(self):
        if self.currentNode.right is not None:
            self.currentNode = self.currentNode.right
            return True
        else:
            return False

    def up(self):
        if self.currentNode.head is not None:
            self.currentNode = self.currentNode.head
            return True
        else:
            return False

    def head(self):
        if self.head is not None:
            self.currentNode = self.head
            return True
        else:
            return False


def sortNodes(nodeList):

    for i in range(len(nodeList) - 1, 0, -1):
        for j in range(i):
            if nodeList[j].frequency > nodeList[j + 1].frequency:
                tempNode = nodeList[j + 1]
                nodeList[j + 1] = nodeList[j]
                nodeList[j] = tempNode
    return nodeList


def clip_blank_Nodes(nodeList):
    return_List = []
    for i in nodeList:
        if i.frequency > 0:
            return_List.append(i)
    return return_List


def encode(node, dict={}, code=''):
    if node.character is '':
        if node.left is not None:
            dict = encode(node.left, dict, '{}1'.format(code))
        if node.right is not None:
            dict = encode(node.right, dict, '{}0'.format(code))
    else:
        dict[node.character] = code
    return dict


def main():
    testNode1 = node()
    testNode1.right = node()
    testNode1.right.count = 1
    print 'Output of test node 1: {}'.format(testNode1.right.count)

    testNodeKeep = node()
    testNodeForget = node()
    testNodeForget.count = 55
    testNodeKeep.right = testNodeForget
    print ('Output of test node keep before forget: {}'.format(
        testNodeKeep.right.count))
    testNodeForget = None
    try:
        print 'Output of test node forget: {}'.format(
            testNodeForget.count)
    except AttributeError:
        print 'Test Node Forget does not have count'
    try:
        print 'Output of test node keep after forget: {}'.format(
            testNodeKeep.right.count)
    except AttributeError:
        print 'Test Node Keep has lost it\'s value'

    testNodeKeep = None
    testNodeForget = None

    testNodeKeep = node(frequency=0)
    testNodeForget = node(frequency=5)
    testNodeKeep.addRight(testNodeForget)

    node.recursive_print = True
    print str(testNodeKeep)


if __name__ == '__main__':
    main()
