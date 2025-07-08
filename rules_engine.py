def apply_rules(df):
    print("⚙️ Applying underwriting rules...")

    def decision(row):
        if row['Previously_Insured'] == 1:
            return "Accept - Already Insured"
        elif row['Vehicle_Damage'] == "No":
            return "Reject - No Prior Vehicle Damage"
        else:
            return "Accept"

    df["Underwriting_Decision"] = df.apply(decision, axis=1)
    return df
