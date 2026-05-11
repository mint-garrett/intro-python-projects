##Two Lane Traffic Light Simulation
by: Garrett Vieira

##What is it?
A simple simulation of a two-lane traffic light that uses set data from a JSON file, and then prints the light color for a set time period. This currently runs for 3 cycles. Everything can be adjusted from the JSON file.

##Requirements
GNU Make
Python 3

##Tested with:
GNU Make 4.4.1 
Python 3.13.9

##Project Files
- README.md  = this file
- traffic_data.json = configuration data that traffic_simulation.py reads
- traffic_simulation.py = simulation script
- Makefile = allows traffic_simulation.py to be ran easier as "make run"

##How to run:
1. Unzip file and open the project directory in the terminal
2. Run (bash)$ make run
3. Simulation should start running in the terminal
