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

### Lesson Reflection

**Summary of Lesson:**
In this lesson, we covered the basics of using Pandas, which is a popular Python data analysis library. We learned:
* How to create Pandas data frames and series, which are core data structures for manipulation
* Approaches for loading data into data frames from sources like CSVs or Excel files
* Exporting data from Pandas to formats like CSV for use in other applications
* Using descriptive statistics and sorting for initial exploratory data analysis

**3 Top Key Points:**
* Pandas has data frames (tables) and series (single columns)
* You can load external data or manually create Pandas data structures
* Exploratory analysis helps summarize and understand data before analysis

**5 Reflection Questions:**
* What real-world use cases can you think of where Pandas would be helpful for working with data?
* When might you prefer using a Pandas series versus a data frame?
* What sources of data could you load into Pandas for your own analysis?
* What exploratory techniques do you think could be helpful for summarizing a dataset?
* How would exporting Pandas data to CSV or Excel formats be useful?

**5 Challenge Exercises:**
* Load a JSON or Excel dataset into a Pandas data frame.
* Try sorting a data frame based on a column value like date or price.
* Filter a data frame to remove rows with missing values.
* Plot a histogram of a numeric column like sales totals.
* Practice exporting filtered or sorted data to a CSV file.



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

### Lesson Reflection

**Summary of Lesson:**
In this lesson, we dived deeper into manipulating Pandas DataFrames. We learned techniques like selecting columns, filtering rows, text replacements, applying custom functions, visualization, and more. These skills allow us to wrangle messy datasets into the exact format we need for analysis.

**3 Key Points:**
* Queries filter DataFrame rows based on conditions
* Functions transform DataFrame values element-wise
* Plots visualize DataFrame data graphically

**5 Reflection Questions:**
* What DataFrame operations do you think could be useful for cleaning your own data?
* When might replacing text values help prepare data for machine learning models?
* How could visualization reveal insights during exploratory data analysis?
* What custom functions might you apply to transform financial or sales dataset values?
* In what situations might complex Boolean filtering queries be necessary?

**5 Challenge Exercises:**
* Load a dataset and practice subsetting columns and filtering rows with different criteria.
* Try splitting a text column on a delimiter and extracting partial strings.
* Define a custom function that flags outlier data points in a DataFrame.
* Create histograms, scatter plots, or other relevant graphs to visualize the distribution of columns.
* Compose a multi-condition query to filter a DataFrame for top customer sales by region.


# Numpy

## Key Terms 1
* **Array:** Primary data structure in NumPy, represented as homogeneous n-dimensional grid of values.
* **Reshape:** Transform an array into a new shape with same number of elements.
* **Ravel:** Flatten an array into one dimensional shape.
* **Stack:** Vertically or horizontally concatenate arrays.
* **Slice:** Extract subset of array elements using indexing.

```python
import numpy as np

# Create array
arr = np.array([1, 2, 3]) 
print(arr)

# Reshape 
arr = arr.reshape(1, 3)
print(arr)  

# Ravel (flatten)
flattened = arr.ravel() 

# Stack vertically  
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
stacked = np.vstack([arr1, arr2])  

# Slice
sliced = arr[0:2]
```

### Lesson Reflection

**Summary of Lesson:**
In this lesson, we learned the basics of using NumPy, which excels at numerical and scientific computing. We covered:
* Creating arrays from lists or built-in functions
* Array operations like reshaping, splitting, slicing, stacking
* Applying math functions and conditions element-wise
* Leveraging optimized NumPy performance vs regular Python

**3 Key Points:**
* Arrays are n-dimensional data structures
* Math functions apply element-wise
* Operations preserve array dimensions

**5 Reflection Questions:**
* What types of numerical or scientific data would be suitable for NumPy arrays?
* When might you need to reshape or flatten arrays for analysis?
* How could stacking arrays vertically or horizontally be useful?
* What real-world calculations could leverage element-wise operations?
* Why is NumPy performance faster than native Python for math operations?

**5 Challenge Exercises:**
* Try splitting a 2D array into rows and columns with np.split().
* Reshape an array from long 1D into a square matrix.
* Create random arrays and compare performance with Python loops vs NumPy.
* Slice array rows/columns to isolate subsets for analysis.
* Stack multiple arrays and summarize statistics on the result.