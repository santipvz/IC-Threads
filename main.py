import subprocess
import cpuinfo
import os


if __name__ == "__main__":
    cpuName = cpuinfo.get_cpu_info()["brand_raw"]
    nCores = os.cpu_count()

    subprocess.run(["bash", "Colector.sh"])

    # We get the data from times.txt
    with open("times.txt", "r") as file:
        info = [line.strip() for line in file.readlines()]

    # The first line needs to be the cpu name
    if info[0] != cpuName:
        raise Exception(f"CPU name mismatch: {info[0]} != {cpuName}")
