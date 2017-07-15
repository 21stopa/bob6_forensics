import pythonwhois
import argparse
import json
import datetime
import yaml

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown Type")

parser = argparse.ArgumentParser(description='Get Information From domains in a file as Output in the Form of JSON.')
parser.add_argument('-i', action='store', nargs=1, required='True', metavar='[FILENAME]', help="Get Info from a domains-file")

args = parser.parse_args()
fName = args.i[0]

with open(fName) as file_object:
    domains = file_object.readlines()

for d in domains:
    data = pythonwhois.get_whois(d)
    output_str = json.dumps(data, default=datetime_handler)
    output_json = yaml.load(output_str)
    with open(d + '.json', 'a') as outfile:
        json.dump(output_json, outfile)

