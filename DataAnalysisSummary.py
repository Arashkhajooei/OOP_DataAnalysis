from Data_Processor import DataProcessor
from EDA_class import ExploratoryDataAnalysis
from Data_loader import DataLoader

class DataAnalysisSummary:
    def __init__(self, data_processor, eda):
        self.data_processor = data_processor
        self.eda = eda

    def summary_statistics(self):
        print("\nStep 4.1: Summary Statistics")
        print(self.data_processor.data.describe())

    def category_wise_analysis(self):
        print("\nStep 4.2: Category-wise Analysis")
        category_counts = self.data_processor.data['category'].value_counts()
        print(category_counts)

    def city_wise_analysis(self):
        print("\nStep 4.3: City-wise Analysis")
        city_counts = self.data_processor.data['city'].value_counts()
        print(city_counts)

    def status_wise_analysis(self):
        print("\nStep 4.4: Status-wise Analysis")
        status_counts = self.data_processor.data['status'].value_counts()
        print(status_counts)

    def cancellation_reasons_analysis(self):
        print("\nStep 4.5: Cancellation Reasons Analysis")
        cancelled_by_counts = self.data_processor.data['cancelled_by'].value_counts()
        print(cancelled_by_counts)

    def price_and_distance_analysis(self):
        print("\nStep 4.6: Price and Distance Analysis")
        print("Average Price:", self.data_processor.data['price'].mean())
        print("Maximum Price:", self.data_processor.data['price'].max())
        print("Minimum Price:", self.data_processor.data['price'].min())
        print("Average Distance:", self.data_processor.data['distance'].mean())
        print("Maximum Distance:", self.data_processor.data['distance'].max())
        print("Minimum Distance:", self.data_processor.data['distance'].min())

data_loader = DataLoader('dataset_orders.csv')
data_processor = DataProcessor(data_loader)
data_processor.load_data()
data_processor.clean_data()
data_processor.preprocess_data()

eda = ExploratoryDataAnalysis(data_processor)
eda.analyze_numerical_variables()
eda.analyze_categorical_variables()
eda.analyze_categorical_pie_charts()

data_analysis_summary = DataAnalysisSummary(data_processor, eda)
data_analysis_summary.summary_statistics()
data_analysis_summary.category_wise_analysis()
data_analysis_summary.city_wise_analysis()
data_analysis_summary.status_wise_analysis()
data_analysis_summary.cancellation_reasons_analysis()
data_analysis_summary.price_and_distance_analysis()
