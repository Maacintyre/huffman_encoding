
def letterCounter(fileName):
    letter_Frequency = [0]
    letter_Frequency = letter_Frequency * 97
    with open(fileName, 'r') as f:
        char_Buffer = f.read(1)
        while char_Buffer != "":
            index = ord(char_Buffer)
            if index == 9:  # Count the horizontal tabs
                letter_Frequency[0] += 1
            elif index == 10:  # Count the newlines
                letter_Frequency[1] += 1
            else:
                index -= 30
                letter_Frequency[index] += 1
            char_Buffer = f.read(1)
    return letter_Frequency


def main():
    print letterCounter('test.txt')


if __name__ == '__main__':
    main()
