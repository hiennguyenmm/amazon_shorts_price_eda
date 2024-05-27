import pandas as pd
import altair as alt
import duckdb
from src.misc import format_sql
from pyprojroot import here

df = pd.read_csv("data.csv")
df = duckdb.query(format_sql(here("./sql/cast_data_type_df.sql"))).to_df()

# check correlation between price, no_of_ratings and ratings
# using pearson and spearman 
# the variables do not have correlations with each other

df[["price", "no_of_ratings", "ratings"]].corr('pearson')
df[["price", "bought_last_month", "ratings"]].corr('spearman')

alt.Chart(df).mark_circle().encode(
    alt.X(alt.repeat("column"), type='quantitative'),
    alt.Y(alt.repeat("row"), type='quantitative')
).properties(
    width=150,
    height=150
).repeat(
    row=['price', 'no_of_ratings', 'ratings', 'bought_last_month'],
    column=['price', 'no_of_ratings', 'ratings', 'bought_last_month']
)
