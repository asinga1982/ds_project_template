import pandas as pd
import seaborn as sns

df = pd.read_csv("E:\\git_new.git\\ds_project_template\data\\raw\\Train_Tickets.csv")
sns.lineplot(y=df.Count, x=df.Datetime)