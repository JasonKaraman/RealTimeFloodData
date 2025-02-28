Real-Time Flood Data Pipeline
A fully automated pipeline for collecting, validating, and storing real-time hyperlocal flood data from NOAA, USGS, Twitter (X), and GIS flood zones into PostgreSQL. 
Useful for collecting and storing data regarding street-level flooding events. This can be useful for building out flood prediction models at the street level.

Features
✅ Automated Data Collection – Runs every 30 minutes
✅ Data Validation – Ensures correct formatting before insertion
✅ PostgreSQL Integration – Stores data efficiently for easy retrieval
✅ Modular Python Code – Well-structured and scalable

Project Structure
/RealTimeFloodData
│── insert_data.py          # Processes & inserts data into PostgreSQL
│── flood_validation.py     # Validates CSV structure before inserting
│── run_every_30_minutes.sh # Automates execution every 30 minutes
│── README.md               # Documentation

⚙️ Installation & Setup
Clone the Repository
git clone https://github.com/JasonKaraman/RealTimeFloodData.git
cd RealTimeFloodData

Install Dependencies
pip install -r requirements.txt

Run the Script Manually
python3 insert_data.py

Automate Execution Every 30 Minutes using cron jobs
crontab -e

Then add this line at the end:
*/30 * * * * /usr/bin/python3 /home/ubuntu/insert_data.py >> /home/ubuntu/logs.txt 2>&1

How It Works
Data Collection – The script ingests real-time flood data from NOAA, USGS, Twitter, and GIS sources.
Validation – flood_validation.py ensures only correctly structured data is inserted.
Database Insertion – insert_data.py processes and inserts valid data into PostgreSQL.
Automation – The run_every_30_minutes.sh script ensures continuous execution via cron jobs.

🤝 Contributing
Feel free to fork this repository, submit issues, or make pull requests! Contributions are welcome.

📜 License
This project is licensed under the MIT License.


