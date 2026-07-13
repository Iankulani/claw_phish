# ============================================
# 🦀 CLAW-PHISH v5.0.0 - PowerShell Installer
# ============================================

Write-Host "================================================" -ForegroundColor Red
Write-Host "    🦀 CLAW-PHISH v5.0.0 - INSTALLER" -ForegroundColor Red
Write-Host "================================================" -ForegroundColor Red
Write-Host ""

# Check Python
Write-Host "[*] Checking Python..." -ForegroundColor Cyan
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[✓] $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[X] Python not found!" -ForegroundColor Red
    Write-Host "[*] Please install Python 3.8+ from python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check pip
Write-Host "[*] Checking pip..." -ForegroundColor Cyan
try {
    pip --version 2>&1 | Out-Null
    Write-Host "[✓] Pip found" -ForegroundColor Green
} catch {
    Write-Host "[X] Pip not found!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Upgrade pip
Write-Host "[*] Upgrading pip..." -ForegroundColor Cyan
python -m pip install --upgrade pip setuptools wheel

# Install dependencies
Write-Host "[*] Installing Python dependencies..." -ForegroundColor Cyan
pip install -r requirements.txt

# Create directories
Write-Host "[*] Creating directories..." -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path ".claw_phish" | Out-Null
New-Item -ItemType Directory -Force -Path "reports" | Out-Null
New-Item -ItemType Directory -Force -Path "temp" | Out-Null

# Create run script
Write-Host "[*] Creating run script..." -ForegroundColor Cyan
@"
@echo off
python claw_phish.py %*
"@ | Out-File -FilePath "run_claw.bat" -Encoding ASCII

# Create config
Write-Host "[*] Creating config..." -ForegroundColor Cyan
@"
{
    "version": "5.0.0",
    "auto_start": false,
    "web": {
        "enabled": false,
        "port": 5000,
        "host": "0.0.0.0"
    },
    "keylogger": {
        "enabled": false,
        "hotkey": "f10"
    },
    "monitoring": {
        "enabled": true
    }
}
"@ | Out-File -FilePath ".claw_phish\config.json" -Encoding UTF8

Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "    🦀 CLAW-PHISH INSTALLATION COMPLETE!" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Host "[✓] Installation successful!" -ForegroundColor Green
Write-Host ""
Write-Host "To run: .\run_claw.bat" -ForegroundColor Cyan
Write-Host ""
Read-Host "Press Enter to exit"