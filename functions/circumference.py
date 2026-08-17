def circle_circumference(radius):
    return 2 * 3.1416 * radius

def main():
    radius = float(input("Enter the Radius of the Circle: "))
    result = circle_circumference(radius)
    print("Circumference of the circle is : ", result)

if __name__ == "__main__":
    main()