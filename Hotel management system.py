# hotel={"101":{"Name":"Manik", "Adhaar number":"987654321","No of people": 2, "check in date":"15/10/2025", "check out date":"20/10/2025",}}
# def main():
#     print("enter 1 for booking \n enter 2 for food order")
#     choice=int(input("enter your choice"))
#     if choice==1:
#         hotel_management_system()
    
#     elif choice==2:
#         food_order()
    
#     else:
#         print("invalid choice")
           
 







# def new_user ():
#     print("1 for room booking \n 2 for hall booking \n 3 for terrace booking \n 4 for bar booking \n  5 for table booking")
#     a=int(input("enter no"))
#     if a==1:
#         print("room booking")
#         name=input("enter your name")
#         adhaar_number=int(input("enter your 12 digit adhaar number"))
#         no_of_people=int(input("enter no of people"))
#         check_in_date=int(input("enter check in date"))
#         check_out_date=int(input("enter check out date"))
#         hotel[adhaar_number]={"name":name, "adhaar number":adhaar_number, "no of people":no_of_people, "check in date":check_in_date, "check out date":check_out_date}
#         print("room booked successfully")
#         print(hotel[adhaar_number])



#     elif a==2:
#         print("hall booking")
#     elif a==3:
#         print("terrace booking")
#     elif a==4:
#         print("bar booking")
#     elif a==5:
#         print("table booking")
#     else:
#         print("invalid input")

# def existing_user():
#     adhaar_number=int(input("enter your 12 digit adhaar number"))
#     for i in hotel:
#         for j in hotel[i]:
#             print(j,hotel[i][j])


# def hall_booking():
#     print("hall booking details")
#     hall_input=input("enter your input (party/meeting)")
#     if hall_input=="party":
#         print("party hall booked")
#     elif hall_input=="meeting":
#         print("meeting hall booked")
#     else:
#         print("invalid input")
        

# def terrace_booking():
#     print("terrace booking details")
#     terrace_input=input("enter terrace type")
#     if terrace_input=="open":
#         print("open terrace booked")
#     elif terrace_input=="closed":
#         print("closed terrace booked")
#     else:
#         print("invalid input")


# def bar_booking():
#     print("bar booking details")
#     bar_input=input("enter bar type")
#     if bar_input=="cocktail":
#         print("cocktail bar booked")
#     elif bar_input=="mocktail":
#         print("mocktail bar booked")
#     else:
#         print("invalid input")



# def table_booking():
#     print("table booking details")
#     table_input=input("enter table type")
#     if table_input=="4 chairs":
#         print("4 chair table booked")
#     elif table_input=="6 chairs":
#         print("6 chair table booked")
#     else:
#         print("invalid input")

    

# def food_order():
#     print("food order details")
#     food_input=input("what would you like to order?")
#     if food_input=="veg":
#         print("veg food ordered")
#     elif food_input=="non-veg":
#         print("non-veg food ordered")
#     else:
#         print("invalid input")



# def hotel_management_system():
#     user_input=int(input("press 1 for existing user \n press 2 for new user"))
#     if user_input==1:
#        existing_user()
#     elif user_input==2:
#         new_user()
#     else:
#         print("invalid input")



# main()




hotel = {}

def existing_user():
    print("1 for room booking \n2 for hall booking \n3 for terrace booking \n4 for bar booking \n5 for table booking")
    a = int(input("Enter no: "))
    
    if a == 1:
        print("Room Booking")
        name = input("Enter your name: ")
        adhaar_number = int(input("Enter your 12 digit Aadhaar number: "))
        no_of_people = int(input("Enter no of people: "))
        check_in_date = input("Enter check-in date (dd-mm-yyyy): ")
        check_out_date = input("Enter check-out date (dd-mm-yyyy): ")
        
        hotel[adhaar_number] = {
            "Name": name,
            "Aadhaar Number": adhaar_number,
            "No of People": no_of_people,
            "Check-in Date": check_in_date,
            "Check-out Date": check_out_date
        }
        
        print("Room booked successfully ")
        print(hotel[adhaar_number])

    elif a == 2:
        hall_booking()
    elif a == 3:
        terrace_booking()
    elif a == 4:
        bar_booking()
    elif a == 5:
        table_booking()
    else:
        print("Invalid input ")

def new_user():
    adhaar_number = int(input("Enter your 12 digit Aadhaar number: "))
    if adhaar_number in hotel:
        print("Booking found ")
        for key, value in hotel[adhaar_number].items():
            print(f"{key}: {value}")
    else:
        print("No booking found ")

def hall_booking():
    print("Hall booking details")
    hall_input = input("Enter your input (party/meeting): ")
    if hall_input.lower() == "party":
        print("Party hall booked ")
    elif hall_input.lower() == "meeting":
        print("Meeting hall booked ")
    else:
        print("Invalid input ")

def terrace_booking():
    print("Terrace booking details")
    terrace_input = input("Enter terrace type (open/closed): ")
    if terrace_input.lower() == "open":
        print("Open terrace booked ")
    elif terrace_input.lower() == "closed":
        print("Closed terrace booked ")
    else:
        print("Invalid input ")

def bar_booking():
    print("Bar booking details")
    bar_input = input("Enter bar type (cocktail/mocktail): ")
    if bar_input.lower() == "cocktail":
        print("Cocktail bar booked ")
    elif bar_input.lower() == "mocktail":
        print("Mocktail bar booked ")
    else:
        print("Invalid input ")

def table_booking():
    print("Table booking details")
    table_input = input("Enter table type (4 chairs / 6 chairs): ")
    if table_input == "4 chairs":
        print("4 chair table booked ")
    elif table_input == "6 chairs":
        print("6 chair table booked ")
    else:
        print("Invalid input ")

def food_order():
    print("Food order details")
    food_input = input("What would you like to order? (veg/non-veg): ")
    if food_input.lower() == "veg":
        print("Veg food ordered ")
    elif food_input.lower() == "non-veg":
        print("Non-veg food ordered ")
    else:
        print("Invalid input ")

def hotel_management_system():
    while True:
        user_input = int(input("\nPress 1 for existing user \nPress 2 for new user \nPress 3 to exit\nEnter choice: "))
        if user_input == 1:
            existing_user()
        elif user_input == 2:
            existing_user()
        
        else:
            print("Invalid input ")


hotel_management_system()
