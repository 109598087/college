import pandas as pd

key_list = ['B']
for discipline in key_list:
    df = pd.read_csv(discipline + '_college_rule.csv')
    df = df.drop_duplicates()
    print(df)
    df.to_csv(discipline + '_college_rule.csv', index=False)
