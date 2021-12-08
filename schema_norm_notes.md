# Instructions to normalize the major dataset for the project

The dataset available at https://hifld-geoplatform.opendata.arcgis.com/datasets/geoplatform::hospitals/about/ must be normalized in the following way:

The table has 31 columns or attributes and must be broken down into:

```
hospital_data.csv 
address_data.csv     
contact_data.csv     
metadata.csv
```

hospital_data.csv must have the following attributes/columns from the main dataset:

name    
alt_name    
objectid    
id    
status     
type    
trauma    
owner    
ttl_staff    
population    
beds      
helipad    
naics_code    
naics_desc    

address_data.csv must have:    

objectid    
id    
x    
y     
address    
city    
county    
countyfips    
state    
state_id    
st_fips    
zip    
country    
latitude    
longitude    

contact_data.csv must have:

objectid    
id     
telephone    
website    

metadata.csv must have:

objectid    
id     
source     
sourcedate    
val_method    
val_date