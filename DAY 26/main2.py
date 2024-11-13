student_dict = {"student": ["Angela", "james", "Lily"], "score": [56, 76, 98]}

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
for index, row in student_data_frame.iterrows():
    print(index)
    print(row.student)
