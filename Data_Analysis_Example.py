import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import sqlite3

# NUMPY EXERCISES

np.zeros(10)

np.arange(10, 50)

np.ones([3, 2], dtype=np.float)

x = np.arange(4, dtype=np.int)
np.ones_like(x) * 7

np.ones([4, 4], dtype=np.int) * 5

np.identity(3)

np.random.randint(10, size=3)

np.random.randn(3, 3, 3)

x = [1, 2, 3]
y = np.array(x)

x = np.array([1, 2, 3], dtype=int)
y = np.copy(x)

np.arange(9).reshape(3, 3)

print("%d bytes" % (x.size * x.itemsize))

x = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
x[1:-1, 1:-1]

np.array(x, np.float)

x + 5

x <= 0

mask = x > 5
x[mask]

mask = x > x.mean()
x[mask]

mask = x > 5 | x < 19 & x == 13
x[mask]

x.any()
x.mean()
x.std()
x.sum()
x.sum(axis=0)
x.sum(axis=1)
x.max()

# PANDA SERIES EXERCISES

pd.Series()

x = [1, 2, 3]
x = pd.Series(x)

x.name = 'Example Name'

x.values

x = pd.Series([1, 2, 3])
index_names = ['first', 'second', 'third']
x.index = index_names

x[0]
x.iloc[0]
x['first']

pd.Series(x, dtype=np.float)

x = x.sort_values()

x + 5

mask = x > x.mean()
x[mask]

x.all()
x.any()
x.sum()
x.mean()
x.max()

# PANDAS DATAFRAME

pd.DataFrame(data=[None],
             index=[None],
             columns=[None])

marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]
marvel_df = pd.DataFrame(data=marvel_data)

column_names = ['name', 'gender', 'first_appearance']
marvel_df.columns = column_names

marvel_df.index = marvel_df['name']

marvel_df = marvel_df.drop(['name'], axis=1)
marvel_df = marvel_df.drop(['Namor', 'Hank Pym'], axis=0)

marvel_df.iloc[:5, ]
marvel_df.iloc[-5:, ].gender.to_frame()

marvel_df.loc['Vision', 'first_appearance'] = 1964
marvel_df['years_since'] = 2018 - marvel_df['first_appearance']

mask = (marvel_df['gender'] == 'female') & (marvel_df['first_appearance'] > 1970)
marvel_df[mask]

marvel_df.describe()
marvel_df.first_appearance.mean()
marvel_df.first_appearance.min()

marvel_df = marvel_df.reset_index()
marvel_df.first_appearance.plot()

pd.read_csv(
    'filename',
    header=None,
    names=['Timestamp', 'Price'],
    index_col=0,
    parse_dates=True
)

# Missing Data
x = pd.dataframe({'A': [1, 2, 3, 4, 5]})

pd.isnull(np.nan)
pd.isnull(None)

pd.notnull(np.nan)
pd.notnull(pd.Series([1, np.nan, 7]))

pd.notnull(x).sum()
pd.notnull(x).count()

x.dropna() # Any row with a single NAN values
x.dropna(how='all')
x.dropna(how='any')

x.fillna(0)
x.fillna(method='ffill')
x.fillna(method='bfill')
x.fillna(method='ffil', axis=1)

df['A'].unique()
x.duplicated() # Keeps first
x.duplicated(keep='last')
x.drop_duplicates() # Keeps first
x.drop_duplicates(keep='last')
x.duplicated(subset=['Name'])

df['Data'].str.split('_')
df['Data'].str.split('_', expand=True)

# Matplotlib

plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Spectral')
plt.colorbar()
plt.show()

plt.hist(values, bins)
plt.bar(np.arange(len(y)), y, width=barWidth, color='#00b894')
plt.boxplot()
# Global API

plt.figure(figsize=(12, 15))
plt.title('Name')
plt.plot(x, x ** 2)
plt.xlabel('x')
plt.ylabel('x ^ 2')
plt.legend('x ^ 2')
plt.subplot(1, 2, 2)

# OOP API
plot_objects = plt.subplots(nrows=2, ncols=2, figsize=(12, 6))
fig, ((ax1, ax2), (ax3, ax4)) = plot_objects
ax1.plot(np.random.randn(50), c='red', linestyle='--')

# Reading Data
with open('filename', 'r') as f:
    reader = csv.reader(f, delimiter='>')
    next(reader)
    for index, values in enumerate(header):
        if not values:
            continue
        fname, lname, age, math, french = values
        print(f'{fname} {lname} (age {age}) got {mark} in class')

csv_url = 'https://name.csv'
pd.read_csv(csv_url).head()
pd.to_csv('file.csv')

connection = sqlite3.connect('filename.db')
df = pd.read_sql('SELECT * FROM employees;', connection,
                 index_col='EmployeeId',
                 parse_dates=['BirthDate', 'HireDate'])
df.to_sql('name', connection)

html_string = 'https://'
dfs = pd.read_html(html_string)
len(dfs) # Check if correct table

pd.read_excel('name.xlsx')
pd.to_excel('name.xlsx')