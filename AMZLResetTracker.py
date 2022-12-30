import time
# Define a list of clusters that need to be reset
clusters = ['A', 'B', 'C', 'D', 'E', 'G']

# Initialize a dictionary to track the progress of each cluster
cluster_progress = {}

# Initialize a dictionary to store the total number of aisles in each cluster
cluster_aisles = {'A': 20, 'B': 20, 'C': 22, 'D': 22, 'E': 20, 'G': 20}

# Initialize a variable to store the total number of aisles
total_aisles = sum(cluster_aisles.values())

# Initialize the progress for each cluster to 0
for cluster in clusters:
  cluster_progress[cluster] = 0

# Main loop to track the progress of resetting the clusters
while True:
  # Print the overall status of the reset process
  print("Cluster progress @"+time.asctime()+": ")
  reset_aisles = 0
  for cluster, progress in cluster_progress.items():
    # Calculate the percentage progress for each cluster
    cluster_percent = (progress / cluster_aisles[cluster]) * 100
    print(f"{cluster}: {cluster_percent:.2f}% ({progress}/{cluster_aisles[cluster]} aisles)")
    reset_aisles += progress

  # Calculate the overall progress as a percentage
  overall_progress = (reset_aisles / total_aisles) * 100
  print(f"Overall progress: {overall_progress:.2f}%\n")

  # Prompt the user to enter the name of a cluster to update
  cluster = input("Enter the name of a cluster to update: ")

  # Check if the entered cluster is in the list of clusters
  if cluster not in clusters:
    print("Invalid cluster name. Try again.")
    continue

  # Prompt the user to enter the number of aisles that have been reset in the selected cluster
  aisles = input("Enter the number of aisles that have been reset in the selected cluster: ")

  # Check if the entered number of aisles is a valid integer
  if not aisles.isdigit() or int(aisles) < 0:
    print("Invalid input. The number of aisles must be a positive integer. Try again.")
    continue

  # Update the progress for the selected cluster
  cluster_progress[cluster] += int(aisles)

  # Check if all clusters have been reset
  if overall_progress == 100:
    print("All clusters have been reset successfully!")
    break
