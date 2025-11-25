#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "\e[1;32m[✓] Installing Lucifer Login Panel...\e[0m"
sleep 1

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

chmod +x "$DIR/login.sh"

BASHRC="/data/data/com.termux/files/usr/etc/bash.bashrc"

sed -i '/login.sh/d' $BASHRC

echo "bash $DIR/login.sh" >> $BASHRC

sleep 1
clear

echo -e "\e[1;32m[✓] Lucifer Login Panel Installed Successfully!\e[0m"
sleep 0.5

echo -e "\e[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\e[0m"
echo -e "\e[1;33m         🔁 Restart Your Termux         \e[0m"
echo -e "\e[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\e[0m"
echo ""
echo -e "\e[1;37mClose the app and open it again.\e[0m"
echo ""
