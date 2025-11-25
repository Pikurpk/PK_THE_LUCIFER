#!/data/data/com.termux/files/usr/bin/bash

# ==========================================
# Hacker Theme Installer for Termux
# By Lucifer x Foysal
# ==========================================

# Colors
GREEN="\e[1;32m"
CYAN="\e[1;36m"
RED="\e[1;31m"
RESET="\e[0m"

# ==========================================
# Loading Animation
# ==========================================
loading() {
    clear
    echo -e "\n${CYAN}Applying Hacker Theme...${RESET}\n"
    bar=""
    for i in {1..40}; do
        bar+="#"
        echo -ne "[$bar] $((i*2))% \r"
        sleep 0.04
    done
    echo -e "\n\n${GREEN}Theme Applied Successfully!${RESET}\n"
    sleep 1
}

loading


# ==========================================
# TERMUX COLOR SCHEME
# ==========================================
echo -e "${CYAN}Setting colors...${RESET}"

mkdir -p ~/.termux

cat > ~/.termux/colors.properties <<EOF
foreground=#00FF00
background=#000000
cursor=#00FF00
color0=#000000
color1=#FF0000
color2=#00FF00
color3=#FFFF00
color4=#00FFFF
color5=#FF00FF
color6=#00CCCC
color7=#FFFFFF
color8=#555555
color9=#FF5555
color10=#55FF55
color11=#FFFF55
color12=#55FFFF
color13=#FF55FF
color14=#55CCCC
color15=#FFFFFF
EOF


# ==========================================
# CUSTOM TERMUX FONT (Hacker Font)
# ==========================================
echo -e "${CYAN}Installing hacker font...${RESET}"
curl -sLO https://raw.githubusercontent.com/romkatv/powerlevel10k-media/master/MesloLGS%20NF%20Regular.ttf
mv "MesloLGS NF Regular.ttf" ~/.termux/font.ttf


# ==========================================
# CUSTOM PS1 (Hacker Prompt)
# ==========================================
echo -e "${CYAN}Applying custom hacker prompt...${RESET}"

cat >> ~/.bashrc <<'EOF'

PS1='\[\e[1;32m\][LUCIFER]\[\e[1;36m\]➤\[\e[0m\] '

EOF


# ==========================================
# EXTRA EFFECT: Green Matrix Shadow at New Terminal
# ==========================================
cat > ~/.bash_profile <<'EOF'
echo -e "\e[32m"
echo "Booting Hacker Environment..."
sleep 0.4
echo -e "\e[0m"
EOF


# ==========================================
# FINAL MESSAGE
# ==========================================
echo -e "${GREEN}INSTALL COMPLETE!"
echo -e "Restart Termux to activate the Hacker Theme.${RESET}"

termux-reload-settings
