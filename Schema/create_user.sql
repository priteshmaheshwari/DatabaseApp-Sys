DROP DATABASE IF EXISTS nyc_covid;

DROP SCHEMA IF EXISTS testing CASCADE;

DROP USER IF EXISTS nyc_covid;

CREATE DATABASE nyc_covid;
CREATE USER nyc_covid WITH PASSWORD 'nyc_covid';
GRANT ALL PRIVILEGES ON DATABASE nyc_covid TO nyc_covid;


CREATE SCHEMA testing;
ALTER USER admin SET search_path = testing;
GRANT ALL PRIVILEGES ON SCHEMA testing TO nyc_covid;