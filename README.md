## Description

**VidGrab** is a versatile video downloader tool that allows users to download videos and playlists from various websites and social media platforms using URLs. The tool supports downloading videos in both **MP3** and **MP4** formats, with options to choose the desired quality. Additionally, VidGrab offers features such as pause and resume download functionality, progress tracking, and the ability to download live-stream videos.

---

## Features

- **Download Videos**: Download videos in both MP4 and MP3 formats.
- **Playlist Support**: Download entire playlists with ease.
- **Quality Options**: Choose from a variety of video quality options (120p, 240p, 360p, 480p, 720p, 1080p).
- **Progress Tracking**: Displays download progress with speed, percentage, and remaining time.
- **Pause & Resume**: Supports pausing and resuming downloads.
- **Cross-Platform**: Works on both **Kali Linux** and **Termux**.

---

## How to Install

### Kali Linux
1. **Install ffmpeg**:
    ```bash
    sudo apt install ffmpeg -y
    ```

2. **Clone the Repository**:
    ```bash
    git clone https://github.com/Mohamed9x60/vidgrab.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd vidgrab
    ```

3. **Install Dependencies**: Install the required Python libraries by running:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Tool**:
    ```bash
    python3 vidgrab.py
    ```

---

### Termux

1. **Update and Upgrade Termux**:
    ```bash
    pkg update && pkg upgrade
    ```

2. **Install ffmpeg**:
    ```bash
    pkg install ffmpeg -y
    ```

3. **Clone the Repository**:
    ```bash
    git clone https://github.com/Mohamed9x60/vidgrab.git
    ```

4. **Navigate to the Project Directory**:
    ```bash
    cd vidgrab
    ```

5. **Install Required Python Libraries**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Tool**:
    ```bash
    python3 vidgrab.py
    ```

---

## Usage

1. After running the tool, you'll see a menu with the following options:
   - **Download a single video**
   - **Download a playlist**
   - **Choose download format** (MP3 or MP4)
   - **Select video quality** (for MP4 downloads)

2. Follow the on-screen prompts to:
   - Enter the video or playlist URL.
   - Choose the format and quality.
   - Start the download.

---

## Credits

- **Developed by**: Mohamed Fouad
- **Message**: _Free Palestine_

---

##Explanatory video


https://github.com/user-attachments/assets/67420ba5-21f6-4283-a0eb-89c2b22c37ff



