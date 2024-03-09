import pandas as pd

def modif(row):
    symptoms = row["SYMPTOMS"].replace("-", " ")
    symptoms = symptoms.replace("  ", " ")
    return symptoms

path = "../../../dataset/symptoms/csv/symptoms.csv"

df = pd.read_csv(path)

df["SYMPTOMS"] = df.apply(modif, axis=1)

print(df.head())

df.to_csv("./symptoms.csv")
