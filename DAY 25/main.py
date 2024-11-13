import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_color = data["Primary Fur Color"].to_list()
gray = squirrel_color.count("Gray")
cinnamon = squirrel_color.count("Cinnamon")
black = squirrel_color.count("Black")
print(f"Gray = {gray}\nBlack = {black}\nCinnamon = {cinnamon}")
