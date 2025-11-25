#!/data/data/com.termux/files/usr/bin/bash

# USERNAME & PASSWORD
username="pkthelucifer"
password="Lucifer@143"

# Clear Screen
clear

# Banner
echo -e "\e[1;31m
██╗     ██╗   ██╗ ██████╗██╗███████╗███████╗██████╗ 
██║     ██║   ██║██╔════╝██║██╔════╝██╔════╝██╔══██╗
██║     ██║   ██║██║     ██║█████╗  █████╗  ██████╔╝
██║     ██║   ██║██║     ██║██╔══╝  ██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚██████╗██║██║     ███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
\e[0m"

echo -e "\e[1;32m          Welcome Lucifer\e[0m"
echo -e "\e[1;34m            Powered by Foysal\e[0m"
echo ""
echo "-------------------------------------------"

# Login Prompt
read -p "Username: " input_user
read -s -p "Password: " input_pass
echo

if [[ "$input_user" == "$username" && "$input_pass" == "$password" ]]; then
    echo -e "\e[1;32mLogin Successful! Welcome Lucifer.\e[0m"
    sleep 1
    clear
else
    echo -e "\e[1;31mWrong Username or Password!\e[0m"
    exit
fi
