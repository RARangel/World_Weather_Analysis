# Import the dependencies.
import pandas as pd
import gmaps
import requests
# Import the API key.
from config import g_key

# Store the CSV you saved created in part one into a DataFrame.
city_data_df = pd.read_csv("weather_data/cities.csv")
city_data_df.head()