import csv
from datetime import datetime
from os import path


# Restaurant class
class Restaurant:

    # Constructor of class
    def __init__(self, name, date_time):
        self.name = name
        self.date_time = date_time
        self.timing = {}

    # function to modify dat and set timing of restaurant
    def do_changes(self):
        day = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

        date_time_split = self.date_time.split('/')

        for index in range(len(date_time_split)):
            date_time_split[index] = date_time_split[index].lstrip()
            date_time_split[index] = date_time_split[index].replace(" - ", "-")
            date_time_split[index] = date_time_split[index].replace(" am", "am")
            date_time_split[index] = date_time_split[index].replace(" pm", "pm")
            date_time_split[index] = date_time_split[index].replace(", ", ",")
            date_time_split[index] = date_time_split[index].rstrip()
            date_time_split[index] = date_time_split[index].replace(" ", ",")
            date_time_split_once = date_time_split[index].split(',')

            time = date_time_split_once[len(date_time_split_once)-1]

            for index_t in range(len(date_time_split_once)-1):
                if "-" in date_time_split_once[index_t]:
                    date_time_split_once_day = date_time_split_once[index_t].split('-')

                    running = False

                    for index_day in day:
                        if index_day == date_time_split_once_day[0]:
                            running = True

                        if running:
                            self.timing[index_day] = time

                        if index_day == date_time_split_once_day[1]:
                            break
                else:
                    self.timing[date_time_split_once[index_t]] = time

    # function to temporary display data
    def display(self):
        print(self.name)
        # print(self.timing)

    def is_open(self, date_time_give):
        temp = date_time_give.split(" ")
        day = temp[0]
        time = temp[1]

        given_time = change_format(time)

        timing = self.timing[day]
        timing_s = timing.split("-")

        open_time = change_format(timing_s[0])
        close_time = change_format(timing_s[1])

        if open_time < close_time:
            return (given_time >= open_time) and (given_time <= close_time)
        else:
            return (given_time >= open_time) or (given_time <= close_time)


# Find open restaurants function
def find_open_restaurants (csv_file_name, search_date_time):

    # reading data from csv files
    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        # getting row from csv file
        for row in csv_reader:
            # creating restaurant class object
            res = Restaurant(row[0], row[1])
            res.do_changes()
            # res.display()
            if res.is_open(search_date_time):
                res.display()
                # print("Open\n")
                line_count += 1

        print(f'Total {line_count} restaurants available')


# Change time format
def change_format(time_p):
    if ":" in time_p:
        time_c = datetime.strptime(time_p, '%I:%M%p')
    else:
        time_c = datetime.strptime(time_p, '%I%p')
    return time_c


# Main part of file
print("Find the open restaurants :")
print("\n***Note: Please enter date in dd-MM-yyyy format and time in mm:hham/pm .***")
while True:
    date = input("Enter date : ")
    date_spl = date.split('/')
    isValidDate = True
    try:
        datetime.strptime(date, '%d-%m-%Y').date()
    except ValueError:
        isValidDate = False
    if isValidDate:
        print("Date entered successfully!")
        break
    else:
        print("Input date is not valid..")

while True:
    time = input("Enter time :")
    isValidDate = True
    try:
        datetime.strptime(time, '%I:%M%p').date()
    except ValueError:
        isValidDate = False
    if isValidDate:
        print("Time entered successfully!")
        break
    else:
        print("Input time is not valid..")

while True:
    file_name = input("Enter the file name of csv file :")
    file_name_spl = file_name.split(".")
    try:
        if file_name_spl[1] == 'csv':
            print("File name is correct!")
            if path.exists(file_name):
                print("File is exists!")
                break;
            else:
                print("File doesn\'t exists! Re-enter file name:")
        else:
            print("File is not in CSV format!")
    except IndexError:
        print("File is not in CSV format!")

date_temp = date.split("-")
date_time = datetime.strptime(date, '%d-%m-%Y').date()
day = date_time.weekday()
weekDays = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
dayS = weekDays[day]

search_day_time = dayS+" "+time
find_open_restaurants(file_name, search_day_time)
