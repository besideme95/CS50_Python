def main():
    time = input("Enter the time:")
    time = convert(time)
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
        time = time
    elif time >=12.00 and time <= 13.00:
        print("Lunch time")
        time = time
    elif time>= 18.00 and time<= 19.00:
        print("Dinner time")
        time = time
    else:
        print("")
#if a = this then print breakfast and etc


def convert(time):
    hours,minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    time = hours + minutes
    return time



if __name__ == "__main__":
    main()

