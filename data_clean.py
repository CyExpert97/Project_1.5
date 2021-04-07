#%%
import pandas as pd 
df = pd.read_csv("data_test_2.csv")
#%%
print(set(df["Role of champion"]))
#%%
df.drop([94],inplace=True)
# %%
df["Role of champion"].replace(
    to_replace=['role-top', 'role-jungle', 'role-support', 'role-mid', 'role-bot'],
    value=[1, 2, 5, 3, 4],
    inplace=True
)
print(set(df["Role of champion"]))

df = pd.get_dummies(df, columns=["Role of champion"], drop_first=True)
df.head()
# %%
df.head()
# %%
df.dtypes
#%%
df["AS ratio"] = df["AS ratio"].fillna(1)
print(set(df["AS ratio"]))
# %%
df.head()
# %%
df["AS ratio"].astype(float)
df.dtypes
# %%
df["Win rate of champion"] = df["Win rate of champion"].str.rstrip('%').astype('float') / 100.0
df.dtypes
# %%
df["Ban rate of champion"] = df["Ban rate of champion"].str.rstrip('%').astype('float') / 100.0
df["Pick rate of champion"] = df["Pick rate of champion"].str.rstrip('%').astype('float') / 100.0
df.head()
# %%
df["Base AS"] = df["Base AS"].astype("float")
df.dtypes
# %%
df.dtypes
# %%
df[["Role of champion_role-jungle", "Role of champion_role-mid", "Role of champion_role-support", "Role of champion_role-top","Win rate of champion","Pick rate of champion", "Move. speed", "Attack range", "Base AS", "AS ratio"]].to_csv("regression_data.csv")
# %%
# New data clean
df["Health"] = df["Health"].str.replace("–", " ", regex=True)
new = df["Health"].str.split("   ", n=1, expand=True)
df["Min_Health"] = new[0]
df["Max_Health"] = new[1]
df["Min_Health"] = df["Min_Health"].astype('float')
df["Max_Health"] = df["Max_Health"].astype('float')
df.drop(columns =["Health"], inplace = True)
df.info()
# %%
df["Health regen."] = df["Health regen."].str.replace("–", " ", regex=True)
new = df["Health regen."].str.split("   ", n=1, expand=True)
df["Min_Health_regen"] = new[0]
df["Max_Health_regen"] = new[1]
df["Min_Health_regen"] = df["Min_Health_regen"].astype('float')
df["Max_Health_regen"] = df["Max_Health_regen"].astype('float')
df.drop(columns =["Health regen."], inplace = True)
df.info()
# %%
df["Armor"] = df["Armor"].str.replace("–", " ", regex=True)
new = df["Armor"].str.split("   ", n=1, expand=True)
df["Min_Armor"] = new[0]
df["Max_Armor"] = new[1]
df["Min_Armor"] = df["Min_Armor"].astype('float')
df["Max_Armor"] = df["Max_Armor"].astype('float')
df.drop(columns =["Armor"], inplace = True)
df['Max_Armor'] = df['Max_Armor'].fillna(df["Min_Armor"])
df.info()
# %%
df.head()
# %%
df["Magic resist."] = df["Magic resist."].str.replace("–", " ", regex=True)
new = df["Magic resist."].str.split("   ", n=1, expand=True)
df["Min_Magic_resist"] = new[0]
df["Max_Magic_resist"] = new[1]
df["Min_Magic_resist"] = df["Min_Magic_resist"].astype('float')
df["Max_Magic_resist"] = df["Max_Magic_resist"].astype('float')
df.drop(columns =["Magic resist."], inplace = True)
df['Max_Magic_resist'] = df['Max_Magic_resist'].fillna(df["Min_Magic_resist"])
df.info()

# %%
df["Attack damage"] = df["Attack damage"].str.replace("–", " ", regex=True)
new = df["Attack damage"].str.split("   ", n=1, expand=True)
df["Min_Attack_damage"] = new[0]
df["Max_Attack_damage"] = new[1]
df["Min_Attack_damage"] = df["Min_Attack_damage"].astype('float')
df["Max_Attack_damage"] = df["Max_Attack_damage"].astype('float')
df.drop(columns =["Attack damage"], inplace = True)
df['Max_Attack_damage'] = df['Max_Attack_damage'].fillna(df["Min_Attack_damage"])
df.info()
# %%
df[["Role of champion_role-jungle", "Role of champion_role-mid", "Role of champion_role-support", "Role of champion_role-top","Win rate of champion","Pick rate of champion", "Move. speed", "Attack range", "Base AS", "AS ratio", "Min_Health", "Max_Health", "Min_Health_regen", "Max_Health_regen", "Min_Armor","Max_Armor","Min_Magic_resist","Max_Magic_resist", "Min_Attack_damage", "Max_Attack_damage"]].to_csv("new_regression_data.csv")
# %%
