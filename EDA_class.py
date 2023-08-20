import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Processor import DataProcessor
from Data_loader import DataLoader

class ExploratoryDataAnalysis:
    def __init__(self, data_processor):
        self.data_processor = data_processor
        self.data = self.data_processor.data

    def analyze_numerical_variables(self):
        print("Step 4: Exploratory Data Analysis (EDA) - Univariate Analysis")
        print("Step 1: Numerical Variables - Descriptive Statistics and Visualization")

        numerical_columns = ['price', 'distance']

        # Descriptive Statistics
        numerical_stats = self.data[numerical_columns].describe()
        print("Descriptive Statistics for Numerical Variables:")
        print(numerical_stats)

        # Visualization - Histograms and Box Plots
        fig, axes = plt.subplots(1, 4, figsize=(20, 5))
        fig.suptitle("Univariate Analysis of Numerical Variables", fontsize=16)

        for i, column in enumerate(numerical_columns):
            # Histogram
            axes[i].hist(self.data[column], bins=20, edgecolor='black', color='skyblue', alpha=0.7)
            axes[i].set_title(f"Histogram of {column}")
            axes[i].set_xlabel(column)
            axes[i].set_ylabel("Frequency")

            # Box Plot
            sns.boxplot(data=self.data[column], ax=axes[i + 2], orient='v', color='lightgreen')
            axes[i + 2].set_title(f"Box Plot of {column}")
            axes[i + 2].set_ylabel(column)

        plt.tight_layout()
        plt.show()

    def analyze_categorical_variables(self):
        print("\nStep 2: Categorical Variables - Frequency Distribution Visualization")
        categorical_columns = ['category', 'city', 'status', 'cancelled_by']

        # Visualization - Bar Charts
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle("Univariate Analysis of Categorical Variables", fontsize=16)

        for i, column in enumerate(categorical_columns):
            # Bar Chart
            sns.countplot(data=self.data, x=column, palette='Set3', ax=axes[i // 2, i % 2])
            axes[i // 2, i % 2].set_title(f"Frequency Distribution of {column}")
            axes[i // 2, i % 2].set_xticklabels(axes[i // 2, i % 2].get_xticklabels(), rotation=45, ha='right')
            axes[i // 2, i % 2].set_xlabel(column)
            axes[i // 2, i % 2].set_ylabel("Count")

        plt.tight_layout()
        plt.show()

    def analyze_categorical_pie_charts(self):
        print("\nStep 3: Categorical Variables - Pie Charts with Percentage in Legend")
        categorical_columns = ['category', 'city', 'status', 'cancelled_by']

        # Pie Chart with Percentage Distribution
        fig, axes = plt.subplots(1, 4, figsize=(20, 5))
        fig.suptitle("Percentage Distribution of Categorical Variables", fontsize=16)

        for i, column in enumerate(categorical_columns):
            # Pie Chart
            value_counts = self.data[column].value_counts()
            wedges, _, autotexts = axes[i].pie(value_counts, autopct='', startangle=90, colors=sns.color_palette('Set3'))
            axes[i].set_title("")  # Remove title from the pie chart

            # Calculate percentage for each category
            total_count = sum(value_counts)
            percentages = [f'{100 * count / total_count:.1f}%' for count in value_counts]

            # Legend with category names and percentage
            axes[i].legend(wedges, [f'{name} ({percentage})' for name, percentage in zip(value_counts.index, percentages)],
                           title=column, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        plt.tight_layout()
        plt.show()


data_loader = DataLoader('dataset_orders.csv')
data_processor = DataProcessor(data_loader)
data_processor.load_data()
data_processor.clean_data()
data_processor.preprocess_data()

eda = ExploratoryDataAnalysis(data_processor)
eda.analyze_numerical_variables()
eda.analyze_categorical_variables()
eda.analyze_categorical_pie_charts()
