#!/usr/bin/env python3
"""
Cybersecurity Asset Inventory System
Week 01 Mini Project

A simple CLI-based asset inventory for cybersecurity administrators.
Data is stored in data/assets.json.
"""

import argparse
import ipaddress
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "assets.json"

ASSET_TYPES = {"Workstation", "Server", "Router", "Switch", "Application"}
RISK_LEVELS = {"Low", "Medium", "High", "Critical"}
SECURITY_STATUSES = {"Secure", "Warning", "Vulnerable"}

REQUIRED_FIELDS = [
    "asset_id", "asset_name", "asset_type", "ip_address",
    "operating_system", "department", "risk_level", "security_status"
]


def load_assets() -> List[Dict[str, Any]]:
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        DATA_FILE.write_text("[]", encoding="utf-8")
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {DATA_FILE}: {exc}") from exc
    if not isinstance(data, list):
        raise ValueError("assets.json must contain a JSON array.")
    return data


def save_assets(assets: List[Dict[str, Any]]) -> None:
    DATA_FILE.write_text(
        json.dumps(assets, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )


def validate_asset(asset: Dict[str, Any], existing_assets: Optional[List[Dict[str, Any]]] = None,
                   updating_id: Optional[str] = None) -> None:
    for field in REQUIRED_FIELDS:
        value = asset.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field} cannot be empty.")

    if not re.fullmatch(r"A\d{3,}", asset["asset_id"].strip()):
        raise ValueError("Asset ID must follow the format A001, A002, A101, etc.")

    try:
        ipaddress.ip_address(asset["ip_address"].strip())
    except ValueError as exc:
        raise ValueError("IP Address must be a valid IPv4 or IPv6 address.") from exc

    if asset["asset_type"] not in ASSET_TYPES:
        raise ValueError(f"Asset Type must be one of: {', '.join(sorted(ASSET_TYPES))}.")
    if asset["risk_level"] not in RISK_LEVELS:
        raise ValueError(f"Risk Level must be one of: {', '.join(['Low','Medium','High','Critical'])}.")
    if asset["security_status"] not in SECURITY_STATUSES:
        raise ValueError("Security Status must be one of: Secure, Warning, Vulnerable.")

    if existing_assets is not None:
        for item in existing_assets:
            if item["asset_id"] == asset["asset_id"] and item["asset_id"] != updating_id:
                raise ValueError(f"Asset ID {asset['asset_id']} already exists.")


def add_asset(asset: Dict[str, Any]) -> None:
    assets = load_assets()
    validate_asset(asset, assets)
    assets.append(asset)
    save_assets(assets)


def display_assets(assets: List[Dict[str, Any]]) -> str:
    lines = [
        "=" * 55,
        "             CYBERSECURITY ASSET INVENTORY",
        "=" * 55,
    ]
    if not assets:
        lines.append("No assets found.")
    else:
        for asset in assets:
            lines.extend([
                f"Asset ID     : {asset['asset_id']}",
                f"Asset Name   : {asset['asset_name']}",
                f"Asset Type   : {asset['asset_type']}",
                f"IP Address   : {asset['ip_address']}",
                f"OS           : {asset['operating_system']}",
                f"Department   : {asset['department']}",
                f"Risk Level   : {asset['risk_level']}",
                f"Status       : {asset['security_status']}",
                "-" * 55,
            ])
    summary = summarize(assets)
    lines.extend([
        "=" * 55,
        f"Total Assets       : {summary['total']}",
        f"Critical Assets    : {summary['critical']}",
        f"High Risk Assets   : {summary['high']}",
        f"Medium Risk Assets : {summary['medium']}",
        f"Vulnerable Assets  : {summary['vulnerable']}",
        "=" * 55,
    ])
    return "\n".join(lines)


def summarize(assets: List[Dict[str, Any]]) -> Dict[str, int]:
    return {
        "total": len(assets),
        "critical": sum(a["risk_level"] == "Critical" for a in assets),
        "high": sum(a["risk_level"] == "High" for a in assets),
        "medium": sum(a["risk_level"] == "Medium" for a in assets),
        "vulnerable": sum(a["security_status"] == "Vulnerable" for a in assets),
    }


def search_assets(term: str) -> List[Dict[str, Any]]:
    term = term.lower()
    return [
        asset for asset in load_assets()
        if any(term in str(value).lower() for value in asset.values())
    ]


def update_asset(asset_id: str, changes: Dict[str, Any]) -> Dict[str, Any]:
    assets = load_assets()
    for asset in assets:
        if asset["asset_id"] == asset_id:
            updated = {**asset, **changes}
            validate_asset(updated, assets, updating_id=asset_id)
            asset.update(changes)
            save_assets(assets)
            return asset
    raise KeyError(f"Asset {asset_id} not found.")


def delete_asset(asset_id: str) -> Dict[str, Any]:
    assets = load_assets()
    for index, asset in enumerate(assets):
        if asset["asset_id"] == asset_id:
            removed = assets.pop(index)
            save_assets(assets)
            return removed
    raise KeyError(f"Asset {asset_id} not found.")


def interactive_add() -> None:
    print("\nAdd New Asset")
    fields = [
        ("asset_id", "Asset ID"),
        ("asset_name", "Asset Name"),
        ("asset_type", "Asset Type"),
        ("ip_address", "IP Address"),
        ("operating_system", "Operating System"),
        ("department", "Owner/Department"),
        ("risk_level", "Risk Level"),
        ("security_status", "Security Status"),
    ]
    asset = {key: input(f"{label}: ").strip() for key, label in fields}
    try:
        add_asset(asset)
        print("Asset added successfully.")
    except ValueError as exc:
        print(f"Validation Error: {exc}")


def interactive_update() -> None:
    asset_id = input("Enter Asset ID to update: ").strip()
    assets = load_assets()
    current = next((a for a in assets if a["asset_id"] == asset_id), None)
    if not current:
        print(f"Asset {asset_id} not found.")
        return

    print("Press Enter to keep the current value.")
    labels = {
        "asset_name": "Asset Name", "asset_type": "Asset Type",
        "ip_address": "IP Address", "operating_system": "Operating System",
        "department": "Owner/Department", "risk_level": "Risk Level",
        "security_status": "Security Status"
    }
    changes = {}
    for key, label in labels.items():
        value = input(f"{label} [{current[key]}]: ").strip()
        if value:
            changes[key] = value

    try:
        update_asset(asset_id, changes)
        print("Asset updated successfully.")
    except (ValueError, KeyError) as exc:
        print(f"Error: {exc}")


def interactive_delete() -> None:
    asset_id = input("Enter Asset ID to delete: ").strip()
    try:
        removed = delete_asset(asset_id)
        print(f"Deleted asset: {removed['asset_name']} ({removed['asset_id']})")
    except KeyError as exc:
        print(f"Error: {exc}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Cybersecurity Asset Inventory System")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("display", help="Display all assets")
    sub.add_parser("add", help="Interactively add an asset")
    sub.add_parser("update", help="Interactively update an asset")
    sub.add_parser("delete", help="Delete an asset")
    search_parser = sub.add_parser("search", help="Search assets")
    search_parser.add_argument("term", help="Search term")

    args = parser.parse_args()

    try:
        if args.command == "display":
            print(display_assets(load_assets()))
        elif args.command == "add":
            interactive_add()
        elif args.command == "update":
            interactive_update()
        elif args.command == "delete":
            interactive_delete()
        elif args.command == "search":
            results = search_assets(args.term)
            print(display_assets(results))
        else:
            parser.print_help()
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
