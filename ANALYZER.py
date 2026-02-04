import pandas as pd

class VehicleDataAnalyzer:
    def __init__(self, csv_path: str):
        self.df = pd.read_csv(csv_path)

    def clean_data(self):
        #
        self.df.dropna(inplace=True)

        # 
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])

    def battery_analysis(self):
        min_voltage = self.df['battery_voltage'].min()
        max_voltage = self.df['battery_voltage'].max()
        avg_voltage = self.df['battery_voltage'].mean()

        status = "Normal"
        if min_voltage < 11.5:
            status = "Warning: Possible battery issue"

        return {
            "min_voltage": round(min_voltage, 2),
            "max_voltage": round(max_voltage, 2),
            "average_voltage": round(avg_voltage, 2),
            "status": status
        }

    def detect_anomalies(self, threshold=11.5):
        anomalies = self.df[self.df['battery_voltage'] < threshold]
        return anomalies

    def summary(self):
        return {
            "total_records": len(self.df),
            "start_time": str(self.df['timestamp'].min()),
            "end_time": str(self.df['timestamp'].max())
        }
