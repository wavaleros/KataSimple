class NumberListStatistics:

    def __init__(self):
        pass

    def processString(self, input_list):
        length = 0
        minimum = -1
        maximum = -1
        average = -1.0
        sum = 0
        result = [length, minimum, maximum, average]
        for i in input_list.split(','):
            if i != '':
                j = int(i)
                length = length + 1
                if minimum == -1 or j < minimum:
                    minimum = j
                if maximum < j:
                    maximum = j
                sum = sum + j

        if length > 0:
            average = sum / length

        result[0] = length
        result[1] = minimum
        result[2] = maximum
        result[3] = average
        return result


if __name__ == '__main__':
    print()
