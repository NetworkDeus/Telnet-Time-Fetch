import os
try:
  os.system('telnet india.colorado.edu 13 > out.dat && clear')

  with open('out.dat','r') as log:
    lines=log.readlines()
    print(lines[4].split()[2])
except:
  print('ERROR!')