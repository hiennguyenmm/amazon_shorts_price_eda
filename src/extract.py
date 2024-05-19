import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.variables import (
    itemname_class,
    price_class,
    no_of_ratings_class,
    ratings_class,
    bought_last_month_class,
)
from src.misc import (
    # xpath_string,
    extract_html,
    # next_page,
    func_extract_soup,
)


# tag = TagObject(here("./shorts/tag.yaml"))


class extraction:

    output_df: pd.DataFrame

    def __init__(self, output_df: pd.DataFrame = None):
        self.output_df = output_df

    def run_web_browser(self, web_link: str, headless: bool = False):
        """Run web browser open the desired website

        Parameters
        ----------
        web_link : str
            website link needs to have https://www format
        headless : bool, optional
            if True no browser is opened, by default False

        Returns
        -------
        _type_
            _description_
        """
        option = webdriver.ChromeOptions()
        if headless:
            # run in headless mode so no browser is opened
            option.add_argument("headless")
        self.chrome_options = webdriver.Chrome(options=option)
        self.chrome_options.get(web_link)
        self.chrome_options.implicitly_wait(20)

        return None

    def search_item(self, text_box_id: str, text_box_input: str):
        """input item needs to be searched in the search box

        Parameters
        ----------
        text_box_id : str
            element id of the search box
        text_box_input : str
            item needs to be searched

        Returns
        -------
        _type_
            _description_
        """
        search_box = self.chrome_options.find_element(By.ID, text_box_id)
        search_box.send_keys(text_box_input)
        search_box.submit()

        return None

    def html_response(
        self,
    ):
        self.response = extract_html(self.chrome_options)
        # for page_click in range(3, 5): #FIXME
        #     xpath_link = xpath_string.format({"page_number": page_click})
        #     self.chrome_options = next_page(self.chrome_options, xpath_link)
        #     self.response = response
        return None

    def close_browser(self):
        self.chrome_options.close()
        return None

    def parse_dataframe(self):

        itemname = func_extract_soup(itemname_class, self.response)
        price = func_extract_soup(price_class, self.response)
        no_of_ratings = func_extract_soup(no_of_ratings_class, self.response)
        ratings = func_extract_soup(ratings_class, self.response)
        bought_last_month = func_extract_soup(
            bought_last_month_class, self.response
        )

        output_df = pd.DataFrame(
            {
                "item_name": itemname,
                "price": price,
                "no_of_ratings": no_of_ratings,
                "ratings": ratings,
                "bought_last_month": bought_last_month,
            }
        )
        self.output_df = output_df

        return None
