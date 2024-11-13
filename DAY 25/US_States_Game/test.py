import pandas as pd

answer_state = "Alabama"
data = pd.read_csv("US_States_Game\\50_states.csv")
data = data.set_index("state")
data = data.index
data = data.reset_index()
print(data)
