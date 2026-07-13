@echo off
:: ============================================
:: 🦀 CLAW-PHISH v5.0.0 - Windows Installer
:: ============================================

title CLAW-PHISH Installer
color 0C

echo ================================================
echo     🦀 CLAW-PHISH v5.0.0 - INSTALLER
echo ================================================
echo.

:: Check Python
echo [*] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] Python not found!
    echo [*] Please install Python 3.8+ from python.org
    pause
    exit /b 1
)
echo [✓] Python found

:: Check pip
echo [*] Checking pip...
pip --version >nul 2>&1
if errorlevel 1 (
    echo [X] Pip not found!
    pause
    exit /b 1
)
echo [✓] Pip found

:: Upgrade pip
echo [*] Upgrading pip...
python -m pip install --upgrade pip setuptools wheel

:: Install Python dependencies
echo [*] Installing Python dependencies...
pip install -r requirements.txt

:: Create directories
echo [*] Creating directories...
mkdir .claw_phish 2>nul
mkdir reports 2>nul
mkdir temp 2>nul

:: Create run script
echo [*] Creating run script...
(
echo @echo off
echo python claw_phish.py %%*
) > run_claw.bat

:: Create config
echo [*] Creating config file...
(
echo {
echo     "version": "5.0.0",
echo     "auto_start": false,
echo     "web": {
echo         "enabled": false,
echo         "port": 5000,
echo         "host": "0.0.0.0"
echo     },
echo     "keylogger": {
echo         "enabled": false,
echo         "hotkey": "f10"
echo     },
echo     "monitoring": {
echo         "enabled": true
echo     }
echo }
) > .claw_phish\config.json

echo.
echo ================================================
echo     🦀 CLAW-PHISH INSTALLATION COMPLETE!
echo ================================================
echo.
echo [✓] Installation successful!
echo.
echo To run: run_claw.bat
echo.
pause