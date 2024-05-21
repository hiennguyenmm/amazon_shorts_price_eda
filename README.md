This project purpose is to give an overview about the price range and sellers' selling performance on Amazon on item booty shorts

**Goal**
1. Extract data from Amazon  
- [x] Connect to Amazon.com
- [x] Automatically search for 'booty shorts'
- [x] Collect html response of the current site
- [ ] Collect multiple html response by browsing next pages
2. Analyze data
- [x] Parse html response to usable data frame
- [ ] EDA
      

**Repository Structure**
```
├── README.md          
│
├── requirements.txt   
|
├── src                
│   ├── __init__.py    
│   │
│   ├── extract.py     <- crawl website and retrieve html response
│   │
│   ├── misc.py        <- helper functions
│   │
│   └── variables.py   <- constant variables for this project
|
│── sql                <- duckdb sql
│   │
│   └── cast_data_type_df.sql         
|
|── main.py           
|
│── .gitignore         
```
