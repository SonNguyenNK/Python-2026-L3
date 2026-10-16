import pandas as po
d=po.read_csv("students.csv")

#1st step
print("first 5 rows")
print(d.head())

#2nd step
rows=d.shape
cols=d.shape
print(f"number of rows {rows} and number of cols {cols}")

#3rd step
name_gpa=d[["name","GPA"]]
print("\n name + GPA")
print(name_gpa.head())

#4th step
high_gpa=d[d["GPA"]>=3.5]
print("\n gud score, scholarship ez")
print(high_gpa)

#5th step
sort_gpa=d.sort_values("GPA", ascending=False)
print("\n students get high and go low")
print(sort_gpa)

#6th step
average_gpa_major=d.groupby("major")["GPA"].mean()
print("\n average gpa by major")
print(average_gpa_major)
