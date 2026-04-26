import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def generate_dummy_data():
    time_steps = np.arange(0, 200, 0.1)
    load = np.sin(time_steps) + np.sin(time_steps * 2) + np.random.normal(scale=0.1, size=len(time_steps))
    df = pd.DataFrame({'Load': load})
    return df

def prepare_data(df, seq_length=60):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df['Load'].values.reshape(-1, 1))
    
    X = []
    y = []
    for i in range(len(scaled_data) - seq_length):
        X.append(scaled_data[i:(i + seq_length)])
        y.append(scaled_data[i + seq_length])
        
    X = np.array(X)
    y = np.array(y)
    
    train_size = int(len(X) * 0.8)
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    print(f"Train shapes: X={X_train.shape}, y={y_train.shape}")
    print(f"Test shapes:  X={X_test.shape}, y={y_test.shape}")
    
    return X_train, X_test, y_train, y_test, scaler
