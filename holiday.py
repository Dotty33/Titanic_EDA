# Welcoming message with information on what is the purpose of the program.
print("Hello - This program will help you to calculate your Holiday costs. These are our destinations: ") 

#user input for the city choice. Each city is numbered.
city = input("\n1. Barcelona\n2. Rome\n3. Paris\n4. Oslo\n Please make your city choice by selecting the corresponding number: ")

# a responce to the user's choice to make it more personalised                      
print("!! Fantastic choice !!")

# defining a function to calculate the flight cost
def plane_cost(city):
    """ This function calculates the city flight cost """ # documenting the role of the function
    
    if city == '1': # using the if/elif statements to assign each city - the statement to its price - the argument.
        return 150
    
    elif city == '2':
        return 180
            
    elif city == '3':
            return 120
    
    elif city == '4':
           return 110
    else:
            print ("You have selected an invalid option") #in case the input is not integer the user will be asked to enter the right value
            return 0

sum_plane_cost = plane_cost(city) # variable assigned to the total value of the function
print(f"The return flight to your chosen city will cost: {sum_plane_cost}") #calling the function to return the relevant value

#user input for the number of night required
num_nights = int(input(f"How many nights would you like to stay? ")) 
choice_n = int(0)
choice_n = num_nights
#varaible assigned to the hotel pp/n
Hotel_cost = 1
r = Hotel_cost

#defining the function calculating the hotel costs - followed similiar process as the plane_cost function minus the if/elif statements.
def hotel_cost(n, r = 100):
 """ This is a function that returns the sum of the nights and the room price"""
 return n * r

sum_hotel_cost = hotel_cost (choice_n * r)
print(f"The Hotel cost for {num_nights} nights is: ",sum_hotel_cost) #incorporating an f string to provide clear output to the user

#setting up variable and defining a function to calculate the car rental - similiar proccess as the hotel-cost function
rental_days = int(input("How many days do you need a car rental for?  "))
choice_CR_daily = int(0)
choice_CR_daily = rental_days

Car_cost = 1
z = Car_cost


def car_rental(v, z = 80):
 """This function calculates the cost of a car rental """
 return v * z

sum_car_rental = car_rental (choice_CR_daily * z)
print(f"The cost of your car rental for {choice_CR_daily} days is: ", sum_car_rental) #incorporating an f string to provide clear output to the user
 
#defining the last function to calculate the total cost of the holiday
def holiday_cost(a, b, c): 
 """ This function calculates the total cost of the holiday"""
 return a + b + c #asking the function to return the sum total of the above function's calculations.

a = sum_hotel_cost 
b = sum_plane_cost
c = sum_car_rental

hols_total = holiday_cost(sum_hotel_cost, sum_plane_cost, sum_car_rental)
print(f"The total cost of your holiday is:, \n{hols_total}\n Thank you for using our services,\n3Enjoy your holidays ") #incorporating an f string to provide clear output to the user

    
