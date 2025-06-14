import argparse
if __name__ =='__main__':

    description ="""USES:
    +Basic Scan:
        -target 127.0.0.1
    +Port Scan:
        -target 127.0.0.1  -ports 21
"""

parser = argparse.ArgumentParser(description="Port Scan", epilog= description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-target",dest="target",metavar="TARGET",help="scans a target",required=True)
parser.add_argument("-ports",dest="ports",help="specify target ports seperated by comma 80,8080,",default="80,8080")
parser.add_argument("-v",dest="verbosity",help= "-v -vv -vvv",default=0,action="count")
parser.add_argument("--openPort",dest="Only_open",help="Diplay open Ports",action="store_true",default=False)
url_details =parser.parse_args()
print("Target: " + url_details.target)
print("verbosity: " + str(url_details.verbosity))
print("Open Ports: " + str(url_details.Only_open))

ports_Open = url_details.ports.split(',')
for ports in ports_Open:
    print("Ports: " + ports)