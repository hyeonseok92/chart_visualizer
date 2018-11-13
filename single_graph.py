import sys
from math import ceil
from os import system,remove,rename

if len(sys.argv) <= 1:
    print("input file path is needed")
    sys.exit()

f = open(sys.argv[1], "r")
TIME = []
TPS = []
LOG = []
title = f.readline().rstrip()
while True:
    line = f.readline()
    if not line:
        break
    splitted_line = line.split(" ")
    i = 0
    while i < len(splitted_line):
        if splitted_line[i].endswith("s]"):#TIME
            if splitted_line[i][0] == '[':
                TIME.append(int(splitted_line[i][1:-2]))
            else:
                TIME.append(int(splitted_line[i][:-2]))

        elif splitted_line[i] == "TPS:":#TPS
            while True:
                i += 1
                if splitted_line[i]:
                    TPS.append(int(splitted_line[i]))
                    break

        elif splitted_line[i] == "LSN_d:":#LOG_DIST
            while True:
                i += 1
                if splitted_line[i]:
                    LOG.append(float(splitted_line[i]))
                    break

        i += 1
f.close()

f = open("single_data.dat", "w")
f.write(title + '\n')
for i in range(len(TIME)):
    f.write(str(TIME[i]) + "\t" + str(TPS[i]/1000.0) + "\t" + str(LOG[i]) + '\n')
f.close()

y2range_max = max(10, ceil(max([ceil(x) for x in LOG]) / 10000.0) * 10000)
system('sed -i -e "s/^set title.*/set title \\\"' + title + '\\\"/" single_graph.p')
system('sed -i -e "s/^set y2range.*/set y2range [0:' + str(y2range_max) + ']/" single_graph.p')
system('sed -i -e "s/^set y2tic.*/set y2tic ' + str(int(y2range_max/5)) + '/" single_graph.p')
system('gnuplot single_graph.p')
rename('line_graph.eps', title + '.eps')

remove("single_data.dat")
