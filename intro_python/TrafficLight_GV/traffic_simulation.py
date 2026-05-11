import json 
import time
import sys

json_data = []
def import_json(filename):
    with open(filename, "r") as read:
        json_data = json.load(read)
    return json_data

def simulation(json_stuff):

    #setup
    light_cycle = json_stuff["light_cycles"]
    traffic_pattern = json_stuff["traffic_pattern"]
    light_patterns = json_stuff["light_patterns"]

    #UI
    print(f"--{traffic_pattern.upper()} SIMULATOR--\n")

    #master loop
    for i in range(light_cycle):
        print(f"Light Cycles: {i+1}/{light_cycle}")
        #scans in light colors for every i in master loop
        for light in light_patterns:
            light_color = light["color"]
            light_duration = light["time"]
            print(f"{light_color.upper()}: {light_duration} seconds")
            time.sleep(light_duration)
        print("\n")

def main():
    try:
        if len(sys.argv) > 1:
            json_file = sys.argv[1]
            data = import_json(json_file)
            simulation(data)
    except Exception as E:
        print(E)

if __name__ == "__main__":
    main()