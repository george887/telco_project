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
    # Going to make $0 to retain them
    df.total_charges = df.total_charges.where((df.tenure != 0), 0)
    # Was getting error as the 0 values where inputed as strings. Changed them to floats
    df['total_charges'] = df.total_charges.astype(float)
    # Churn into yes/no 1/0
    df.churn = df.churn.replace("Yes", 1)
    df.churn = df.churn.replace("No", 0)
    # Dropping cotract_type and renaming contract_type_id to cotract_type. 1 = Month-to-Month, 2 = 1 yr, 3 = 2 yr
    df = df.drop("contract_type", axis=1)
    df = df.rename(columns={'contract_type_id':'contract_type'})
    # Dropping internet_service_type and renaming internet_service_type_id to internet_service_type. 
    # 1 = DSL, 2 = Fiber Optic yr, 3 = None
    df = df.drop("internet_service_type", axis=1)
    df = df.rename(columns={'internet_service_type_id':'internet_service_type'})
    # paperless_billing into yes/no 1/0
    df.paperless_billing = df.paperless_billing.replace("Yes", 1)
    df.paperless_billing = df.paperless_billing.replace("No", 0)
     # splitting the data into train, test and validate
    train_validate, test = train_test_split(df, test_size = .20, random_state = 123)
    train, validate = train_test_split(train_validate, test_size = .30, random_state = 123)
