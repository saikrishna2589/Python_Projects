import polars as pl

file_dir ='files/cars.csv'

df = pl.read_csv(file_dir)

#analyse data
print(df.head())

#filter data for 4 cylinders

filter_df_4_cyl = df.filter(pl.col("cylinders")==4)

print(filter_df_4_cyl)

#calculate mean of the horsepower by cylinders.

mean_horsepower_by_cyl = df.group_by('cylinders').agg(pl.col('horsepower').mean())

print(mean_horsepower_by_cyl)

#export to excel for 4 cyclinders and meanhorse power info.

filter_df_4_cyl.write_csv('files/4_cyclinderdata.csv')