def hours_to_minutes(hours):
    return hours * 60

def main():
    hours = int(input("Enter the Number of hours :: "))
    minutes = hours_to_minutes(hours)
    print("Total minutes is = ", minutes)

if __name__ == "__main__":
    main()