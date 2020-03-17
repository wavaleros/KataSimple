class NumberListStatistics:
    
    def __init__(self):
        pass
    
    def processString(self, input_list): 
        length = 0
        minimo = -1
        result = [length, minimo]
        for i in input_list.split(','):
            if i != '':
                length = length+1

        result[0] = length
        result[1] = minimo
        return result

if __name__ == '__main__':
    print()
