import pandas as pd

MyCourses = {
    'Class': ['CS101', 'CS94', 'CS20'],
    'Instructor': ['Bruce', 'Picara', 'Mitzenmacher'],
}

df = pd.DataFrame(MyCourses)
print(df)
