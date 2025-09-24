# Pandas

## Key Terms 1

* **Data frame:** A two-dimensional data structure inside Pandas similar to a spreadsheet, with columns and rows.
* **Series:** A one-dimensional array with axis labels, usually created from a Pandas data frame column.
* **Loading:** The process of reading external data into a Pandas data frame.
* **Exploratory analysis:** Initial investigation of data to understand its characteristics before further analysis.
* **Exporting:** Saving data from a Pandas data frame out to another format like CSV or Excel.

```python
import pandas as pd

# Create data frame
data = [[1, 2], [3, 4]]
df = pd.DataFrame(data, columns=['Num1', 'Num2'], index=['R1', 'R2'])
print(df)

# Create series
s = df['Num1']
print(s)
```

```python
# Load CSV file into data frame
df = pd.read_csv('data.csv')

# Exploratory analysis
print(df.describe())

# Export data frame to CSV
df.to_csv('export.csv')
```

## Key Terms 2

* **Dataframe:** Tabular data structure in Pandas with labeled rows and columns.
* **Series:** Single column of labeled data in Pandas.
* **Loading:** Reading external dataset into Pandas dataframe.
* **Manipulation:** Transforming, filtering, cleaning dataframe after loading.
* **Visualization:** Creating charts and plots from dataframe data.

```python
import pandas as pd

# Create dataframe
data = [[1, 2], [3, 4]]
df = pd.DataFrame(data, columns=['Num1', 'Num2'], index=['R1', 'R2'])
print(df)

# Create series
s = df['Num1']
print(s)
```

```python
# Load CSV file into dataframe
df = pd.read_csv('data.csv')

# Filter dataframe rows
new_df = df[df['Sales'] > 1000]

# Plot histogram from dataframe
df['Sales'].plot.hist()
```
