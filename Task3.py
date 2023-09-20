import pandas as pd

#loads csv file into the dataframe
df = pd.read_csv("assignment_data.csv") 

# since there were few records with zero sq ft value in the data given, it will give an inf when calculating the price per sq_ft
# so the records with zero sq-ft need to be removed.
df = df[df['sq__ft']!=0] 

#to calculate the price for square_ft
df['price_per_sqft'] = df['price'] / df['sq__ft'] 
print(df['price_per_sqft'])


# to calulate the average price per square_ft
average_price_per_sqft = df['price_per_sqft'].mean() 
print(average_price_per_sqft)

# to filter the properties that were sold less than avg price per sq-ft
new_df = df[df['price_per_sqft'] < average_price_per_sqft] 

# optional based on whether we want to keep the price_per_sqft column or not in our new dataset
# new_df = new_df.drop(columns=['price_per_sqft']) 


try:
    new_df.to_csv("output_csv_file.csv", index=False) # converting dataframe to  csv file
    print("New filtered CSV file is created")
except Exception as e:
    print("error occured:", e)


#average_price_per_sqft = 145.67


 






