echo off
set output=%1
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"
set "datestamp=%YYYY%%MM%%DD%" & set "timestamp=%HH%%Min%%Sec%"
"C:\Program Files (x86)\Wireshark\tshark.exe" -i \Device\NPF_{EC9A82BA-3169-41F0-A45D-1B03A7311955} -w C:\%datestamp%%timestamp%.pcap > NUL
echo on
