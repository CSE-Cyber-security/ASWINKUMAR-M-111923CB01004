# Week 01 – Cybersecurity Asset Inventory System

A Python-based command-line application for maintaining a cybersecurity asset inventory.

## Features

- Add IT assets
- Display all assets
- Search assets by ID, name, type, IP, OS, department, risk, or status
- Update asset details
- Delete assets
- Validate asset IDs and IP addresses
- Validate asset type, risk level, and security status
- Store inventory data in JSON
- Generate a security summary:
  - Total assets
  - Critical assets
  - High-risk assets
  - Medium-risk assets
  - Vulnerable assets

## Allowed values

### Asset Type
- Workstation
- Server
- Router
- Switch
- Application

### Risk Level
- Low
- Medium
- High
- Critical

### Security Status
- Secure
- Warning
- Vulnerable

## Repository Structure

```text
Week-01-Cybersecurity-Asset-Inventory/
├── src/
│   └── asset_inventory.py
├── data/
│   └── assets.json
├── tests/
│   └── test_cases.md
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
└── README.md
```

## Requirements

- Python 3.9 or newer
- No third-party Python packages are required.

## Run

From the repository root:

```bash
python src/asset_inventory.py display
```

Other commands:

```bash
python src/asset_inventory.py add
python src/asset_inventory.py search Web-Server
python src/asset_inventory.py update
python src/asset_inventory.py delete
```

## Example output

```text
=======================================================
             CYBERSECURITY ASSET INVENTORY
=======================================================
Asset ID     : A101
Asset Name   : HR-PC-01
Asset Type   : Workstation
IP Address   : 192.168.1.10
OS           : Windows 11
Department   : HR
Risk Level   : Medium
Status       : Secure
-------------------------------------------------------
...
Total Assets       : 3
Critical Assets    : 1
High Risk Assets   : 1
Medium Risk Assets : 1
Vulnerable Assets  : 1
=======================================================
```

## Security validation

The program checks:

1. Asset ID format such as `A101`
2. Duplicate Asset IDs
3. Valid IPv4/IPv6 addresses
4. Allowed asset types
5. Allowed risk levels
6. Allowed security statuses
7. Required fields

## GitHub upload

After creating a GitHub repository named `Week-01-Cybersecurity-Asset-Inventory`, upload this project folder or use:

```bash
git init
git add .
git commit -m "Add Week 01 cybersecurity asset inventory"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Project outcome

This mini project demonstrates basic cybersecurity asset management, input validation, CRUD operations, JSON data persistence, and security-risk summarization.
