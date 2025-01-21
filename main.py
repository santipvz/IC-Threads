import subprocess
import cpuinfo
import os
import pandas as pd


if __name__ == "__main__":

    cpuName = cpuinfo.get_cpu_info()["brand_raw"]
    nCores = os.cpu_count()

    # We check that data.csv exists
    if os.path.exists("data.csv"):

        # We read the data
        data = pd.read_csv("data.csv")

    else:
        data = pd.DataFrame(columns=["CPU", "Cores", "Threads", "Iteration", "Time"])

    data = data.astype(
        {
            "CPU": "string",
            "Cores": "int",
            "Threads": "int",
            "Iteration": "int",
            "Time": "int",
        }
    )

    # Set the combination of columns as a multi-index
    data.set_index(["CPU", "Cores", "Threads", "Iteration"], inplace=True)

    subprocess.run(["bash", "Colector.sh"])

    # We get the data from times.txt
    with open("times.txt", "r") as file:
        info = [line.strip() for line in file.readlines()]

    # The first line needs to be the cpu name
    if info[0] != cpuName:
        raise Exception(f"CPU name mismatch: {info[0]} != {cpuName}")

    # Each line is an iteration
    for i, line in enumerate(info[1:]):
        # Each number is with a different amount of threads
        for j, time in enumerate(line.split(",")):

            # We create the row index
            rowIndex = {
                "Cores": nCores,
                "Threads": j + 1,
                "Iteration": i + 1,
                "CPU": cpuName,
            }

            # Reorder the keys based on the MultiIndex level names
            indexValues = tuple(rowIndex[name] for name in data.index.names)

            data.loc[indexValues] = {"Time": time}

    data.sort_index(inplace=True)

    # We save the data
    data.to_csv("data.csv", index=True)
