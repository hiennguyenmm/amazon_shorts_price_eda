import pandas as pd
import altair as alt
import duckdb
from src.misc import format_sql
from pyprojroot import here

df = pd.read_csv("data.csv")
df = duckdb.query(format_sql(here("./sql/cast_data_type_df.sql"))).to_df()

# summarize data
# 56 items have price, number of ratings and ratings
# bought last month is not always available

df.describe()
alt.Chart(
    df.melt(id_vars="item_name"), title="KDE 4 variables of interest"
).mark_line().transform_density(
    "value",
    groupby=["variable"],
    as_=["value", "density"],
).encode(
    x="value:Q", y="density:Q"
).facet(
    "variable:N", columns=2
).resolve_scale(
    y="independent", x="independent"
)

# check correlation between price, no_of_ratings and ratings
# using pearson and spearman
# the variables do not have correlations with each other

df[["price", "no_of_ratings", "ratings"]].corr("pearson")
df[["price", "no_of_ratings", "ratings", "bought_last_month"]].corr("spearman")

alt.Chart(df).mark_circle().encode(
    alt.X(alt.repeat("column"), type="quantitative"),
    alt.Y(alt.repeat("row"), type="quantitative"),
).properties(width=150, height=150).repeat(
    row=["price", "no_of_ratings", "ratings", "bought_last_month"],
    column=["price", "no_of_ratings", "ratings", "bought_last_month"],
)
