#!/data/data/com.termux/files/usr/bin/bash
clear

# =============================================
# TERMUX-SETUP MAIN MENU
# =============================================
while true; do
clear
echo -e "\e[1;32m=========================================\e[0m"
echo -e "\e[1;36m        L U C I F E R   T E R M U X\e[0m"
echo -e "\e[1;32m=========================================\e[0m"

echo -e "\e[1;33m[1]\e[0m Fast Termux Package Installer"
echo -e "\e[1;33m[2]\e[0m Termux Tools Menu (Hacker Dashboard)"
echo -e "\e[1;33m[3]\e[0m Network Tools Pack"
echo -e "\e[1;33m[4]\e[0m Safe Utility Tools Pack"
echo -e "\e[1;33m[0]\e[0m Exit"
echo ""
read -p "Choose an option: " choice

# =============================================
# 1. FAST PACKAGE INSTALLER
# =============================================
if [[ $choice == "1" ]]; then
clear
echo -e "\e[1;36mInstalling Fast Termux Packages...\e[0m"
pkg update -y
pkg upgrade -y
pkg install python git curl wget nano neofetch zip unzip htop -y
termux-setup-storage
echo -e "\e[1;32m✔ Fast Package Installation Complete!\e[0m"
sleep 2

# =============================================
# 2. HACKER DASHBOARD
# =============================================
elif [[ $choice == "2" ]]; then
while true; do
clear
echo -e "\e[1;32m=========== Hacker Dashboard ===========\e[0m"
echo -e "\e[1;35m[1]\e[0m Show System Info"
echo -e "\e[1;35m[2]\e[0m Show IP Address"
echo -e "\e[1;35m[3]\e[0m Show Storage Info"
echo -e "\e[1;35m[0]\e[0m Back"
read -p "Choose: " dash

case $dash in
1) neofetch; read -p "Enter to continue..." ;;
2) curl ifconfig.me; read -p "Enter to continue..." ;;
3) df -h; read -p "Enter to continue..." ;;
0) break ;;
*) echo "Invalid!"; sleep 1 ;;
esac
done

# =============================================
# 3. NETWORK TOOLS PACK
# =============================================
elif [[ $choice == "3" ]]; then
clear
echo -e "\e[1;34mInstalling Network Tools...\e[0m"
pkg install nmap net-tools dnsutils traceroute tcpdump -y
echo -e "\e[1;32m✔ Network Tools Installed!\e[0m"
sleep 2

# =============================================
# 4. SAFE TOOLS PACK
# =============================================
elif [[ $choice == "4" ]]; then
clear
mkdir -p ~/lucifer-tools
cd ~/lucifer-tools

echo 'echo "Your IP:"; ifconfig' > network_info.sh
echo 'htop' > system_monitor.sh

chmod +x *.sh

echo -e "\e[1;32m✔ Safe Tools Installed at ~/lucifer-tools!\e[0m"
sleep 2

# =============================================
# EXIT
# =============================================
elif [[ $choice == "0" ]]; then
clear
echo -e "\e[1;31mExiting Lucifer Setup...\e[0m"
sleep 1
exit

# =============================================
# INVALID OPTION
# =============================================
else
echo "Invalid option!"
sleep 1
fi

done
