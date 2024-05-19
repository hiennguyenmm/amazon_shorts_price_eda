from src.extract import extraction
from src.variables import text_box_id
import duckdb
import altair as alt

text_box_input = "booty shorts"
website = "https://www.amazon.com/"

data_crawling = extraction()
data_crawling.run_web_browser(website)
data_crawling.search_item(text_box_id, text_box_input)
data_crawling.html_response()
data_crawling.parse_dataframe()
data_crawling.close_browser()

df = data_crawling.output_df


df = duckdb.query(
    """
select item_name,
             cast(replace(price,'$','') as float) as price,
             cast(replace(no_of_ratings,',','') as integer) as no_of_ratings,
             bought_last_month
              from df 
where item_name is not null
             """
).to_df()
df.count()

alt.Chart(df).mark_bar().encode(x="price", y="count()")
alt.Chart(df).mark_point().encode(x="price", y="no_of_ratings")
alt.Chart(df).mark_boxplot().encode(x="price", y="no_of_ratings")
