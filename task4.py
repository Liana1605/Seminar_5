#Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой должен отгадать. 

def qiuck_sort(array):
    if len(array) <=1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return qiuck_sort(less) + [pivot] + qiuck_sort(greater)

print(qiuck_sort([15,5,2]))