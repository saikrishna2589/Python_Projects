import polars as pl
from mpmath.libmp import round_up

file_loc = 'files/sales.csv'

#read data
df = pl.read_csv(file_loc)


#fill na with avg
avg_sales = round(df['sales'].mean(),0)
avg_profit = round(df['profit'].mean(),0)


#replace null with mean
df_cleaned = df.with_columns([pl.col('sales').fill_null(avg_sales) ,
                              pl.col('profit').fill_null(avg_profit)])
#comparision to avg sales
df_comparision_sales = df_cleaned.with_columns([
    (pl.col('sales') - avg_sales).alias('sales_comp_to_avg')
])

print(df_comparision_sales)

#extract month column
df_moded = df_comparision_sales.with_columns(pl.col('order_date')
                                             .str.slice(5,2)
                                             .cast(pl.Int32).alias('month'))
print(df_moded)

#create pivot and calculate avg sales by month

df_avg_sales_by_month = df_moded.group_by('month').agg(pl.col('sales')
                                                       .mean().alias('avg_sales_by_month'))
print(df_avg_sales_by_month)