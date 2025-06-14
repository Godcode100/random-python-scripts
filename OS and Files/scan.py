import argparse
if __name__ == '__main__':

    description = """Use Cases:
        + Basic Scan:
            -target 127.0.0.1
        +Specific Port Scan
            -target 127.0.0.1 -Port 21
        +Port List:
            -target 127.0.0.1 -Port 21,22
        +Only show open Ports:
            -target 127.0.0.1 --open True"""

    parser = argparse.ArgumentParser(description="PortScanning",epilog=description,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-target",metavar="TARGET",dest="target",help="trget to scan",required=True)
    parser.add_argument("-ports",dest="ports",help="specify the target ports seperated by comma[80,8080 by default]",default="80,8080")
    parser.add_argument("-v",dest="verbosity",default=0,action="count",help="verbosity level -v -vv -vvv")
    parser.add_argument("--open",dest="only_open",action="store_true",default=False,help="Only display Open Ports")

    site_details = parser.parse_args()
    print("Target:"+ site_details.target)
    print("Verbosity:"+str(site_details.verbosity))
    print("Open Ports" + str(site_details.only_open))
    portlist =site_details.ports.split(',')
    #print("Ports:"+portlist)
    for port in portlist:
        print("Ports" + port)
    
