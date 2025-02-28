#!/bin/bash
while true; do
    python3 /home/ubuntu/insert_data.py
    sleep 1800  # Wait 30 minutes before running again
done

chmod +x /home/ubuntu/run_every_30_minutes.sh
