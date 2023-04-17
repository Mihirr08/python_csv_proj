import pandas as pd

pathToCsv = input("Enter your path to csv:\n")

df = pd.read_csv(pathToCsv)

# Identifying the top 10 most popular amenities or features that Airbnb hosts
# provide to customer


sortedDf = df.sort_values("review_scores_rating", ascending = False)

print("--------------------Top 10 amenities ----------------------------")
print(sortedDf.head(10).filter(["amenities"]))


# Analyse the average price of stay in each location
location = input("\nEnter your location to get average price:\n")

locRow = df.loc[df["host_location"] == location]

locRow = locRow.filter(["price"])

priceAddition = 0.0
for index, row in locRow.iterrows():
    priceAddition = priceAddition + int(row.iloc[0])


number_of_row, _ = locRow.shape
print(f"\nAverage price for {location} is {(priceAddition / (number_of_row))} ")


# Analyse the average review scores rating for each location
# reviewLocation = input("\nEnter your location to get average review of that location:\n")

locations = list(set(df["host_location"]))

input("\nPress enter to get average rating for all locations\n")

print("\n----------------------------Average rating for each locations-------------------------------------\n")
for loc in locations:
    currentLocRows = df.loc[df["host_location"] == loc].filter(["review_scores_value"])
    tempPrice = 0.0
    for _, row in currentLocRows.iterrows():
        tempPrice = tempPrice + int(row.iloc[0])

    total_row, _ = currentLocRows.shape
    print(f"{loc} : {(tempPrice / (total_row))} ")

# row = df.loc[df["host_id"] == "hostId"]


