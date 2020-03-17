class NumberListStatistics:

    def __init__(self):
        pass

    def processString(self, input_list):
        length = 0
        minimum = -1
        maximum = -1
        result = [length, minimum, maximum]
        for i in input_list.split(','):
            if i != '':
                j = int(i)
                length = length + 1
                if minimum == -1 or j < minimum:
                    minimum = j
                if maximum < j:
                    maximum = j

        result[0] = length
        result[1] = minimum
        result[2] = maximum
        return result


if __name__ == '__main__':
    print()
