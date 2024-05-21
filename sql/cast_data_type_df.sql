select
    item_name,
    cast(replace(price, '$', '') as float) as price,
    cast(replace(no_of_ratings, ',', '') as integer) as no_of_ratings,
    cast(replace(ratings, ' out of 5 stars', '') as float) as ratings,
    bought_last_month
from
    df
where
    item_name is not null