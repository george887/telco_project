import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from acquire import get_telco_data
import warnings
warnings.filterwarnings("ignore")

def prepare_telco(df):
    # Switching gender column to read male. Keeping track of male and female
    df.rename(columns={'gender': 'male'}, inplace=True)
    
    # Making males have a value of 1 and females 0
    df['male'] = df['male'].replace("Male", 1)
    df['male'] = df['male'].replace("Female", 0) 
   
    # Switching partner column to read partners. 
    df.rename(columns={'partner': 'partners'}, inplace=True)
   
    # Partners have a value yes/no 1/0.
    df['partners'] = df['partners'].replace("Yes", 1)
    df['partners'] = df['partners'].replace("No", 0)  
   
    # Dependents column to read yes/no 1/0.
    df['dependents'] = df['dependents'].replace("Yes", 1)
    df['dependents'] = df['dependents'].replace("No", 0)
    
    # phone_service column to read yes/no 1/0.
    df['phone_service'] = df['phone_service'].replace("Yes", 1)
    df['phone_service'] = df['phone_service'].replace("No", 0)
    
    # multiple_lines adding no phone service as no for multiple lines
    df["multiple_lines"] = df["multiple_lines"].replace("No phone service", "No")
   
    # Now making into yes/no 1/0
    df.multiple_lines = df.multiple_lines.replace("Yes", 1)
    df.multiple_lines = df.multiple_lines.replace("No", 0)
   
    # online_security into yes/no 1/0
    df["online_security"] = df["online_security"].replace("No internet service", "No")
    df.online_security = df.online_security.replace("Yes", 1)
    df.online_security = df.online_security.replace("No", 0)

    # Had to convert No internet service to No, then online_backup into yes/no 1/0.
    df["online_backup"] = df["online_backup"].replace("No internet service", "No")
    df.online_backup = df.online_backup.replace("Yes", 1)
    df.online_backup = df.online_backup.replace("No", 0)

    # Had to convert No internet service to No, then device_protection into yes/no 1/0.
    df["device_protection"] = df["device_protection"].replace("No internet service", "No")
    df.device_protection = df.device_protection.replace("Yes", 1)
    df.device_protection = df.device_protection.replace("No", 0)

    # Had to convert No internet service to No, then tech_support into yes/no 1/0.
    df["tech_support"] = df["tech_support"].replace("No internet service", "No")
    df.tech_support = df.tech_support.replace("Yes", 1)
    df.tech_support = df.tech_support.replace("No", 0)

    # Had to convert No internet service to No, then streaming_tv into yes/no 1/0.
    df["streaming_tv"] = df["streaming_tv"].replace("No internet service", "No")
    df.streaming_tv = df.streaming_tv.replace("Yes", 1)
    df.streaming_tv = df.streaming_tv.replace("No", 0)

    # Had to convert No internet service to No, then streaming_movies into yes/no 1/0.
    df["streaming_movies"] = df["streaming_movies"].replace("No internet service", "No")
    df.streaming_movies = df.streaming_movies.replace("Yes", 1)
    df.streaming_movies = df.streaming_movies.replace("No", 0)

    # Total charges showed 11 entries with $0 having no tenure. Going to make $0 to retain them
    df.total_charges = df.total_charges.where((df.tenure != 0), 0)
    
    # Was getting error as the 0 values where inputed as strings. Changed them to floats
    df['total_charges'] = df.total_charges.astype(float)
    
    # Churn into yes/no 1/0
    df.churn = df.churn.replace("Yes", 1)
    df.churn = df.churn.replace("No", 0)
    
    # Dropping cotract_type and renaming contract_type_id to cotract_type. 1 = Month-to-Month, 2 = 1 yr, 3 = 2 yr
    df = df.drop("contract_type", axis=1)
    df = df.rename(columns={'contract_type_id':'contract_type'})
    df = df.loc[:,~df.columns.duplicated()]
    df['contract_type'] = df.contract_type.astype(float)
   
    # Dropping internet_service_type and renaming internet_service_type_id to internet_service_type. 
    # 1 = DSL, 2 = Fiber Optic yr, 3 = None
    df = df.drop("internet_service_type", axis=1)
    df = df.rename(columns={'internet_service_type_id':'internet_service_type'})
    
    # paperless_billing into yes/no 1/0
    df.paperless_billing = df.paperless_billing.replace("Yes", 1)
    df.paperless_billing = df.paperless_billing.replace("No", 0)

    # Creating tenure in years
    df['tenure_years'] = round(df.tenure / 12, 2)
    
     # splitting the data into train, test and validate
    train_validate, test = train_test_split(df, test_size = .20, random_state = 123)
    train, validate = train_test_split(train_validate, test_size = .30, random_state = 123)
    return train, validate, test

