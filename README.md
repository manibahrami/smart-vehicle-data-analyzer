# Smart Vehicle Data Analyzer 

This project is a Python-based tool designed to analyze vehicle sensor data and detect potential issues using historical logs.

The main goal of this project is not real-time ECU communication, but **data analysis and system behavior inspection**, similar to how diagnostic tools analyze exported vehicle logs.

## What does this project do?

- Loads vehicle sensor data from CSV files
- Cleans and processes raw data
- Analyzes battery voltage behavior
- Detects abnormal voltage drops
- Generates a simple diagnostic summary

## Why this project?

Direct OBD-II communication is not always available, especially on older or proprietary vehicle systems.  
This project focuses on **post-processing vehicle data**, which is a realistic and widely used approach in automotive diagnostics and data analysis.

## Technologies used

- Python
- Pandas
- Object-Oriented Programming (OOP)

## Project structure

smart-vehicle-data-analyzer/
├── data/
├── analyzer.py
├── main.py
├── requirements.txt
└── README.md


## How to run

1. Install dependencies:

2. Run the project:

## Example use cases

- Analyzing vehicle logs
- Detecting battery-related issues
- Learning automotive data analysis concepts
- Practicing real-world Python projects

## Notes

This project is designed as a learning and portfolio project and can be extended with:
- Data visualization
- More sensors (RPM, speed, temperature)
- GUI or web interface




