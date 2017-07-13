# Deep Learning CSV Cheat Sheet
A deep learning cheat sheet with Jupyter notebook examples 


## Pandas as pd
### Importing from CSV

- Documentation: [df = pd.read_csv('file-path-and-name.csv')](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)
- Usage example: 
- Full example:

### See Columns with missing values

- Documentation: [df.isnull().sum()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)
- Usage example: 
- Full example:

### Replace value 

- Documentation: [df.replace(['male', 'female'], [1, 2], inplace=True) ](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)
- Usage example: 
- Full example:

### Removing Lines / Removing Columns

- Documentation: [df = df.drop(df.columns[[0, 1, 3]], axis=1)](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.drop.html)
- Usage example: 
- Full example:

### Missing Values / Empty cells

- Documentation: [df["Age"].fillna(df["Age"].mean(), inplace=True)], axis=1)](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.drop.html)
- Usage example: 
- Full example:

### Cut / Delete Rows based on condition

- Documentation: 
- Usage example: [survive = df.drop(df[(df.Pclass > 1) | (df.Sex == 1) ].index)](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.drop.html)
- Full example:

### Labels / Truth / What to predict 

Labels are the truth in a deep learning model. If you want to predict if someone survived the Titanic with a CSV with 10 columns, such as name, ticket price, age etc. Then, the column that indicates if they survived is the label column. In this case, it is 0 if they died and 1 if they survived. [See this example on Quora.](https://www.quora.com/What-is-one-hot-encoding-and-when-is-it-used-in-data-science)

In Pandas you can use the data.get_dummies() function to turn numerical categories into binary / hot encoding / dummy representation. 

- Documentation: [data.get_dummies()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html)
- Usage example: **creating-labels.ipynb**
- Full example:

## Numpy as np

### Replace null/nan value

- Documentation: np.nan
- Usage example: [df.replace(['S', 'C', 'Q', np.nan], [1, 2, 3, 0], inplace=True) ](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)
- Full example:

## Seaborn as np

### Visulize data

- Documentation: np.nan
- Usage example: [sns.pairplot(df, hue="Survived", vars=["Age", "Pclass", "Sex"]) ](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)
- Full example:
