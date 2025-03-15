import pandas as pd
from matplotlib import pyplot as plt

grades = [90.5, 100.0, 75.8, 25.6]
studytime = [40, 50, 35, 10]

df = pd.DataFrame(grades, columns=['Grades'])

df["studytime"] = studytime

print(df)

plt.scatter(grades, studytime)
plt.show()