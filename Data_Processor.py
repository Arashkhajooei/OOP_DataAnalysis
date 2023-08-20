from Data_loader import DataLoader,DataProcessor
import pandas as pd

class DataProcessor:
    def __init__(self, data_loader):
        self.data_loader = data_loader
        self.data = None

    def load_data(self):
        self.data = self.data_loader.read_data()

    def clean_data(self):
        print("Step 3: Data Cleaning")

        # Step 3.1: Convert date columns to proper datetime format
        self.data['create_time'] = pd.to_datetime(self.data['create_time'])
        self.data['accept_time'] = pd.to_datetime(self.data['accept_time'])

        # Step 3.2: Convert 'price' and 'Distance' columns to numeric
        self.data['price'] = pd.to_numeric(self.data['price'], errors='coerce')
        self.data['distance'] = pd.to_numeric(self.data['distance'], errors='coerce')

        # Step 3.3: Handle missing values in 'biker_id'
        self.data['biker_id'].fillna('NOT_ACCEPTED', inplace=True)

        # Step 3.4: Handle missing values in 'cancelled_by'
        self.data['cancelled_by'].fillna("UNKNOWN", inplace=True)

    def preprocess_data(self):
        print("Step 4: Data Preprocessing")

        # Step 4.1: Convert text columns to lowercase
        self.data['category'] = self.data['category'].str.lower()
        self.data['city'] = self.data['city'].str.lower()
        self.data['status'] = self.data['status'].str.lower()
        self.data['cancelled_by'] = self.data['cancelled_by'].str.lower()

        # Step 4.2: Remove duplicate rows
        self.data.drop_duplicates(inplace=True)

        # Step 4.3: Convert 'order_id', 'customer_id', and 'biker_id' to integers
        self.data['order_id'] = self.data['order_id'].astype(int)
        self.data['customer_id'] = self.data['customer_id'].astype(int)

        missing_values = self.data.isnull().sum()
        print(missing_values)



data_loader = DataLoader('dataset_orders.csv')
data_processor = DataProcessor(data_loader)

data_processor.load_data()
data_processor.clean_data()
data_processor.preprocess_data()
