import pandas as pd

# 1. Load both files
students_df = pd.read_csv("students.csv")
scores_df = pd.read_csv("scores.csv")

# 2. MERGE FIRST on 'student_id'
merged_df = pd.merge(students_df, scores_df, on="student_id")
print(" Merged DataFrame Preview ")
print(merged_df.head())

# 3. Check missing values in the merged dataset
print("\n Missing Values Count ")
print(merged_df.isna().sum())

# 4. Fill or remove missing data appropriately
# Drop rows missing crucial identifying information
merged_df = merged_df.dropna(subset=["student_id", "name"]).copy()

# Identify subject score columns (e.g., python, math, database)
score_cols = [col for col in ["python", "math", "database"] if col in merged_df.columns]

# Fill missing scores with column mean values
merged_df[score_cols] = merged_df[score_cols].fillna(merged_df[score_cols].mean())

# 5. Calculate each student's average score across subjects
merged_df["average_score"] = merged_df[score_cols].mean(axis=1)
print("\n Student Averages ")
print(merged_df[["student_id", "name", "major", "average_score"]].head())

# 6. Find the top 5 students
top_5_students = merged_df.sort_values("average_score", ascending=False).head(5)
print("\n Top 5 Students ")
print(top_5_students[["student_id", "name", "major", "average_score"]])

# 7. Compute average score by major
major_avg = merged_df.groupby("major")["average_score"].mean().reset_index()
print("\n Average Score by Major ")
print(major_avg)