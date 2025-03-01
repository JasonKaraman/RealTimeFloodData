REAL-TIME HYPERLOCAL FLOOD DATA PIPELINE

A fully automated pipeline for collecting, validating, and storing real-time hyperlocal flood data from NOAA, USGS, Twitter (X), and GIS flood zones into PostgreSQL. Useful for collecting and storing data regarding street-level flooding events. This can be useful for building out flood prediction models at the hyperlocal level. This was developed to measure flood events in Charleston, SC but can be applied to anywhere locally.

FEATURES

✅ Automated Data Collection – Runs every 30 minutes

✅ Data Validation – Ensures correct formatting before insertion

✅ PostgreSQL Integration – Stores data efficiently for easy retrieval

✅ Modular Python Code – Well-structured and scalable


PROJECT STRUCTURE

/RealTimeFloodData

│── insert_data.py          # Processes & inserts data into PostgreSQL

│── flood_validation.py     # Validates CSV structure before inserting

│── run_every_30_minutes.sh # Automates execution every 30 minutes

│── README.md               # Documentation


INSTALLATION AND SETUP

1. CLONE REPOSITORY

git clone https://github.com/JasonKaraman/RealTimeFloodData.git

cd RealTimeFloodData

2. SAVE GIS FLOOD ZONES LOCALLY

Ensure `/home/ubuntu/data/gis_flood_zones_YYYY-MM-DD.csv` is populated before running the script.  

If missing, download GIS flood zones from official sources or generate the required CSV format.


3. INSTALL DEPENDENCIES

pip install -r requirements.txt


4. RUN SCRIPT MANUALLY

python3 insert_data.py


5. AUTOMATE SCAN EVERY 30 MINUTES WITH CRON JOBS

crontab -e

Then add this line at the end:

*/30 * * * * /usr/bin/python3 /home/ubuntu/insert_data.py >> /home/ubuntu/logs.txt 2>&1


HOW IT WORKS

Data Collection – The script ingests real-time flood data from NOAA, USGS, Twitter, and GIS sources.

Validation – flood_validation.py ensures only correctly structured data is inserted.

Database Insertion – insert_data.py processes and inserts valid data into PostgreSQL.

Automation – The run_every_30_minutes.sh script ensures continuous execution via cron jobs.


CONTRIBUTING

Feel free to fork this repository, submit issues, or make pull requests! Contributions are welcome.


LICENSE

This project is licensed under the MIT License.


