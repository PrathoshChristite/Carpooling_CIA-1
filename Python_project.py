from datetime import datetime
import os

# Defines welcome message and gives a brief about the program
def welcome_message():
    print("*" * 30 + "Welcome" + "*" * 30)
    print("")
    print("1) In this application, you will have the option to take a cab from Lavasa to Pune or the other way around so that the cost of travel won't become a reason for you to have a small break from Christ")
    print("")
    print("2) All you have to do is to give some basic information about yourselves and choose a driver from n number of drivers in our database, and just like that, you will be able to book a taxi")
    print("")

# Function to gather passenger details and travel preferences
def first_page_passengers():
    try:
        # Gather passenger information
        no_of_people = int(input("Enter the number of people traveling with you (Excluding you): "))
        names = []
        contact_number = []
        gender = []

        for i in range(no_of_people + 1):
            input_names = input("Enter " + str(i + 1) + " passenger name: ")
            input_contact_number = int(input("Enter " + str(i + 1) + " passenger contact number: "))
            input_gender = input("Enter " + str(i + 1) + " passenger Gender (male, female, or others): ")

            gender.append(input_gender.lower())
            names.append(input_names)
            contact_number.append(input_contact_number)

        pick_up_location = input("Enter the pick-up location: ")
        destination = input("Enter your destination: ")

        # Choose one-way or two-way trip
        print("Enter 1 for one way")
        print("Enter 2 for two way")
        one_or_two_way = int(input("Please enter 1 or 2: "))

        if one_or_two_way == 1:
            one_or_two_way = "One way"
        elif one_or_two_way == 2:
            one_or_two_way = "Two way"
        else:
            print("Invalid input. Please pick either 1 or 2.")
            return  # Exit the function in case of error

        pick_up_time = input("Enter the time you're traveling (HH:MM format): ")
        pick_up_date = input("Enter the date you're traveling (DD-MM-YYYY format): ")

        # Error handling for time and date format
        try:
            pick_up_time_obj = datetime.strptime(pick_up_time, "%H:%M").time()
            pick_up_date_obj = datetime.strptime(pick_up_date, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid time or date format. Please enter in HH:MM and DD-MM-YYYY formats, respectively.")
            return  # Exit the function in case of error

        payment_method = input("Please enter the type of payment that will be used: ")

        # Store passenger and travel details in dictionaries
        personal_details_passenger = {"Names": names, "Contact Number": contact_number, "Gender": gender}
        travel_details_passenger = {
            "pick up location": pick_up_location,
            "destination": destination,
            "one_or_two_way": one_or_two_way,
            "pick up time": pick_up_time,
            "pick_up_date": pick_up_date,
        }
        print(personal_details_passenger)
        print(travel_details_passenger)


    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of people.")
        return  # Exit the function in case of error

    # Existing code...

    print("")
    file_path = 'driver_details.txt'

    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()

    # Display driver details
    print("Driver Details:")
    print("*" * 90)
    for i, line in enumerate(lines):
        if i == 0:
            print("headers")
            print(line)
            print("*" * 90)
        else:
            line = line.strip()
            print(f"Driver {i}:")
            print(line)
            print("*" * 90)

    # Choose a driver
    while True:
        try:
            driver_choice = int(input("Enter the number of the driver you prefer: "))
            driver_choice = driver_choice + 1
            if driver_choice < 1 or driver_choice > len(lines):
                print("Invalid driver number. Please choose a valid driver.")
            else:
                driver_choice = driver_choice - 1
                chosen_driver = lines[driver_choice].strip()
                print(f"\nYou have selected Driver {driver_choice}:\n{chosen_driver}")
                driver_details = chosen_driver.split(',')
                one_way_price = driver_details[4]
                round_trip_price = driver_details[6]
                if one_or_two_way == 1 and n == 0:
                    print("The entire fare for the trip comes to" + one_way_price)
                elif one_or_two_way == 1 and n >= 1:
                    print("The entire fare for the trip comes to" + one_way_price)
                    print("Price for each individual is " + str(int(int(one_way_price) / (no_of_people + 1))))
                elif one_or_two_way == 2 and n == 0:
                    print("The entire fare for the trip comes to" + round_trip_price)
                else:
                    print("The entire fare for the trip comes to " + round_trip_price)
                    print("Price for each individual is " + str(int(int(round_trip_price) / (no_of_people + 1))))
                break  # Exit the loop after a valid driver is chosen
        except ValueError:
            break  # Exit the loop after a valid driver is chosen
        except ValueError:
            print("Invalid input. Please enter a valid integer for the driver number.")

    print("The driver has been booked")


# Function to gather driver details
def first_page_driver(driver_details_list):
    try:
        print("Enter your details")
        print("Follow the format while entering the data")
        print("********************")
        name = input("Name: ")
        contact_no = int(input("Contact Number: "))
        car_model = input("Car Model: ")
        no_of_seats = int(input("No. of Seats (Excluding the driver): "))
        gender = input("Enter your Gender: ")
        print("Select Y if available on a particular day and N if not available on that day")
        option1 = input("Sunday (Y/N): ")
        option2 = input("Monday (Y/N): ")
        option3 = input("Tuesday (Y/N): ")
        option4 = input("Wednesday (Y/N): ")
        option5 = input("Thursday (Y/N): ")
        option6 = input("Friday (Y/N): ")
        option7 = input("Saturday (Y/N): ")
        print("")
        driver = []

        # Check the state of each checkbox and display output
        if option1.lower() == "y":
            driver.append("Sun")

        if option2.lower() == "y":
            driver.append("Mon")

        if option3.lower() == "y":
            driver.append("Tue")

        if option4.lower() == "y":
            driver.append("Wed")

        if option5.lower() == "y":
            driver.append("Thur")

        if option6.lower() == "y":
            driver.append("Fri")

        if option7.lower() == "y":
            driver.append("Sat")
        available_days = ' '.join(driver)

        print("Enter your working hours")
        time_available = input("Available time (HH:MM) to (HH:MM): ")
        print("Fill the Fare of the trip")
        price1 = input("Price One way: ")
        price2 = input("Price Two way: ")

        print("The available days are " + available_days)
        personal_details_driver = {"Name": name, "Contact Number:": contact_no, "Gender": gender}
        Date_time_price = {"Available Days": available_days, "Available Time": time_available,
                           "One Way Price": price1, "Round Trip": price2}
        Car_details = {"Car Model": car_model, "Number of Seats": no_of_seats}
        driver_details_list.append({
            "personal_details_driver": personal_details_driver,
            "Date_time_price": Date_time_price,
            "Car_details": Car_details
        })
        print(personal_details_driver)
        print(Date_time_price)
        print(Car_details)

    except ValueError:
        print("Invalid input. Please enter a valid integer for contact number and number of seats.")
        return  # Exit the function in case of error


# Function to display the first page and get user input
def first_page():
    print("Choose the number 1 if you're a driver")
    print("Choose the number 2 if you're a passenger")
    print("")
    while True:
        try:
            choice = int(input("Please enter your selection: "))
            if choice == 1:
                print("You have selected Driver")
                driver_details_list = []
                first_page_driver(driver_details_list)
                return driver_details_list
            elif choice == 2:
                print("You have selected Passenger")
                first_page_passengers()
                return None  # Return None for passenger option
            else:
                print("Please choose either 1 or 2")
        except ValueError:
            print("Invalid input. Please enter a valid integer for your selection.")


# Function to save driver details to a file
def save_driver_details(driver_details_list):
    file_name = "driver_details.txt"

    # Check if the file exists
    file_exists = os.path.isfile(file_name)

    with open(file_name, mode='a') as file:
        # Write column names only if the file doesn't exist
        if not file_exists:
            file.write("Name,Contact Number,Gender,Available Days,Available Time,One Way Price,Round Trip,Car Model,"
                       "Number of Seats\n")

        for driver_details in driver_details_list:
            personal_details = driver_details["personal_details_driver"]
            date_time_price = driver_details["Date_time_price"]
            car_details = driver_details["Car_details"]

            line = f"{personal_details['Name']},{personal_details['Contact Number:']},{personal_details['Gender']},{date_time_price['Available Days']},{date_time_price['Available Time']},{date_time_price['One Way Price']},{date_time_price['Round Trip']},{car_details['Car Model']},{car_details['Number of Seats']}\n"
            file.write(line)

    print("Driver details saved to", file_name)


# Function to run the main program
def run_program():
    welcome_message()
    driver_details_list = []
    while True:
        driver_details = first_page()
        if isinstance(driver_details, list):
            driver_details_list.extend(driver_details)
        print("\n")
        continue_program = input("Do you want to continue with the program? (Y/N): ")
        if continue_program.lower() != "y":
            break
        print("\n")

    if driver_details_list:
        save_driver_details(driver_details_list)


# Run the program
run_program()
