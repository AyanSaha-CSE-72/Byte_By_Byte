import sys
import os
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_preparation import generate_dummy_data, prepare_data
from lstm_model import build_and_train_lstm
from advanced_modules import GridFormingInverterAI, RLMicrogridController, RiskAssessmentModule, CarbonEmissionOptimizer, ResilienceEnhancer
from regional_architecture import ZeroCarbonRegion, BulkGenerationRegion, BulkConsumptionRegion, MicrogridRegion
from intelligent_systems import IntelligentMonitoringAndFaultDetection, IntelligentOperationSystem, IntelligentControlAndEnergyManagement

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

    # Init regions
    zero_carbon = ZeroCarbonRegion()
    bulk_gen = BulkGenerationRegion()
    bulk_cons = BulkConsumptionRegion()
    microgrid = MicrogridRegion()
    
    # Init Systems
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

def main():
    print("1. Preparing Data...")
    df = generate_dummy_data()
    X_train, X_test, y_train, y_test, scaler = prepare_data(df)
    
    print("\n2. Building and Training LSTM Model...")
    model = build_and_train_lstm(X_train, y_train, X_test, y_test)
    
    print("\n3. Evaluating predictions...")
    predictions = model.predict(X_test)
    
    print("\n4. Running Architecture Simulation...")
    run_master_grid_simulation(predictions)
    
    # প্রেডিক্ট করা ডাটাকে আবার আগের স্কেলে ফিরিয়ে আনা
    predictions_inverse = scaler.inverse_transform(predictions)
    y_test_inverse = scaler.inverse_transform(y_test.reshape(-1, 1))
    
    # ফলাফলের ভিজ্যুয়ালাইজেশন
    plt.figure(figsize=(12, 6))
    plt.plot(y_test_inverse, label='Actual Load', color='blue')
    plt.plot(predictions_inverse, label='Predicted Load', color='red', alpha=0.7)
    plt.title('Load Forecasting & Smart Grid Operation')
    plt.xlabel('Time')
    plt.ylabel('Power Load')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
