import polars as pl
from dask.order import order

directory_loc = 'files/iris.csv'

df = pl.read_csv(directory_loc)

stats_data = df.describe()

setosa_df = df.filter(pl.col('species')=='setosa')

#mean sepal length per species

mean_sepal_length = df.group_by('species').agg(pl.col('sepal_length').mean())

print("\n mean sepal length by species:")
print(mean_sepal_length)

setosa_df.write_csv('files/setosa_iris_polars.csv')