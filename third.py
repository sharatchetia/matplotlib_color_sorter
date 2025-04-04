import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Conveyor belt properties
belt_length = 10
belt_y = 5

# Object properties
objects = []

# Sorting positions for different colors
sorting_bins = {"red": 3, "blue": 6, "green": 9}

fig, ax = plt.subplots()
ax.set_xlim(0, belt_length)
ax.set_ylim(0, 10)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Sorting System Simulation")

# Draw conveyor belt
belt = plt.Rectangle((0, belt_y - 0.5), belt_length, 1, color="gray", alpha=0.5)
ax.add_patch(belt)

# Draw bins
for color, xpos in sorting_bins.items():
    ax.add_patch(plt.Rectangle((xpos - 0.5, 0), 1, 2, color=color, alpha=0.3))

circles = []

def spawn_object():
    obj = {"x": 0, "y": belt_y, "size": np.random.randint(5, 15), "color": np.random.choice(["red", "blue", "green"]) }
    objects.append(obj)
    circle = plt.Circle((obj["x"], obj["y"]), obj["size"] / 50, color=obj["color"])
    circles.append(circle)
    ax.add_patch(circle)

def update(frame):
    if frame % 20 == 0:  # Spawn a new object every 20 frames
        spawn_object()
    
    for i, obj in enumerate(objects):
        if obj["x"] < sorting_bins[obj["color"]]:
            obj["x"] += 0.1  # Move forward
        else:
            obj["y"] -= 0.1  # Drop into bin
        circles[i].center = (obj["x"], obj["y"])
    return circles

ani = animation.FuncAnimation(fig, update, frames=1000, interval=100, blit=False)
plt.show()
