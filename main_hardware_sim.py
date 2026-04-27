import time
from hardware_controller import AnalogSensors, SmartEnergyMeter, ProtectionRelay, NetworkDevices

# ==============================================================================
# MAIN EDGE COMPUTING SIMULATION SCRIPT
# এই স্ক্রিপ্ট একটি Microgrid Edge Device (যেমনে Advantech/Siemens IPC) এ চলবে 
# যা সব সেন্সর থেকে ডাটা নিয়ে AI সার্ভারে পাঠায় এবং প্রয়োজনে লজিক্যালি ট্রিপ করে।
# ==============================================================================

def run_hardware_scan():
    print("="*55)
    print(" ⚡ 5MVA MICROGRID HARDWARE DATA ACQUISITION ⚡ ")
    print("="*55)
    
    # 1. Initialize component controllers
    analog_sensors = AnalogSensors()
    smart_meter = SmartEnergyMeter()
    relay = ProtectionRelay()
    network = NetworkDevices()
    
    print("\n--- Measuring Phase Voltages & Currents (CT/PT) ---")
    voltages = analog_sensors.read_voltages()
    currents = analog_sensors.read_currents()
    
    print("\n--- Reading Smart Meter & PQ Analyzer (RS485) ---")
    power_data = smart_meter.read_power_data()
    print(f"|--- Smart Meter Output: Active: {power_data['ActivePower_MW']} MW | Frequency: {power_data['Frequency_Hz']} Hz")
    
    print("\n--- Checking Protection Relays (GPIO) ---")
    fault_detected = relay.check_fault_status()
    
    if fault_detected:
        print("\n!!! WARNING: FAULT DETECTED ON GRID !!!")
        print("Executing fast-action logic on Edge controller...")
        relay.trigger_trip()
    else:
        print("\n--- Sending data to Central AI & SCADA Servers via Ethernet ---")
        payload = {
            "Voltages_kV": voltages,
            "Currents_A": currents,
            "Power_Data": power_data,
            "Fault_Status": "Healthy"
        }
        network.send_to_ai_server(payload)
        
    print("\n================ ACQUISITION CYCLE COMPLETE =================\n")

if __name__ == "__main__":
    # Simulate hardware running continuously in a real project
    for loop in range(1, 4):
        print(f"\n[ SYSTEM TICK: {loop} ]")
        run_hardware_scan()
        time.sleep(2)
