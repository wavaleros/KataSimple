class NumberListStatistics:
    list_legth = 0

    def __init__(self):
        self.list_legth = 0

    def processString(self, input_list): 
        for i in input_list.split(','):
            if i != '':
                self.list_legth = self.list_legth+1

if __name__ == '__main__':
    print()
