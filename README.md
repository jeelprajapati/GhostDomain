<h1 align="center">
  <img src="https://img.icons8.com/ios-filled/100/ghost.png" alt="GhostDomain" width="80px">
  <br>GhostDomain
</h1>

<h4 align="center">Subdomain discovery & takeover vulnerability detection tool.</h4>

<p align="center">
  <a href="https://github.com/jeelprajapati/GhostDomain"><img src="https://img.shields.io/github/stars/jeelprajapati/GhostDomain?style=social"></a>
  <a href="https://github.com/jeelprajapati/GhostDomain/releases"><img src="https://img.shields.io/github/v/release/jeelprajapati/GhostDomain?color=blue&label=release"></a>
  <a href="https://github.com/jeelprajapati/GhostDomain/issues"><img src="https://img.shields.io/github/issues/jeelprajapati/GhostDomain?color=yellow"></a>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Install</a> •
  <a href="#usage">Usage</a> •
  <a href="#demo">Demo</a> •
  <a href="#structure">Structure</a> •
  <a href="#license">License</a>
</p>

---

GhostDomain is a Python tool that helps security researchers find subdomains of a domain and detect if any of them are vulnerable to subdomain takeover.

---

## Features

- ✅ Brute-force subdomain discovery
- ✅ CNAME and DNS resolution
- ✅ Subdomain takeover detection (via fingerprint matching)
- ✅ Clean terminal output with color and status codes
- ✅ Ctrl+C interrupt support
- ✅ Banner + version output
- ✅ Supports custom wordlists

---


## Installation

Clone the repo:
```bash
git clone https://github.com/jeelprajapati/GhostDomain.git
```

Move into the project folder:
```bash
cd GhostDomain
```

Install dependencies::
```bash
pip install -r requirements.txt
```

---


## Usage

Basic scan using default wordlist:
```bash
python main.py -d example.com
```

Scan with a custom wordlist:
```bash
python main.py -d example.com -w mysubs.txt
```

Show version:
```bash
python main.py -v
```

Show help:
```bash
python main.py -h
```

---


## Demo

```bash
 ____ _               _   ____                        _
| |  _| '_ \ / _ \/ __| __| | | |/ _ \| '_ ` _ \ / _` | | '_ \
| |_| | | | | (_) \__ \ |_| |_| | (_) | | | | | | (_| | | | | |
 \____|_| |_|\___/|___/\__|____/ \___/|_| |_| |_|\__,_|_|_| |_|


Subdomain Takeover Scanner
Version: 1.0.0 by GhostDomain 🔥


[NXDOMAIN]  Jeel.example.com - No DNS Record
```

---


## Structure

```bash
ghostDomain/
├── main.py               # Main scanner script
├── common_subs.txt       # Default wordlist
├── fingerprints.json     # Vulnerability fingerprints
├── requirements.txt      # Dependencies
└── README.md             # You're reading it!
```

---

## License

MIT License © 2025 Jeel Prajapati
