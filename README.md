The purpose of this project is to support my business idea of selling booty shorts on Amazon. We aim to analyze the market prices and buying demand on the platform to gain a comprehensive understanding of the market landscape.  

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
│   ├── analysis.py    <- exploratory analysis and visualizations
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
