import csv 

#Assignment 1

# a (1)
# Question: Load the data from a CSV file into memory using the CSV module. The path
# to the file will be specified by the user then use these loaded data to perform
# following tasks.
pathToCsv = input("Enter your path to csv:\n")

with open(pathToCsv, "r") as csvFile:
    csvReader = csv.DictReader(csvFile)

    # a (2)
    # Retrieve a name of listing, host_name, description, host_location, and the
    # date the host was created for an individual host by host_id 
    hostId = input("Enter the host id:\n")

    for row in csvReader:
        if row["host_id"] == str(hostId):
            #host name
            print("--------------------------------------")
            print("Host name: ")
            print(row["host_name"])
            #description
            print("--------------------------------------")
            print("Description: ")
            print(row["description"])
            #host location
            print("--------------------------------------")
            print("Location: ")
            print(row["host_location"])
            #Date
            print("--------------------------------------")
            print("Created date: ")
            print(row["host_since"])
            print("--------------------------------------")
            break
    

    # a (3)
    # Retrieve host_name, property_type, price, minimum_nights, and
    # maximum_nights of all Airbnb listing for a specified location
    location = input("Enter your location:\n")

    for row in csvReader:
        if row["host_location"] == str(location):
            #host name
            print("--------------------------------------")
            print("Host name: ")
            print(row["host_name"])
            #Property type
            print("--------------------------------------")
            print("Property type: ")
            print(row["property_type"])
            #host location
            print("--------------------------------------")
            print("Price: ")
            print(row["price"])
            #Minimum nights
            print("--------------------------------------")
            print("Minimum nights: ")
            print(row["minimum_nights"])
            #Maximum nights
            print("--------------------------------------")
            print("Minimum nights: ")
            print(row["maximum_nights"])
            print("--------------------------------------")
            break
    
    # a (2)
    propertyType = input("Enter your property type:\n")

    for row in csvReader:
        if row["property_type"] == str(propertyType):
            #host name
            print("--------------------------------------")
            print("Room type: ")
            print(row["room_type"])
            #Property type
            print("--------------------------------------")
            print("Accomodates: ")
            print(row["accommodates"])
            #host location
            print("--------------------------------------")
            print("Bathroom: ")
            print(row["bathrooms_text"])
            #Minimum nights
            print("--------------------------------------")
            print("Bedrooms: ")
            print(row["bedrooms"])
            #Maximum nights
            print("--------------------------------------")
            print("Beds: ")
            print(row["beds"])
            print("--------------------------------------")
            break






# df = pd.read_csv(pathToCsv)

# hostId = int(input("Enter the host id:\n"))
# row = df.loc[df["host_id"] == hostId]
# print(f"\n\nDATA FOR HOST ID {hostId}\n")
# print(row.filter(["host_id", "property_type", "price", "minimum_nights", "maximum_nights"]))


# location = input("Enter your location:\n")
# locRow = df.loc[df["host_location"] == location]
# print(f"\n\nDATA FOR LOCATION {location}\n")
# print(locRow.filter(["host_id", "property_type", "price", "minimum_nights", "maximum_nights"]))

# property_type = input("Enter your property type:\n")
# propertyRow = df.loc[df["property_type"] == property_type]
# print(f"\n\nDATA FOR PROPERTY TYPE {property_type}\n")
# print(propertyRow.filter(["host_id", "room_type", "accommodates", "bathrooms", "bedroom", "beds"]))




