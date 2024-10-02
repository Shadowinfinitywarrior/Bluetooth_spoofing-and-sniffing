import subprocess
import asyncio
from bleak import BleakScanner
import sys
import os
import platform

def spoof_bluetooth_mac(mac_address):
    """Spoofs the Bluetooth MAC address."""
    if platform.system() == "Linux":
        try:
            print(f"[INFO] Changing Bluetooth MAC address to {mac_address}...")
            subprocess.run(["sudo", "hciconfig", "hci0", "down"])
            subprocess.run(["sudo", "bdaddr", "-i", "hci0", mac_address])
            subprocess.run(["sudo", "hciconfig", "hci0", "up"])
            print(f"[SUCCESS] Bluetooth MAC address changed to {mac_address}")
        except Exception as e:
            print(f"[ERROR] Failed to change MAC address: {e}")
    elif platform.system() == "Windows":
        print("[ERROR] MAC address spoofing is not supported on Windows.")
    else:
        print("[ERROR] Unsupported platform for MAC address spoofing.")

def sniff_bluetooth_traffic():
    """Starts sniffing Bluetooth traffic using hcidump."""
    if platform.system() == "Linux":
        try:
            print("[INFO] Starting Bluetooth sniffing...")
            subprocess.run(["sudo", "hcidump", "-i", "hci0", "--raw"])
        except Exception as e:
            print(f"[ERROR] Failed to start sniffing: {e}")
    elif platform.system() == "Windows":
        print("[ERROR] Sniffing Bluetooth traffic is not supported on Windows.")
    else:
        print("[ERROR] Unsupported platform for Bluetooth sniffing.")

async def scan_nearby_ble_devices():
    """Scans for nearby Bluetooth Low Energy (BLE) devices using Bleak."""
    print("[INFO] Scanning for Bluetooth Low Energy (BLE) devices...")
    devices = await BleakScanner.discover()

    if not devices:
        print("[INFO] No devices found.")
    else:
        print("[INFO] Found the following devices:")
        for device in devices:
            print(f"    {device.name} - {device.address}")

def scan_nearby_devices():
    """Wrapper function to call the BLE scanning function asynchronously."""
    print("[INFO] Scanning for nearby devices...")
    asyncio.run(scan_nearby_ble_devices())

def main():
    """Main function to handle user input and provide options."""
    while True:
        print("\nWelcome to the Bluetooth Spoofing & Sniffing Tool")
        print("Choose an option:")
        print("1. Spoof Bluetooth MAC Address")
        print("2. Sniff Bluetooth Traffic")
        print("3. Scan for Nearby Devices")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_mac = input("Enter the new MAC address (e.g., 00:11:22:33:44:55): ")
            spoof_bluetooth_mac(new_mac)
        elif choice == "2":
            sniff_bluetooth_traffic()
        elif choice == "3":
            scan_nearby_devices()
        elif choice == "4":
            print("Exiting...")
            sys.exit()
        else:
            print("[ERROR] Invalid choice, try again.")

if __name__ == "__main__":
    if platform.system() != "Windows":
        # Only check for root privileges on non-Windows systems
        if os.geteuid() != 0:
            print("[ERROR] This tool requires root privileges. Run the script with sudo.")
            sys.exit(1)
    main()
