# Data Analysis Project: Ride Sharing Data Analysis

This project focuses on performing OOP exploratory data analysis (EDA) 

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Setup](#setup)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Exploratory Data Analysis (EDA) is a critical step in understanding and extracting meaningful insights from datasets. In this project, we use Python to process, clean, and analyze ride-sharing data. We follow Object-Oriented Programming (OOP) principles and SOLID principles to create modular and organized code.

## Project Structure

The project is structured into several components:
- `data_loader.py`: Defines the DataLoader class to read data from a CSV file.
- `data_processor.py`: Defines the DataProcessor class for data cleaning and preprocessing.
- `exploratory_data_analysis.py`: Defines the ExploratoryDataAnalysis class for EDA.
- `data_analysis_summary.py`: Defines the DataAnalysisSummary class for generating summary statistics and analysis.
- `main.py`: Combines the classes to execute the data processing, EDA, and analysis steps.

## Usage

To run the project and perform the analysis:

1. Clone this repository to your local machine.
2. Install the required dependencies (see [Dependencies](#dependencies)).
3. Ensure that the `dataset_orders.csv` file is in the project directory or adjust the file path accordingly.
4. Run the `EDA_class.py` script.

## Dependencies

The project requires the following dependencies:
- pandas
- numpy
- matplotlib
- seaborn

Install the dependencies using the following command:
```sh
pip install pandas numpy matplotlib seaborn
