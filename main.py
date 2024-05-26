from src.extract import extraction
from src.variables import text_box_id

text_box_input = "booty shorts"
website = "https://www.amazon.com/"

data_crawling = extraction()
data_crawling.run_web_browser(website)
data_crawling.search_item(text_box_id, text_box_input)
data_crawling.html_response()
data_crawling.parse_dataframe()
data_crawling.close_browser()

df = data_crawling.output_df
