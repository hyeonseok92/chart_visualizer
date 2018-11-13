reset
set size 1,0.5
set title "update: 256, type: CALC, page: 1048576, thread: 16"
set xlabel "Time (s)" offset 0,0.5
set ylabel "Throughput(K Txm/s)" offset 2,0
set y2label "Distance (MiB)" offset -1.5,0
set xtic 5
set ytic 2000 nomirror
set y2tic 8000
set xrange [0:60]
set yrange [0:11000]
set y2range [0:40000]
set key horizontal inside width -3.0 center top
set terminal postscript eps 20
set output "line_graph.eps"

plot "single_data.dat" using 1:2 title 'Throughput' with lines axes x1y1 lt 1 lw 2,\
    "single_data.dat" using 1:(valid(3) == 1 ? $3 : 1/0) title 'Log Dist' with lines axes x1y2 lt 3 lw 2
