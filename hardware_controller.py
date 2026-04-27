import time
import random
from pin_mapping_config import HARDWARE_CONFIG

# ==============================================================================
# HARDWARE INTERFACES SIMULATION
# বাস্তব জগতে লাইব্রেরি যেমন: RPi.GPIO, pymodbus, spidev ব্যাবহার করতে হবে।
# ==============================================================================

class AnalogSensors:
    """ CT/PT Sensors for real-time electrical measurement """
    def __init__(self):
        self.pins = HARDWARE_CONFIG["CT_PT_SENSORS"]
        
    def read_voltages(self):
        # 11kV system (simulated as scaled down ADC values)
        v_a = round(random.uniform(10.8, 11.2), 2)
        v_b = round(random.uniform(10.8, 11.2), 2)
        v_c = round(random.uniform(10.8, 11.2), 2)
        print(f"[{self.pins['V_A_PIN']}, {self.pins['V_B_PIN']}, {self.pins['V_C_PIN']}] ADC Read - Voltages(kV): A={v_a}, B={v_b}, C={v_c}")
        return [v_a, v_b, v_c]

    def read_currents(self):
        # Current in Amperes
        i_a = round(random.uniform(200, 250), 2)
        i_b = round(random.uniform(200, 250), 2)
        i_c = round(random.uniform(200, 250), 2)
        print(f"[{self.pins['I_A_PIN']}, {self.pins['I_B_PIN']}, {self.pins['I_C_PIN']}] ADC Read - Currents(A): A={i_a}, B={i_b}, C={i_c}")
        return [i_a, i_b, i_c]


class SmartEnergyMeter:
    """ RS485 Modbus RTU Communication for Smart Meters & PQ Sensors """
    def __init__(self):
        self.port = HARDWARE_CONFIG["SMART_METERS"]["PORT"]
        self.baudrate = HARDWARE_CONFIG["SMART_METERS"]["BAUDRATE"]
        self.slave_id = HARDWARE_CONFIG["SMART_METERS"]["METER_ID_1"]

    def read_power_data(self):
        print(f"[Modbus RS485 on {self.port} | ID: {self.slave_id}] Fetching Real-time Power & Energy Data...")
        active_power = round(random.uniform(4.5, 4.9), 2) # MW
        frequency = round(random.uniform(49.8, 50.2), 2)  # Hz
        return {"ActivePower_MW": active_power, "Frequency_Hz": frequency}


class ProtectionRelay:
    """ GPIO Control for SEL-351A / ABB RET670 Protection Relay """
    def __init__(self):
        self.trip_pin = HARDWARE_CONFIG["PROTECTION_RELAY"]["TRIP_SIGNAL_PIN"]
        self.fault_pin = HARDWARE_CONFIG["PROTECTION_RELAY"]["FAULT_STATUS_PIN"]

    def check_fault_status(self):
        # Digital Input (HIGH/LOW)
        fault_detected = random.choice([False, False, False, False, True]) # 20% chance of fault for simulation
        status = "HIGH (FAULT)" if fault_detected else "LOW (NORMAL)"
        print(f"[GPIO IN - {self.fault_pin}] Reading Relay Status: {status}")
        return fault_detected

    def trigger_trip(self):
        # Digital Output
        print(f"[GPIO OUT - {self.trip_pin}] !!! SENDING TRIP SIGNAL TO CIRCUIT BREAKER !!!")
        print(">> CIRCUIT OPENED. SYSTEM PREVENTED FROM DAMAGE.")


class NetworkDevices:
    """ PMU, SCADA, AI Server Communication via Ethernet / IEC 61850 """
    def __init__(self):
        self.config = HARDWARE_CONFIG["NETWORK_DEVICES"]

    def send_to_ai_server(self, data):
        print(f"[Ethernet -> {self.config['AI_SERVER_IP']}] Sending 5MVA Grid Data to AI Server over IEC 61850...")
        time.sleep(0.5)
        print(f"   --> Data Uploaded Successfully.")

