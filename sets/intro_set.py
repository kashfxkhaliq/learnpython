def average(array):
    var = set(array)
    avg = sum(var) / len(var)
    return avg

if __name__ == '__main__':
    n = int(input("Enter The Number :: "))
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)