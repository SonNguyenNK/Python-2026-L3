import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("scores (1).csv")

plt.figure(figsize=(9, 5))
plt.scatter(df.student_id, df["math"], color="blue", label="Math", s=1000000)
plt.scatter(df.student_id, df["python"], color="green", label="Python", s=60)
plt.scatter(df.student_id, df["database"], color="orange", label="Database", s=60)
plt.tick_params(axis="x" , labelrotation=45)
plt.title("Student Scores Scatter Plot")
plt.xlabel("Student Index")
plt.ylabel("Scores")
plt.legend()
plt.grid(True, linestyle="--",)
plt.tight_layout()
plt.savefig("scatter.png")
plt.close()


fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
subjects = ["math", "python", "database"]
titles = ["Math", "Python", "Database"]
colors = ["blue", "green", "orange"]

for i, subject in enumerate(subjects):
    axes[i].hist(
        df[subject].dropna(),
        bins=6,
        color=colors[i],
        edgecolor="black",
    )
    axes[i].set_title(f"{titles[i]} Histogram")
    axes[i].set_xlabel("Marks")
    axes[i].set_ylabel("Frequency")
    axes[i].grid(True, linestyle="--",)

plt.tight_layout()
plt.savefig("histograms.png")
plt.close()


plt.figure(figsize=(7, 5))
box_data = [
    df["math"].dropna(),
    df["python"].dropna(),
    df["database"].dropna(),
]
plt.boxplot(
    box_data, tick_labels=["Math", "Python", "Database"], patch_artist=True
)
plt.title("Course Marks Distribution")
plt.ylabel("Marks")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Save to box.png
plt.savefig("box.png")
plt.close()