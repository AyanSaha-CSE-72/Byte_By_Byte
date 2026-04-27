from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def build_and_train_lstm(X_train, y_train, X_test, y_test):
    # ২. LSTM মডেল তৈরি (Building the LSTM Model)
    model = Sequential()

    # প্রথম LSTM লেয়ার
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(0.2)) # ওভারফিটিং রোধ করার জন্য Dropout দেওয়া হয়

    # দ্বিতীয় LSTM লেয়ার
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))

    # আউটপুট লেয়ার
    model.add(Dense(units=1))

    # মডেল কম্পাইল করা
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.summary()

    # ৩. মডেল ট্রেইনিং (Model Training)
    print("Training started...")
    model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))
    print("Training completed!")
    
    return model
