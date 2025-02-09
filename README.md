# Threads

## Overview

This is a project for a subject called "Introducción a los computadores" (Introduction to Computers) that accounted for 70% of the final grade. It was made by a team of 3 people. The submission took place on Thursday, the 27th of November of 2022, and earned a grade of 7.8 out of 10 points.

## Project Summary

For this project we had to create a program that measured how long a CPU-intensive task took to complete using more or less threads. Here are the instructions we were given in spanish: [Project Instructions (Spanish)](docs/proyecto%20grupo%20ic.pdf). With the results we realized that we did not use threads properly; we only used one actual CPU core due to Python's Global Interpreter Lock (GIL). Now it uses processes so it can use all the CPU cores.

## Contributing

You can contribute to this project by adding the data of your CPU. You need to run [main.py](main.py) and check if it adds the CPU data to the [data.csv](data.csv) file. If it doesn't, it means that the data is already there. If it is added, create a fork with the name of your CPU and make a pull request. Ensure that your branch is up to date with main and only change [data.csv](data.csv). Create a fork for each CPU you want to add.
