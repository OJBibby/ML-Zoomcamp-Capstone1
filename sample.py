import pandas as pd

# Original Base.csv dataset was larger than github allows, with 1 million entries and a size of over 200mb.

df = pd.read_csv('Base.csv')
neg_samp = df[df['fraud_bool']==0].sample(n=11029, random_state=42)
pos_samp = df[df['fraud_bool']==1]
df_sample = pd.concat([neg_samp, pos_samp], ignore_index=True, sort=False)
df_sample.to_csv("Data.csv", index=False)