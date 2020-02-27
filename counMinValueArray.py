import collections

numbers = [0, 0, 0, 0.55, 0, 8]

x = collections.Counter(numbers)

def mini(array):
    mini = 99999
    for i in array:
        mini = min(mini, i)
    return mini

minimo = mini(x)

def solution(array):
    count = 0
    for i in numbers:
        if i == minimo:
            count += 1
    return count

print("solucion: ", solution(numbers))
print("minimo ", mini(x))

