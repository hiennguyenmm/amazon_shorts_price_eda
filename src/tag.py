import yaml
from pathlib import Path


class TagObject:
    """Store class"""

    itemname_class: str
    price_class: str
    no_of_ratings_class: str
    ratings_class: str
    bought_last_month_class: str

    def __init__(self, file: Path):
        with open(file, "r") as yamlfile:
            self._from_yaml = yaml.load(yamlfile, Loader=yaml.FullLoader)

        yaml_config = self._from_yaml["output_class"]

        self.itemname_class = yaml_config["itemname_class"]
        self.price_class = yaml_config["price_class"]
        self.no_of_ratings_class = yaml_config["no_of_ratings_class"]
        self.ratings_class = yaml_config["ratings_class"]
        self.bought_last_month_class = yaml_config["bought_last_month_class"]
