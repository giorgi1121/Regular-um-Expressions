import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #create valid format pattern
    valid_format = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)+ to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)+$", s)

    #check if input is valid else raise ValueError
    if valid_format:
        #divide input into groups and check if hours are correct, else raise ValueError
        parts = valid_format.groups()
        if int(parts[1]) > 12 or int(parts[5]) > 12:
            raise ValueError
        else:
            #if format is correct call new_format function to convert input into 24hour format
            starting = new_format(parts[1], parts[2], parts[3])
            ending = new_format(parts[5], parts[6], parts[7])
        
        return starting + " to " + ending
    
    else:
        raise ValueError


def new_format(hour, minutes, am_pm):
    # if time is PM then 12 o'clock shoudl be 12 in 24hour format, otherwise it shoudl be add 12
    if am_pm == "PM":
        if hour == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    
    # if time is AM then 12 o'clock should be 0:00 in 24hour format, otherwise it does not change 
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    
    # if minutes equals None then new_minutes should be :00, otherwise it remains unchanged
    if minutes == None:
        new_minutes = ":00"
        new_time = f"{new_hour:02}{new_minutes}"
    else:
        new_time = f"{new_hour:02}:{minutes}"

    #return new_time format
    return new_time


if __name__ == "__main__":
    main()