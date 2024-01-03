# Create a function which checks correct name input
def check_names(name):

    # Returns true only when a letter is input
    flag = True if name.isalpha() == True else False
    return flag

# Create a function which checks DOB format
def check_DOB(dob):

    flag = True
    while flag == True:
        # Seperate day, month, and year and put into list
        dob_list = dob.split("/")

        # Checks if DOB input was in the correct format
        if len(dob_list) != 3:
            flag = False
            break

        day = dob_list[0]
        month = dob_list[1]
        year = dob_list[2]

        # Check day, month and year are integers
        for num in dob_list:
            try:
                int(num)
            except ValueError:
                flag = False
                break

        # Check month is int between 1 and 12
        if int(month) < 1 or int(month) > 12:
            flag = False
            break

        # Check the day is correct depending on the month
        # April, June, September and November only have 30 days
        months_30days = [4,6,9,11]
        if int(month) in months_30days:
            if int(day) < 0 or int(day) > 30:
                flag = False
                break

        # Feb has 29 days on a leap year
        elif int(month) == 2 and int(year) % 4 == 0:
            if int(day) < 0 or int(day) > 29:
                flag = False
                break
        
        # Feb has 28 days if not a leap year
        elif int(month) == 2 and int(year) % 4 != 0:
            if int(day) < 0 or int(day) > 28:
                flag = False
                break

        # Any other month has 31 days
        else:
            if int(day) < 0 or int(day) > 31:
                flag = False
                break
        break

    return flag

# Create a function which checks mobile number
def check_mobile(mobile):
    flag = True

    # Check the input is a set of integers
    try:
        int(mobile)
    except ValueError:
        flag = False

    # Check the input is only 10 characters long
    if len(mobile) != 10:
        flag = False

    return flag 

# Create a function which checks email
def check_email(email):
    flag = True
    while flag == True:
        # check email does not contain spaces
        if " " in email:
            flag = False
            break

        # change the str into a list containing [username,domain]
        email_list = email.split("@")

        # Check format is correct
        if len(email_list) != 2:
            flag = False
            break

        # Ensure username exist
        username = email_list[0]
        if username == "":
            flag = False
            break

        # Check username contains allowed character, letters or numbers
        allowed_characters = ['!','#','$','&','\'','*','+','-','/','=','?','^',
                      '_','`','{','|','}','~','.']
        for char in username:
            if char.isalnum() == False and char not in allowed_characters:
                flag = False
                break
        if flag == False:
            break
        
        # Check top-level domain is contained in domain
        # Only check common UK ones
        domain = email_list[1]
        tld_uk = [".com",".co.uk",".org",".net"]
        for tld in tld_uk:
            if tld in domain:
                flag = True
                break
            else:
                flag = False
        break
    return flag

# Create check street name
def check_street_name(street_name):
    flag = True

    # Create a list which contains each word
    split_address = street_name.split()

    # Check that each section of the address only contains a
    # letter or a number
    for item in split_address:
        if item.isalnum() == False:
            flag = False
            break
    return flag

# Create a function which checks the city name
def check_city(city):

    # Split the city name into a list, seperating by " "
    split_city = city.split()

    # Checks each word in the list is only alphabetical
    for item in city:
        flag = True if item.isalpha() == True else False
        if flag == False:
            break
    return flag

# Create a function to check postcode format
def check_postcode(postcode):
    
    flag = True
    while flag == True:

        # Check postcode is in correct format
        # A means an alphabetical character, N means a numerical character
        allowed_formats = ["AN NAA","ANN NAA","AAN NAA","AANN NAA",
                           "ANA NAA", "AANA NAA"]
        
        postcode_format = ""

        for char in postcode:

            # if its an alphabetical character, add A to the format
            if char.isalpha() == True:
                postcode_format += "A"

            # if its a numerical character, add N to the format
            elif char.isnumeric() == True:
                postcode_format += "N"

            # if its a space, add a space
            elif char == " ":
                postcode_format += " "

            # any other character flags an error
            else:
                flag = False
                break
        
        if postcode_format not in allowed_formats:
            flag = False
            break
        
        break
    return flag

user_info = {}

line = '-'*60
print(line)
print("Forshaw's Financial Consultation")
print(line)
print("Thank you for creating an account with us.\n"
      "To complete your registration, please complete the form below.")
print(line)
print("Personal Information:")

# User enters their forename, if incorrect input put in then it will
# ask the user to try again
while True:
    user_forename = input("\nForename:\n")
    if check_names(user_forename) == True:
        break
    else:
        print("Input error! Forename not recognised. Please try again.")


# User enters their surname, if incorrect input put in then it will
# ask the user to try again
while True:
    user_surname = input("\nSurname:\n")
    if check_names(user_surname) == True:
        break
    else:
        print("Input error! Surnames not recognised. Please try again.")

# User to select their gender from a list, if option not chosen from the
# list, user will be asked again
while True:
    print("\nSelect your gender from the list\n"
          "1. Male\n"
          "2. Female\n"
          "3. Non-binary\n"
          "4. Prefer not to say"
          "5. Other")
    option = input("Input the number for your selected option:\n")
    if option == "1":
        user_gender = "male"
        break
    elif option == "2":
        user_gender = "female"
        break
    elif option == "3":
        user_gender = "non-binary"
        break
    elif option == "4":
        user_gender = "prefer not to say"
        break
    elif option == "5":
        user_gender = input("Please enter your gender:\n")
        break
    else:
        print("Input error! Option not recognised. Please try again.")

# User inputs their date of birth, if typed in incorrect, it will ask
# again
while True:
    user_dob = input("\nDate of Birth (dd/mm/yyyy):\n")
    if check_DOB(user_dob) == True:
        break
    else:
        print("Input error! Date not recognised. Please try again.")

print(line)
print("Contact Information:")

# User inputs their phone number, if theres an error it will try again
while True:
    user_mobile = input("\nEnter your mobile number:\n"
                   "+44")
    if check_mobile(user_mobile) == True:
        user_mobile = "+44" + user_mobile
        break
    else:
        print("Input error! Mobile number not recognised. Please try again.")

# User inputs their email, if theres an error it will try again
while True:
    user_email = input("\nEnter your email address:\n")
    if check_email(user_email) == True:
        break
    else:
        print("Input Error! Email address not recognised. Please try again.")

# User inputs their street address, if theres an error it will try again
while True:
    user_address = input("\nEnter your house number and street address:\n")
    if check_street_name(user_address) == True:
        break
    else:
        print("Input error! Address not recognised. Please try again.")

# User inputs their city, if theres a mistake it will try again
while True:
    user_city = input("\nEnter the city you live in:\n")
    if check_city(user_city) == True:
        break
    else:
        print("Input Error! City not recognised. Please try again.")
        
# User inputs their postcode, if theres a mistake it will try again
while True:
    user_postcode = input("\nEnter your postcode:\n")
    if check_postcode(user_postcode) == True:
        break
    else:
        print("Input Error! Postcode not recognised. Please try again.")

# Add user information into a dictionary
user_info["Forename"] = user_forename
user_info["Surname"] = user_surname
user_info["Gender"] = user_gender
user_info["Date of Birth"] = user_dob
user_info["Mobile Number"] = user_mobile
user_info["Email"] = user_email
user_info["Street Address"] = user_address
user_info["City"] = user_city
user_info["Postcode"] = user_postcode
        
# Display the user information to the user
print(line)
print("Your information:")
for key, value in user_info.items():
    print(f"{key}: {value}")
print(line)
