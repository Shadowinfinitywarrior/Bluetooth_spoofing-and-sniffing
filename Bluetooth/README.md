Bluetooth Spoofing & Sniffing Tool

This Python tool allows you to spoof Bluetooth MAC addresses, sniff Bluetooth traffic, and scan for nearby devices. It supports both classic Bluetooth (for devices like mobile phones, tablets, PCs) and Bluetooth Low Energy (BLE) devices.

Features:

Spoof Bluetooth MAC Address (Linux only)
Sniff Bluetooth Traffic (Linux only)

Scan for nearby devices:
Bluetooth Low Energy (BLE) devices
Classic Bluetooth devices (such as mobile phones, tablets, PCs)

Requirements:

Windows:

Python 3.7 or higher
Bleak: for scanning BLE devices
PyBluez: for scanning classic Bluetooth devices

Linux:

Python 3.7 or higher
Bleak: for scanning BLE devices
PyBluez: for scanning classic Bluetooth devices
BlueZ tools (hcitool, hcidump, etc.) for sniffing traffic and spoofing MAC addresses.

Installation:

Clone this repository:


git clone https://github.com/your-username/bluetooth-tool.git
cd bluetooth-tool

Install the required Python packages:

For Windows:

pip install bleak pybluez

For Linux:

sudo apt-get install python3-pybluez bluez-tools
pip install bleak pybluez

Usage:

Running the Tool
Open a terminal and navigate to the directory containing the script.

Run the script:

Linux (requires root privileges):

bash
Copy code
sudo python3 bluetooth_tool.py

Windows:

python bluetooth_tool.py

Tool Options
Once the tool is running, you'll be presented with the following options:

Spoof Bluetooth MAC Address (Linux only):
Enter a new MAC address to spoof your Bluetooth device.
Sniff Bluetooth Traffic (Linux only):
Starts sniffing Bluetooth traffic using hcidump.
Scan for Nearby Devices:
Scans for both BLE devices and classic Bluetooth devices.
Exit:
Closes the tool.

Example Output:

Scanning for BLE devices:
[INFO] Scanning for Bluetooth Low Energy (BLE) devices...
[INFO] Found the following BLE devices:
    DeviceName1 - 00:11:22:33:44:55
    DeviceName2 - 66:77:88:99:AA:BB
Scanning for classic Bluetooth devices:


[INFO] Scanning for classic Bluetooth devices (phones, tablets, PCs)...
[INFO] Found the following classic Bluetooth devices:
    Phone1 - 22:33:44:55:66:77
    Tablet1 - 88:99:AA:BB:CC:DD

Notes:

MAC Address Spoofing and Traffic Sniffing: These features are only available on Linux due to platform limitations.
Windows Support: Bluetooth sniffing and MAC address spoofing are not supported on Windows.

Troubleshooting:

Permission Issues (Linux):

Ensure that you run the tool with sudo or root privileges to allow it to access Bluetooth devices.
Missing Dependencies (Linux):

Make sure the required tools like hcitool and hcidump are installed on your system.

sudo apt-get install bluez bluez-tools

Windows Classic Bluetooth Scanning:

Ensure your Bluetooth adapter is enabled and compatible with PyBluez.