def greater(a, b):
    if a > b:
        return a
    else:
        return b
    
def main():
    x = int(input("Enter The Number :: "))
    y = int(input("Enter The Number :: "))
    
    z = greater(x, y)
    print("The Greater Number is :: ", z)
    
if __name__ == "__main__":
    main()