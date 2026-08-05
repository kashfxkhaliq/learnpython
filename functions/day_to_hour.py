def days_to_hours(days):
    return days * 24

def main():
    days = int(input("Enter the Number of days: "))
    hours = days_to_hours(days)
    print("Total hours : ", hours)

if __name__ == "__main__":
    main()