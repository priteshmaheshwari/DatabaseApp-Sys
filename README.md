# Hospital Information System and COVID-19 Impact in 2021

Our project enables the user to explore Healthcare facilities in the United States, and provides a comparative study on the effects of the COVID-19 pandemic well into 2021. 

## Data

The major dataset can be found at https://hifld-geoplatform.opendata.arcgis.com/datasets/geoplatform::hospitals/about/    
Download it in csv format.

The supporting dataset can be found at https://github.com/Dartmouth-DAC/covid-19-hrr-mapping/tree/master/rolling-averages   
Download the us-counties-2021.csv file. 

The non-relational dataset can be found at https://data.cityofnewyork.us/Health/COVID-19-Daily-Counts-of-Cases-Hospitalizations-an/rc75-m7u3   
Download in the XML format.

These datasets (normalized) can be found at https://github.com/priteshmaheshwari/DatabaseApp-Sys/tree/submission as well.

If the link above does not work, the required information is:

### GitHub ID: priteshmaheshwari     
### Repository: DatabaseApp-Sys     
### Branch: Submission     
The data is available under ``` data ```

## Build

The first step, of course, is creating the user, and then setting up the database. Using the terminal, navigate to the  code folder, and run the following commands:

```
psql -U postgres postgres < create_user.sql
```     
And then:     
```
psql -U nyc_covid nyc_covid < schema.sql
```     

```
pip install pandas     
pip install psycopg2     
pip install tabulate     
pip install numpy     
pip install webbrowser    
pip install sqlalchemy     
pip install lxmlz     

```

## Run

Assuming the database is now set up, run the following lines, again from the code folder       

Load data: `python3 dataload.py`

And then:     

Run application: `python3 application.py`