# Taxi booking system Documentation
  -Prathosh Chander and Saara Khobragade
## Topic 
A system for car booking (Lavasa to Pune)

## Description 
The Taxi booking system is a platform that facilitates available taxis between Lavasa and Pune, allowing drivers to enter their details and passengers to choose from a database of available drivers. The goal of the system is to provide a convenient mode of transportation for individuals traveling between the two locations. Passengers can view the availability of seats for specific timings and find drivers who are available at the chosen date and time .
## Data Types:

### String:
Used to store names, contact numbers, genders, locations, dates, and other textual data.
### Integer: 
Used to store numerical values such as the number of people, seats, and choices.
### List:
Used to store multiple values for names, contact numbers, genders, available days, etc.
### Dictionary: 
Used to store key-value pairs for personal details, travel details, driver details, etc.

## Functions used:

### welcome_message():

Displays a welcome message and provides an overview of the taxi booking system.

### first_page_passengers():

1. Collects personal details of passengers, such as names, contact numbers, and genders.
2. Prompts for pick-up location, destination, one-way or round trip selection, pick-up time, and date.
3. Converts the inputted pick-up time and date into datetime objects for further processing.
4. Stores the passenger's personal details and travel details in dictionaries.
5. Prints the personal and travel details for verification.
6. Lists out all the driver details.
7. It allocates a unique number to each driver and lets users choose a specific driver based on their preference.
8. Price gets displayed if more than one person is traveling the price gets divided among the passengers.



### first_page_driver(driver_details_list):

1. Collects personal details of a driver, including name, contact number, car model, number of seats, and gender.
2. Asks the driver for their availability on each day of the week.
3. Collects the available time slot, fare for one-way trip, and fare for a round trip.
4. Creates dictionaries for personal details, date and time availability, and car details. Appends the driver details to the driver_details_list.
5. Prints the personal details, date and time availability, and car details for verification.




### first_page():

1. Displays options for selecting either a driver or a passenger.
2. Takes user input and, depending on the choice, calls the appropriate function.
3. Returns the driver_details_list for drivers or an empty list for passengers.

### save_driver_details(driver_details_list):

1. Saves the driver details to a CSV file named "driver_details.txt".
2. Uses the csv module to write the driver details to the file.

### display_available_drivers(available_drivers):

1. Takes the available_drivers list as input.
2. Displays the details of available drivers, including their names, contact numbers, car models, and number of seats.

   
## Sample Output
### Welcome Message:

![WhatsApp Image 2023-06-20 at 15 40 18](https://github.com/PrathoshChristite/Carpooling_CIA-1/assets/118895000/f21c84b0-82cc-4030-9f5b-557098192fbe)

This output is displayed when the program starts, providing a welcoming message and an introduction to the system’s  purpose.

### Passenger Input:

![passengers](https://github.com/PrathoshChristite/Carpooling_CIA-1/assets/118895000/84ecaa71-f381-425a-a0ea-40e37bb488a6)

This output represents the input process for passengers. The passengers are prompted to enter their personal information (names, contact numbers, genders) and travel details (pick-up location, destination, one-way or two-way, pick-up time, pick-up date, payment method).

### Available Drivers

![WhatsApp Image 2023-06-20 at 16 06 16](https://github.com/PrathoshChristite/Carpooling_CIA-1/assets/118895000/8ab49ff3-e956-4f8d-bce6-672c4accdcaa)

This output displays the available drivers' details based on the passenger's requirements. It includes the driver's name, contact number, car model, and the number of available seats in their car.

### Driver Input:

![driver](https://github.com/PrathoshChristite/Carpooling_CIA-1/assets/118895000/6e3020e1-deb9-41be-8396-0de357e13d93)


This output showcases the input process for drivers. Drivers are prompted to provide their personal information (name, contact number, car model, number of seats, gender), availability on specific days, available time range, and fare details for one-way and two-way trips.

### run program 

![run](https://github.com/PrathoshChristite/Carpooling_CIA-1/assets/118895000/396fc3fd-ba8e-4ce9-957d-beacfeecdba0)

### driver details

![driver details](https://github.com/PrathoshChristite/Carpooling_CIA-1/assets/118895000/ea83b171-eaeb-44dc-b819-af7263526a69)



