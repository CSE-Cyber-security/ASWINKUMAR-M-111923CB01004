# Test Cases

| ID | Test Case | Input / Action | Expected Result |
|---|---|---|---|
| TC-01 | Add valid asset | Add A104 with valid fields | Asset is added and stored in `data/assets.json` |
| TC-02 | Display assets | Run `python src/asset_inventory.py display` | All assets and security summary are displayed |
| TC-03 | Search asset | Search `Web-Server` or `A102` | Matching asset is displayed |
| TC-04 | Update asset | Change A103 status from Warning to Secure | Updated value is saved |
| TC-05 | Delete asset | Delete A103 | Asset is removed from the inventory |
| TC-06 | Invalid asset type | Enter `Firewall` | Validation error is shown |
| TC-07 | Invalid risk level | Enter `Extreme` | Validation error is shown |
| TC-08 | Invalid IP | Enter `999.999.1.1` | Validation error is shown |
| TC-09 | Duplicate ID | Add another asset with A101 | Duplicate-ID error is shown |
| TC-10 | Empty required field | Leave Asset Name blank | Validation error is shown |

## Manual test commands

```bash
python src/asset_inventory.py display
python src/asset_inventory.py search Web-Server
python src/asset_inventory.py add
python src/asset_inventory.py update
python src/asset_inventory.py delete
```
