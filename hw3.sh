cd /home/guest/Documents
date > Current-ports.txt
nmap -p1-65535 --open 192.168.10.*/24 >> Current-ports.txt

date >> changes.txt
diff Current-ports.txt Base-ports.txt >> changes.txt

cp Current-ports.txt Base-ports.txt
