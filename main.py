import subprocess
import cpuinfo
import os
import pandas as pd


if __name__ == "__main__":

    cpuName = cpuinfo.get_cpu_info()["brand_raw"]
    nCores = os.cpu_count()

    # We get the number of iterations
    with open("iterations.txt", "r") as file:
        nIterations = int(file.readline())

    # We get the number of max threads
    with open("threads.txt", "r") as file:
        nThreads = int(file.readline())

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

    # Now we check if this CPU is already in the data
    alreadyTimed = True

    if cpuName in data.index.get_level_values("CPU"):
        # We get the rows with the same CPU
        rows = data.xs(cpuName, level="CPU")

        # We check if the number of cores is the same
        if nCores in rows.index.get_level_values("Cores"):
            # We get the rows with the same number of cores
            rows = rows.xs(nCores, level="Cores")

            # Now the rows need to have all combinations of threads and iterations
            for nThread in range(1, nThreads + 1):
                for nIter in range(1, nIterations + 1):

                    if (nThread, nIter) not in rows.index:
                        alreadyTimed = False
                        break
        else:
            alreadyTimed = False
    else:
        alreadyTimed = False

    # If the CPU is not in the data, we need to time it
    if not alreadyTimed:
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

    else:
        print("This CPU is already in the database")