def prepare_telco_all(df):
    # Switching gender column to read male. Keeping track of male and female
    df.rename(columns={'gender': 'male'}, inplace=True)
    
    # Making males have a value of 1 and females 0
    df['male'] = df['male'].replace("Male", 1)
    df['male'] = df['male'].replace("Female", 0) 

    # Switching partner column to read partners. 
    df.rename(columns={'partner': 'partners'}, inplace=True)

    # Partners have a value yes/no 1/0.
    df['partners'] = df['partners'].replace("Yes", 1)
    df['partners'] = df['partners'].replace("No", 0)  

    # Dependents column to read yes/no 1/0.
    df['dependents'] = df['dependents'].replace("Yes", 1)
    df['dependents'] = df['dependents'].replace("No", 0)
    
    # phone_service column to read yes/no 1/0.
    df['phone_service'] = df['phone_service'].replace("Yes", 1)
    df['phone_service'] = df['phone_service'].replace("No", 0)
    
    # multiple_lines adding no phone service as no for multiple lines
    df["multiple_lines"] = df["multiple_lines"].replace("No phone service", "No")

    # Now making into yes/no 1/0
    df.multiple_lines = df.multiple_lines.replace("Yes", 1)
    df.multiple_lines = df.multiple_lines.replace("No", 0)

    # online_security into yes/no 1/0
    df["online_security"] = df["online_security"].replace("No internet service", "No")
    df.online_security = df.online_security.replace("Yes", 1)
    df.online_security = df.online_security.replace("No", 0)

    # Had to convert No internet service to No, then online_backup into yes/no 1/0.
    df["online_backup"] = df["online_backup"].replace("No internet service", "No")
    df.online_backup = df.online_backup.replace("Yes", 1)
    df.online_backup = df.online_backup.replace("No", 0)

    # Had to convert No internet service to No, then device_protection into yes/no 1/0.
    df["device_protection"] = df["device_protection"].replace("No internet service", "No")
    df.device_protection = df.device_protection.replace("Yes", 1)
    df.device_protection = df.device_protection.replace("No", 0)

    # Had to convert No internet service to No, then tech_support into yes/no 1/0.
    df["tech_support"] = df["tech_support"].replace("No internet service", "No")
    df.tech_support = df.tech_support.replace("Yes", 1)
    df.tech_support = df.tech_support.replace("No", 0)

    # Had to convert No internet service to No, then streaming_tv into yes/no 1/0.
    df["streaming_tv"] = df["streaming_tv"].replace("No internet service", "No")
    df.streaming_tv = df.streaming_tv.replace("Yes", 1)
    df.streaming_tv = df.streaming_tv.replace("No", 0)

    # Had to convert No internet service to No, then streaming_movies into yes/no 1/0.
    df["streaming_movies"] = df["streaming_movies"].replace("No internet service", "No")
    df.streaming_movies = df.streaming_movies.replace("Yes", 1)
    df.streaming_movies = df.streaming_movies.replace("No", 0)

    # Total charges showed 11 entries with $0 having no tenure. Going to make $0 to retain them
    df.total_charges = df.total_charges.where((df.tenure != 0), 0)
    
    # Was getting error as the 0 values where inputed as strings. Changed them to floats
    df['total_charges'] = df.total_charges.astype(float)
    
    # Churn into yes/no 1/0
    df.churn = df.churn.replace("Yes", 1)
    df.churn = df.churn.replace("No", 0)
    
    # Dropping cotract_type and renaming contract_type_id to cotract_type. 1 = Month-to-Month, 2 = 1 yr, 3 = 2 yr
    #df = df.drop("contract_type", axis=1)
    #df = df.rename(columns={'contract_type_id':'contract_type'})
    #df = df.loc[:,~df.columns.duplicated()]
    service_dum = pd.get_dummies(df.contract_type)
    df = pd.concat([df, service_dum], axis = 1)
    df.rename(columns = {'Month-to-month': 'month_to_month', 'One year': 'one_year', 'Two year': 'two_year'})
    df['contract_type'] = df.contract_type.astype(float)

    # Dropping internet_service_type and renaming internet_service_type_id to internet_service_type. 
    # 1 = DSL, 2 = Fiber Optic yr, 3 = None
    df = df.drop("internet_service_type", axis=1)
    df = df.rename(columns={'internet_service_type_id':'internet_service_type'})
    
    # paperless_billing into yes/no 1/0
    df.paperless_billing = df.paperless_billing.replace("Yes", 1)
    df.paperless_billing = df.paperless_billing.replace("No", 0)

    # Creating tenure in years
    df['tenure_years'] = round(df.tenure / 12, 2)
    
    # splitting the data into train, test and validate
    #train_validate, test = train_test_split(df, test_size = .20, random_state = 123)
    #train, validate = train_test_split(train_validate, test_size = .30, random_state = 123)
    return df
