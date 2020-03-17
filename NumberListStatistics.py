class NumberListStatistics:
    number_list = []

    def __init__(self):
        pass

    def get_list_size(self):
        return len(self.number_list)

    def processString(self, input_list):
        self.number_list = input_list.split(',')


if __name__ == '__main__':
    print()
