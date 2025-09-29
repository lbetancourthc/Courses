import argparse
import json
import os
import sys

def formatter(string, sort_keys=True, indent=4):
    # Load incoming string into JSON
    loaded_json = json.loads(string)
    # Dump as a string
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

def main(path, sort):
    with open(path, "r") as f:
        print(formatter(f.read(), sort_keys=sort))

if __name__ == "__main__":
    main(sys.argv[-1], sort=True)

# Example of use after remove args
# main(sys.argv[-1]) => python3 jformat.py examples/example.json