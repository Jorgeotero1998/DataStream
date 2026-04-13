# DataStream

A simple and effective Python tool to scrape web data, analyze it, and generate a video report of the process.

## What it does
* **Scrapes 100+ items:** Goes through multiple pages automatically.
* **Smart Connection:** Uses different User-Agents to stay under the radar.
* **Data Cleanup:** Saves everything into a clean CSV file ready for Excel.
* **Auto Video:** Creates an MP4 video showing the robot's progress (so you don't have to record your screen).
![SCRAPPERPYTHON-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/888866e5-c7b8-4a6b-acea-962161f99497)


## How it works
The project is split into three main parts to keep the code clean:
1. **Engine (`engine.py`):** Handles the "handshake" with the website.
2. **Parser (`parser.py`):** Grabs the titles and points, then calculates the summary.
3. **Video Creator (`video_creator.py`):** Draws the progress frames and builds the video file.

## Setup
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/Jorgeotero1998/DataStream.git](https://github.com/Jorgeotero1998/DataStream.git)
   pip install -r requirements.txt
   python main.py
