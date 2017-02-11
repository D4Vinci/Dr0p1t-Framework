@echo off
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
netsh firewall set service type = remotedesktop mode =enable
netsh firewall add portopening tcp 3389 rdp
netsh firewall add portopening udp 3389 rdp
