import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# ১. ডাটা লোডিং এবং প্রস্তুতি (Data Loading & Preparation)
# বি.দ্র: এখানে ডামি ডাটা (Sine wave + Noise) ব্যবহার করা হয়েছে। 
# আসল কাজ করার সময় pd.read_csv('your_data.csv') ব্যবহার করে আসল ডাটাসেট লোড করতে হবে।
def generate_dummy_data():
    time_steps = np.arange(0, 200, 0.1)
    # একটি কাল্পনিক এনার্জি লোড প্যাটার্ন তৈরি করা হলো
    load = np.sin(time_steps) + np.sin(time_steps * 2) + np.random.normal(scale=0.1, size=len(time_steps))
    df = pd.DataFrame({'Load': load})
    return df

df = generate_dummy_data()

# ডাটা ভিজ্যুয়ালাইজেশন
plt.figure(figsize=(12, 5))
plt.plot(df['Load'][:500])
plt.title('Simulated Power Load Data')
plt.xlabel('Time Steps')
plt.ylabel('Load')
plt.show()

# ডাটা স্কেলিং (LSTM মডেলে ডাটা স্কেলিং করা খুব জরুরি)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df['Load'].values.reshape(-1, 1))

# সিকোয়েন্স তৈরি করা (Sequence Generation)
def create_sequences(data, seq_length):
    X = []
    y = []
    for i in range(len(data) - seq_length):
        X.append(data[i:(i + seq_length)])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

SEQ_LENGTH = 60 # অতীত ৬০টি ডাটা পয়েন্ট দেখে ভবিষ্যৎ প্রেডিক্ট করবে
X, y = create_sequences(scaled_data, SEQ_LENGTH)

# ট্রেইন এবং টেস্ট সেটে ভাগ করা (80% Train, 20% Test)
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

print(f"Train shapes: X={X_train.shape}, y={y_train.shape}")
print(f"Test shapes:  X={X_test.shape}, y={y_test.shape}")


# ২. LSTM মডেল তৈরি (Building the LSTM Model)
model = Sequential()

# প্রথম LSTM লেয়ার
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2)) # ওভারফিটিং রোধ করার জন্য Dropout দেওয়া হয়

# দ্বিতীয় LSTM লেয়ার
model.add(LSTM(units=50, return_sequences=False))
model.add(Dropout(0.2))

# আউটপুট লেয়ার
model.add(Dense(units=1)) # যেহেতু আমরা একটি ভ্যালু (লোড) প্রেডিক্ট করব

# মডেল কম্পাইল করা
model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()


# ৩. মডেল ট্রেইনিং (Model Training)
print("Training started...")
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))
print("Training completed!")


# --- NEW ADVANCED AI MICROGRID MODULES ---

class GridFormingInverterAI:
    """ 1. Grid-Forming Inverter Intelligence """
    def __init__(self):
        self.virtual_inertia = 0.8
        
    def support_stability(self, frequency_deviation):
        # AI based Virtual inertia support
        if abs(frequency_deviation) > 0.05:
            print("[Inverter] Injecting virtual inertia for stability without synchronous generator.")
            return True
        return False

class RLMicrogridController:
    """ 2. Reinforcement Learning Control """
    def __init__(self):
        self.policy = "Initial Policy"
        
    def learn_and_optimize(self, state, reward):
        # Learns optimal control policy over time
        print(f"[RL Agent] Learning... State: {state}, Reward: {reward}")
        # In a real scenario, stable-baselines3 or custom RL agents go here
        
class RiskAssessmentModule:
    """ 3. Real-Time Risk Assessment """
    def check_blackout_probability(self, load_forecast, capacity):
        margin = capacity - load_forecast
        prob = max(0.0, 1.0 - (margin / capacity))
        print(f"[Risk] Blackout Probability: {prob*100:.2f}% | Voltage collapse check: {'Safe' if prob < 0.8 else 'WARNING'}")
        return prob

class CarbonEmissionOptimizer:
    """ 4. Carbon Emission Optimization """
    def dispatch_schedule(self, solar_forecast, load_forecast):
        # Emission-aware dispatch scheduling
        fossil_gen_needed = max(0, load_forecast - solar_forecast)
        print(f"[Emission] Fossil generation needed: {fossil_gen_needed:.2f}kW. Scheduling optimized low-carbon dispatch.")
        return fossil_gen_needed

