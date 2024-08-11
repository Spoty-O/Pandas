import pandas

df = pandas.read_csv('cats_dataset.csv')
# all_cats = df.count()["Breed"]
# breed = df['Breed'].value_counts()
# birman_cats = breed['Birman']
# dervon_rex_cats = breed['Devon Rex']
# birman_percent = birman_cats / all_cats * 100
# dervon_percent = dervon_rex_cats / all_cats * 100
# print(birman_percent)
# print(dervon_percent)
# print(birman_percent + dervon_percent)
temp = df[df["Gender"] == "Female"].groupby(by=["Breed"])['Weight (kg)'].agg(['min', 'max', 'mean'])
print(temp)