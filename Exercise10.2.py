class Time:
    def __init__(self ,h ,m, s):
        self.h = h
        self.m = m
        self.s = s
    def show(self):
        print(f"{self.h}:{self.m}:{self.s}")

    def from_s(self, sec):
        self.h = sec // 3600
        sec %= 3600
        self.m = sec // 60
        self.s = sec % 60
    
    def to_sec(self):
        return (self.h * 3600) + (self.m * 60) + (self.s)
    
while True:
    user_choice = input("Enter yes = start or no = Exit: ")
    if user_choice == "yes":
        operation = int(input("Enter 1= seconds to time or 2= time to seconds\n"))
        if operation == 1:
            seconds = int(input("Enter the number of seconds: "))
            t = Time(None, None, None)
            t.from_seconds(seconds)
            print("The time is:")
            t.show()
        elif operation == 2:
            hour = int(input("Enter hours: "))
            minute = int(input("Enter minutes: "))
            second = int(input("Enter seconds: "))
            t = Time(hour, minute, second)
            print("The number of seconds is:")
            print(t.to_seconds())
        else:
            print("Error. try again.")
    elif user_choice == "no":
        break
    else:
        print("Error. try again.")
