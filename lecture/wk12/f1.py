import sys

print("Error! Warning! Danger", file=sys.stderr)

# you can user print to send data to another destination

print("Output message here", file=sys.stdout)

print("Input this data to a file", file=open("test1.txt", "w"))
