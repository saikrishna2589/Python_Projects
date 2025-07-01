import polars as pl
# steps
#1. read data
#2. replace null column values with resp. means
#3. add column temp - temp(mean)
#4. add month column (numeric)
#5. group the avg temp. by month

file_loc = 'files/weather.csv'

df = pl.read_csv(file_loc)

print(df.head())
avg_temp =  round(df['temperature'].mean(),1)
avg_humidity = round(df['humidity'].mean(),1)
avg_windspeed = round(df['wind_speed'].mean(),1)

df_clean = df.with_columns(
    [pl.col('temperature').fill_null(avg_temp),
     pl.col('humidity').fill_null(avg_humidity),
    pl.col('wind_speed').fill_null(avg_windspeed)])

#add column temp-temp(mean)

df_clean_add_col = df_clean.with_columns((pl.col('temperature')-avg_temp)
                                         .alias('diff_from_avg'))

print(df_clean_add_col)


# add month column
df_add_month = df_clean_add_col.with_columns(pl.col('date')
                                             .str.slice(5,2)
                                             .cast(pl.Int32).alias('month'))

#avg temp by month

df_avg_temp_by_month = df_add_month.group_by('month').agg(pl.col('temperature').mean())
print(df_avg_temp_by_month)

