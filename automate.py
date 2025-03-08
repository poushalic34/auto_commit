
import os
import datetime
import random

# Change directory to the repo
repo_path = "https://github.com/poushalic34/auto_commit"  # Update with your repo path
os.chdir(repo_path)

# Create or update a file
filename = "daily_update.txt"
with open(filename, "a") as file:
    file.write(f"Commit on {datetime.datetime.now()} - Random value: {random.randint(1, 100)}\n")

# Git commands to add, commit, and push
os.system("git add .")
os.system(f'git commit -m "Auto commit on {datetime.datetime.now().strftime("%Y-%m-%d")}"')
os.system("git push origin main")
