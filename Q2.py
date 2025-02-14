# Import libraries
import matplotlib.pyplot as plt
import numpy as np
with open("data2.txt","r") as fin:
    data=fin.read()
#data="ATCGTAGCTAGCTACGATCGATCGTAGCTAGCTAGCTGACTGATCGTAGCTAGCTAGCTAGCTGACTGATCGTAGCTAGCTAGCTAGCTGACT"
nucleotides = ["A", "T", "C", "G"]
genome_length=len(data)
genome = ""
for i in range(genome_length):
 genome += data[i]

# We'll use the parametric equations for a helix:
# x = cos(t), y = sin(t), z = t (or a scaled version of t)
# We want to span a range so that the helix makes a few turns.
t = np.linspace(0, 4 * np.pi, genome_length) # 4*pi gives about
#2 turns
x = np.cos(t)
y = np.sin(t)
z = np.linspace(0, 5, genome_length) # z increases linearly to
#spread out the helix vertically
# Combine the coordinates into a (genome_length x 3) array
coordinates = np.column_stack((x, y, z))
colors = {'A': 'red', 'T': 'blue', 'C': 'green', 'G': 'orange'}
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for i, nucleotide in enumerate(genome):
 ax.scatter(coordinates[i, 0], coordinates[i, 1], coordinates[i, 2],
 color=colors[nucleotide], marker='o')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Genome Visualization")
plt.show()