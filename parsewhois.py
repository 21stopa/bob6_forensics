import pythonwhois
import argparse

parser = argparse.ArgumentParser(description='Get Information From domains in a file as Output in the Form of JSON.')
parser.add_argument('-i', action='store', nargs=1, required='True', metavar='[FILENAME]', help="Get Info from a domains-file")

args = parser.parse_args()
fName = args.i[0]

with open(fName) as file_object:
    domains = file_object.readlines()

for d in domains:
    print d.rstrip()
#data = pythonwhois.net.get_whois_raw(d,with_server_list =False)
