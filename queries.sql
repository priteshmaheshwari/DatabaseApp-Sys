-- Hospital Information according to Zip code, with Google Maps location
-- TAKE ZIP AS INPUT

SELECT h.objectid, h.id, h.name, a.address, a.city, a.county, a.state, a.zip, a.latitude, a.longitude, h.type, c.telephone, c.website
FROM hospital_data h JOIN address_data a ON h.objectid = a.objectid AND h.id = a.id
JOIN contact_data c ON h.objectid = c.objectid AND h.id = c.id
WHERE a.zip = 10035;

-- Giving all information avalable for Covid cases in a particular county and date range
-- TAKE COUNTY AND DATE RANGE AS INPUT

SELECT date, state, cases, cases_avg, cases_avg_per_100k, deaths, deaths_avg, deaths_avg_per_100k
FROM counties
WHERE LOWER(COUNTY) = 'albany' AND
DATE BETWEEN '2021-01-03' AND '2021-01-04';

-- Giving a list of all hospitals with address for a particular NAICS code and ZIP code
-- TAKE NAICS CODE AND ZIP CODE AS INPUT

SELECT DISTINCT(NAICS_CODE), NAICS_DESC
FROM hospital_data;

SELECT h.objectid, h.id, h.name, h.type, h.beds, a.address, a.city, a.county, a.state, a.zip, a.latitude, a.longitude
FROM hospital_data h JOIN address_data a ON h.objectid = a.objectid AND h.id = a.id
WHERE a.zip = 12180;

-- The date a hospital was last reviewed in a particular zip code
-- TAKE ZIP CODE AS INPUT

SELECT h.objectid, h.id, h.name, h.status, h.type, h.trauma, h.owner, h.ttl_staff, h.population, h.beds, h.helipad, m.source, m.sourcedate, m.val_method, m.val_date, a.zip
FROM hospital_data h JOIN metadata m ON h.objectid = m.objectid AND h.id = m.id JOIN address_data a ON h.objectid = a.objectid AND h.id = a.id 
-- ORDER BY a.zip;
WHERE a.zip = 12180;

-- The sum of deaths and number of hospitals in a particular county
-- TAKE COUNTY AS INPUT, AND THEN DIVIDE SUM/COUNT

SELECT SUM(c.deaths), LOWER(c.county), c.state
FROM counties c
GROUP BY c.county, c.state
HAVING LOWER(c.county) = LOWER('ALBANY')
ORDER BY c.county, c.state;

SELECT COUNT(a.id),LOWER(a.county), a.state
FROM address_data a
GROUP BY a.county, a.state
HAVING LOWER(a.county) = LOWER('ALBANY')
ORDER BY a.county, a.state;