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
