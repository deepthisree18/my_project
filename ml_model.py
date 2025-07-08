from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

def train_model(df):
    print("🧠 Training model...")

    # Encode categorical columns
    df = df.copy()
    cat_cols = ["Gender", "Vehicle_Age", "Vehicle_Damage"]
    le = LabelEncoder()
    for col in cat_cols:
        df[col] = le.fit_transform(df[col])

    # Define features and target
    X = df[["Age", "Annual_Premium", "Previously_Insured", "Vehicle_Damage", "Driving_License"]]
    y = df["Response"]

    # Split into train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Model accuracy: {acc:.2%}")

    return model
