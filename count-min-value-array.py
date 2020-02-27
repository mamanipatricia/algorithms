import collections

numbers = [0,0,0,0.55,0]

def findUniq(numbers):
    x = collections.Counter(numbers)
    print(x)
    print(min(x))
    mini = 99999
    count = 0

    minimo = min(mini, x[count])
    for count in x:
        print("--",x)
        print('minimoo', minimo)
        if x[count] == minimo:
            print(count)

findUniq(numbers)

