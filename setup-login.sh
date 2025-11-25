#!/data/data/com.termux/files/usr/bin/bash
username="pkthelucifer"
password="Lucifer@143"

animate_color_banner() {
    text="$1"
    colors=(31 32 33 34 35 36)
    for i in {1..16}; do
        clear
        color=${colors[$((i % 6))]}
        echo -e "\n\n"
        echo -e "                 \e[1;${color}m${text}\e[0m"
        echo -e "                    \e[1;32mWelcome Lucifer\e[0m"
        echo -e "                   \e[1;34mPowered by Foysal\e[0m"
        echo ""
        sleep 0.06
    done
}

loading() {
    clear
    echo -e "\n\n"
    echo -e "                \e[1;36mInitializing System...\e[0m\n"
    bar=""
    for i in {1..30}; do
        bar+="#"
        echo -ne "                [\e[1;32m$bar\e[0m] $((i*3))% \r"
        sleep 0.05
    done
    echo -e "\n\n               \e[1;32mLoading Complete!\e[0m"
    sleep 0.7
}

banner_text="
██╗     ██╗   ██╗ ██████╗██╗███████╗███████╗██████╗ 
██║     ██║   ██║██╔════╝██║██╔════╝██╔════╝██╔══██╗
██║     ██║   ██║██║     ██║█████╗  █████╗  ██████╔╝
██║     ██║   ██║██║     ██║██╔══╝  ██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚██████╗██║██║     ███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
"

loading
animate_color_banner "$banner_text"

clear
echo -e "\n\n\e[1;31m$banner_text\e[0m"
echo -e "                 \e[1;32mWelcome Lucifer\e[0m"
echo -e "                \e[1;34mPowered by Foysal\e[0m"
echo ""
echo "-------------------------------------------"

read -p "Username: " input_user
read -s -p "Password: " input_pass
echo

if [[ "$input_user" == "$username" && "$input_pass" == "$password" ]]; then
    echo -e "\e[1;32mLogin Successful! Welcome Lucifer.\e[0m"
    sleep 1
    clear
else
    echo -e "\e[1;31mWrong Username or Password!\e[0m"
    kill -9 $PPID
fi
