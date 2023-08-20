import pandas as pd

class DataLoader:
    def __init__(self, file_path, chunk_size=10000):
        self.file_path = file_path
        self.chunk_size = chunk_size

    def read_data(self):
        data_chunks = pd.read_csv(self.file_path, chunksize=self.chunk_size)
        return pd.concat(data_chunks)

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def examine_data(self):
        print("Step 1: Data Information")
        print(self.data.info())

    def analyze_missing_values(self):
        print("\nStep 2: Missing Values")
        missing_values = self.data.isnull().sum()
        print(missing_values)

    def check_duplicates(self):
        print("\nStep 3: Data Duplication Check")
        duplicated_rows = self.data.duplicated()
        duplicated_count = duplicated_rows.sum()
        print("Number of duplicated rows:", duplicated_count)

class Application:
    def __init__(self, data_loader, data_processor):
        self.data_loader = data_loader
        self.data_processor = data_processor

    def run(self):
        data = self.data_loader.read_data()
        self.data_processor = DataProcessor(data)

        self.data_processor.examine_data()
        self.data_processor.analyze_missing_values()
        self.data_processor.check_duplicates()

# Create instances of the components
data_loader = DataLoader('dataset_orders.csv')
data_processor = DataProcessor(None)  # DataProcessor will receive data later

# Create the application and run it
app = Application(data_loader, data_processor)
app.run()