class ResilienceEnhancer:
    """ 5. Resilience Enhancement """
    def predict_storm_impact(self, weather_data):
        if weather_data == 'Storm':
            print("[Resilience] Storm detected! Entering disaster-prepared microgrid mode. Reserving battery capacity.")
            return 'ISLANDED_MODE'
        return 'GRID_CONNECTED'

# --- REGIONAL AND SYSTEM ARCHITECTURE (From Diagram) ---

class ZeroCarbonRegion:
    def generate(self):
         print("[Zero Carbon Region] Generating renewable energy (Solar/Wind).")
         return 120.0

class BulkGenerationRegion:
    def generate(self):
         print("[Bulk Generation] Generating baseline bulk power (Nuclear/Fossil).")
         return 500.0

class BulkConsumptionRegion:
    def consume(self):
         print("[Bulk Consumption] City/Industrial heavy power consumption.")
         return 450.0

class MicrogridRegion:
    def operate(self):
         print("[Microgrid Region] Managing local PV arrays and CESS (Energy Storage).")
         return 20.0

class IntelligentMonitoringAndFaultDetection:
    def monitor(self, region_data):
        print(f"[IMFD System] Monitoring system state. Total net flow: {region_data:.2f} MW. No faults detected.")

class IntelligentOperationSystem:
    def process_data(self, data):
        print(f"[IOS Network] Processing deep learning analytics on regional data metrics.")
        return data * 0.95

class IntelligentControlAndEnergyManagement:
    def manage(self, inverter, rl, risk, carbon, resilience, load):
        print("[ICEMS] Coordinating AI sub-modules for Energy Management...")
        
        # 1. Resilience Check
        mode = resilience.predict_storm_impact('Clear')
        
        # 2. Risk Assessment
        risk.check_blackout_probability(load, capacity=1.5)
        
        # 3. Carbon Optimization
        carbon.dispatch_schedule(solar_forecast=0.5, load_forecast=load)
        
        # 4. Inverter Intelligence
        inverter.support_stability(frequency_deviation=0.06)
        
        # 5. RL Control update
        rl.learn_and_optimize(state="High Demand", reward=10)


# integrating them into a master Smart Energy Grid
def run_master_grid_simulation(predicted_load):
    print("\n" + "="*50)
    print("   RUNNING SMART GRID AI ARCHITECTURE SIMULATION   ")
    print("="*50)
    
    # Init sub-modules
    inverter = GridFormingInverterAI()
    rl_controller = RLMicrogridController()
    risk_module = RiskAssessmentModule()
    carbon_optimizer = CarbonEmissionOptimizer()
    resilience_module = ResilienceEnhancer()

    # Init regions & systems
    zero_carbon = ZeroCarbonRegion()
    bulk_gen = BulkGenerationRegion()
    bulk_cons = BulkConsumptionRegion()
    microgrid = MicrogridRegion()
    
    imfd = IntelligentMonitoringAndFaultDetection()
    ios = IntelligentOperationSystem()
    icems = IntelligentControlAndEnergyManagement()
    
    # 1. Energy Flow & Data Acquisition from Regions
    gen_zc = zero_carbon.generate()
    gen_bg = bulk_gen.generate()
    cons_bc = bulk_cons.consume()
    mg_state = microgrid.operate()
    
    net_flow = gen_zc + gen_bg - cons_bc + mg_state
    
    # 2. Intelligent Systems Processing
    imfd.monitor(net_flow)
    ios.process_data(net_flow)
    
    # 3. Intelligent Control based on predicted load
    latest_load = predicted_load[-1][0]
    icems.manage(inverter, rl_controller, risk_module, carbon_optimizer, resilience_module, latest_load)
    
    print("="*50 + "\n")

# ৪. প্রেডিকশন এবং ফলাফল মূল্যায়ন (Prediction and Evaluation)
print("Evaluating predictions...")
predictions = model.predict(X_test)

# Run the master grid architecture simulation using the LSTM prediction
run_master_grid_simulation(predictions)

# প্রেডিক্ট করা ডাটাকে আবার আগের স্কেলে ফিরিয়ে আনা
predictions_inverse = scaler.inverse_transform(predictions)
y_test_inverse = scaler.inverse_transform(y_test)

# ফলাফলের ভিজ্যুয়ালাইজেশন
plt.figure(figsize=(12, 6))
plt.plot(y_test_inverse, label='Actual Load', color='blue')
plt.plot(predictions_inverse, label='Predicted Load', color='red', alpha=0.7)
plt.title('Load Forecasting & Smart Grid Operation')
plt.xlabel('Time')
plt.ylabel('Power Load')
plt.legend()
plt.show()
