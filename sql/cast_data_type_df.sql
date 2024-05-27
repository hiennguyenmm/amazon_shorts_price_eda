select
    item_name,
    cast(replace(price, '$', '') as float) as price,
    cast(replace(no_of_ratings, ',', '') as integer) as no_of_ratings,
    cast(replace(ratings, ' out of 5 stars', '') as float) as ratings,
    case
        when bought_last_month not like '% bought in past month' then null
        else cast(replace(bought_last_month, '+ bought in past month', '') as integer)
    end as bought_last_month
from
    df
where
    item_name is not null