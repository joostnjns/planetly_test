import pandas as pd

df = pd.read_csv(r"..\GlobalLandTemperaturesByCity\GlobalLandTemperaturesByCity.csv", encoding = 'utf-8')
print("Before cleaning: ", str(df.dt.count()))

# Remove entries where date or temperature is empty (not useable in API)
df.dropna(subset = ['dt', 'AverageTemperature', 'City', 'Country'], inplace=True )
print("After removing NaN: ", str(df.dt.count()))

# Create different columns for year, month and day
df[['year', 'month', 'day']] = df['dt'].str.split('-', 0, expand=True)   #0: return all splits; expand=True: return dataframe instead of series


# Write output
df.to_csv(r'C:\Users\jneuj\Downloads\planetly\GlobalLandTemperaturesByCity\GlobalLandTemperaturesByCity_preprocessed.csv', sep=',', encoding = 'utf-8', index=False)