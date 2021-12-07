# Hospital Information System and COVID-19 Impact in 2021

Our project enables the user to explore Healthcare facilities in the United States, and provides a comparative study on the effects of the COVID-19 pandemic well into 2021. 

## Data

The major dataset can be found at https://hifld-geoplatform.opendata.arcgis.com/datasets/geoplatform::hospitals/about/    
Downloaded in csv format.

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

List the steps needed to build your application from the terminal. That should include the step needed to install dependencies (including your non-relational datastore).

You should also include the step needed to set up the database and configure your schema. Assume a clean Postgres install.

Example:

```
psql -U postgres postgres < create_user.sql
psql -U nyc_covid nyc_covid < schema.sql

pip install
```

## Run

Explain how to run your application from the terminal. That should include the step needed to run the code that loads the data into your database (as well as any additional step needed to load your supporting dataset(s), if you're taking the course at the graduate level). Also be clear about the entry point for your application. If you've created a web application, remember to include a link to the page hosted by your application.

Example:

Load data: `python3 code/load_data.py`

Run application: `python3 code/application.py`