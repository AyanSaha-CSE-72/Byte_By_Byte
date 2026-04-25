import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from assessment_planning import ExistingGridAssessment, FeasibilityPlanning
from design_deployment import MicrogridDesign, SensorCommunicationDeployment, ConventionalControlSetup
from data_collection import DataCollectionStorage
from ai_models import AIModelsDevelopment, ModelTrainingValidation
from integration_testing import AIControlIntegration, SimulationStabilityTesting
from cybersecurity_pilot import CybersecurityImplementation, PilotDeployment, PerformanceEvaluation, ScalingExpansion

def main():
    print("====================================================")
    print("   AI-BASED MICROGRID CONTROL - IMPLEMENTATION FLOW  ")
    print("====================================================\n")
    print("STARTING PIPELINE...")

    # 1. Assessment & Planning
    assesment = ExistingGridAssessment().execute()
    feasible = FeasibilityPlanning().execute(assesment)

    # 2. Design & Baseline Deployment
    design_spec = MicrogridDesign().execute()
    SensorCommunicationDeployment().execute(design_spec)
    ConventionalControlSetup().execute()

    # 3. Data layer
    historical_data = DataCollectionStorage().execute()

    # 4. AI Development & Training
    models = AIModelsDevelopment().execute()
    trained_metrics = ModelTrainingValidation().execute(historical_data, models)

    # 5. Integration & Testing
    AIControlIntegration().execute(trained_metrics)
    test_result = SimulationStabilityTesting().execute()

    # 6. Security, Deployment & Scaling
    if test_result["test_status"] == "Passed":
        CybersecurityImplementation().execute()
        PilotDeployment().execute()
        PerformanceEvaluation().execute()
        ScalingExpansion().execute()
    else:
        print("\n[!] Stability test failed. Cannot proceed to deployment.")

    print("\n================ PIPELINE FINISHED =================")

if __name__ == "__main__":
    main()
