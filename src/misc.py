import bs4
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from src.variables import page_class, output_class


def func_extract_soup(class_string, soup):
    result = [
        (
            i.find("span", attrs={"class": class_string}).get_text()
            if i.find("span", attrs={"class": class_string})
            else None
        )
        for i in soup
    ]
    return result


def next_page(chrome_options):  # FIXME
    """Navigate to next page

    Parameters
    ----------
    chrome_options : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    # chrome_options.find_element_by_xpath(By.XPATH, xpath_string).click()
    chrome_options.find_element(By.LINK_TEXT, "Next").click()
    return None


def extract_html(chrome_options) -> bs4.element.ResultSet:

    soup = BeautifulSoup(chrome_options.page_source, features="html.parser")
    response = soup.select(
        "div",
        attrs={"class": page_class},
    )[
        0
    ].findAll("div", attrs={"class": output_class})
    return response
