watch -n 10 "python crtGet.py > crt.temp;mv crt.temp crt"

while date
do
  curl http://www.us-proxy.org/ 2>/dev/null | grep "<tr><" | sed s/\<tbody\>//g | awk -F "<" '{print "http://"$3":"$5}'| sed s/td\>//g > proxy
  echo Start Scatter
  bash -c "for i in "\$"(cat proxy)
  do
    echo Running "\$"i
    { python sendData.py "\$"i & }
    while [ "\$"(jobs | wc -l) -ge 10 ]
    do
      sleep 10
    done
  done" &
  sleep 300
  echo End Scatter
  kill %1 %2 %3 %4 %5 %6 %7 %8 %9 %10 %11 %12
done
