import pandas as pd


def get_abc_list(ABC, df):
    a_list = list()
    for a in df.iloc[:, 2]:
        if ABC in a:
            a_list.append(1)
        else:
            a_list.append(0)
    return a_list


df = pd.read_csv('college.csv')

a_list = get_abc_list('A', df)
b_list = get_abc_list('B', df)

print(a_list)
print(b_list)
