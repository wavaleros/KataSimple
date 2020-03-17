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
                if minimo == -1 or int(i) < minimo:
                    minimo = int(i)

        result[0] = length
        result[1] = int(minimo)
        return result

if __name__ == '__main__':
    print()
