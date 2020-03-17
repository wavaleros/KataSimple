class NumberListStatistics:

    def __init__(self):
        pass

    def processString(self, input_list):
        length = 0
        minimum = -1
        result = [length, minimum]
        for i in input_list.split(','):
            if i != '':
                j = int(i)
                length = length + 1
                if minimum == -1 or j < minimum:
                    minimum = j

        result[0] = length
        result[1] = minimum
        return result


if __name__ == '__main__':
    print()
