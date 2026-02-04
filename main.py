from analyzer import VehicleDataAnalyzer

def main():
    analyzer = VehicleDataAnalyzer("data/sample_vehicle_data.csv")

    analyzer.clean_data()

    print("=== Vehicle Data Summary ===")
    print(analyzer.summary())

    print("\n=== Battery Analysis ===")
    battery_result = analyzer.battery_analysis()
    for key, value in battery_result.items():
        print(f"{key}: {value}")

    print("\n=== Voltage Anomalies ===")
    anomalies = analyzer.detect_anomalies()
    if anomalies.empty:
        print("No anomalies detected.")
    else:
        print(anomalies)

if __name__ == "__main__":
    main()
