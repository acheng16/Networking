Name: Andrew Cheng
Section: Section 2 (2:20pm-3:40pm)
Used to run program: 
python3 ftps.py <local-port-on-gamma> <troll-port-on-gamma>
troll -C <IP-address-of-beta> -S <IP-address-of-gamma> -a <client-port-on-beta>
-b <server-port-on-gamma> <troll-port-on-beta> -t -x <packet-drop-%>
troll -C <IP-address-of-gamma> -S <IP-address-of-beta> -a <server-port-on-gamma>
-b <client-port-on-beta> <troll-port-on-gamma> -t -x <packet-drop-%>
python3 ftpc.py <remote-IP-gamma> <remote-port-on-gamma> <troll-port-on-beta>
<local-file-to-transfer>
Notes:
Beta(client) is binded to port 9611
