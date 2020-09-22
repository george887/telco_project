import pandas as pd
from env import host, user, password
import os

# establish mysql connection
def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# Creating a function to access the telco data
def get_telco_data():
    filename = "telco.csv"
    # if a file is found with a name that matches filename (telco.csv), the function will return the data as a dataframe
    if os.path.isfile(filename):
        return pd.read_csv(filename)
        
    else:
        sql_querry = '''
                        SELECT * FROM customers AS cust
                        JOIN contract_types AS ct ON cust.contract_type_id = ct.contract_type_id
                        JOIN internet_service_types AS i_s ON cust.internet_service_type_id = i_s.internet_service_type_id
                        JOIN payment_types AS pt ON cust.payment_type_id = pt.payment_type_id;
                    '''
        df = pd.read_sql(sql_querry, get_connection('telco_churn'))
        # Create a DF with the telco data
        df.to_csv('telco_churn.csv')
        return df
