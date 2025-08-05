# System Health Monitor

System Health Monitor is a lightweight Python-based monitoring tool that tracks system resource usage (CPU, memory, and disk), logs the data to a CSV file, sends real-time alerts via Slack, and provides a live dashboard using Streamlit.

## Features

- Monitors CPU, memory, and disk usage
- Logs data with timestamps to a CSV file
- Sends alerts to Slack when CPU usage exceeds a specified threshold
- Displays a real-time dashboard for visualizing system metrics
- Fully containerized using Docker for cross-platform deployment

## Technologies Used

- Python 3
- psutil
- Streamlit
- requests
- pandas
- Docker

### Prerequisites

- Python 3.10 or higher
- pip
- Docker (optional, for containerized deployment)
