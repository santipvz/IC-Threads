import matplotlib.pyplot as plt
import os
import pandas as pd

directory = os.path.dirname(os.path.abspath(__file__))

# We check if the directory exists
if not os.path.exists(os.path.join(directory, "images")):
    # If the directory doesn't exist, we create it
    os.mkdir(os.path.join(directory, "images"))


# We obtain the data
info = pd.read_csv("data.csv")

# Make Cores,Threads,Iteration,Time into integers
info = info.astype(
    {
        "CPU": "string",
        "Cores": "int",
        "Threads": "int",
        "Iteration": "int",
        "Time": "int",
    }
)

# The max number of threads
maxThreads = info["Threads"].max()

# We group by CPU
for cpu in info.groupby(["CPU"]):
    CPUname = cpu[0][0]

    plt.figure(figsize=(13, 9))  # This makes the image show the entire graph
    plt.title(CPUname, fontsize=22)
    plt.grid()

    # We put the dots of the average
    plt.scatter(
        [x + 1 for x in range(maxThreads)],
        [x * (10**-9) for x in cpu[1].groupby(["Threads"])["Time"].mean()],
        s=50,
        c="b",
        zorder=4,
        marker="o",
    )

    # We plot the average
    plt.plot(
        [x + 1 for x in range(maxThreads)],
        [x * (10**-9) for x in cpu[1].groupby(["Threads"])["Time"].mean()],
        linewidth=5,
        c="r",
        zorder=3,
        label="Average",
    )

    # We plot and scatter each iteration
    for iteration in cpu[1].groupby(["Iteration"]):
        plt.scatter(
            [x + 1 for x in range(maxThreads)],
            [x * (10**-9) for x in iteration[1]["Time"]],
            s=5,
            zorder=2,
            marker="o",
        )
        plt.plot(
            [x + 1 for x in range(maxThreads)],
            [x * (10**-9) for x in iteration[1]["Time"]],
            linewidth=1,
            zorder=1,
            label="Test " + str(iteration[0][0]),
        )

    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5), shadow=True, fancybox=True)
    plt.xlabel("Threads")
    plt.ylabel("Time (s)")

    # We save the image
    plt.savefig(os.path.join(directory, "images", CPUname + ".svg"))

plt.show()
