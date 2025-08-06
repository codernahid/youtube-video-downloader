# Clean YouTube Downloader GUI

A sleek, simple, and efficient desktop application I built for downloading YouTube videos or extracting audio in MP3 format. It uses a clean Graphical User Interface (GUI) and is powered by the robust `yt-dlp` library.

The entire application is packaged into a single, standalone `.exe` file that runs on any Windows PC without needing any installation.

## ✨ Features

-   **Simple & Clean Interface:** No clutter. Just paste the URL and download.
-   **Video & Audio:** Download full videos as MP4 or extract audio-only as MP3.
-   **Real-time Progress:** A visual progress bar and status updates keep you informed.
-   **Standalone Executable:** No need to install Python or any libraries. Just click and run the `.exe`.
-   **Choose Your Path:** Easily browse and select where you want to save your downloads.
-   **Built for Windows:** Designed to work seamlessly as a native Windows application.

## 🚀 How to Use (For Everyone)

This is the easiest way to get started. No coding required!

1.  **Download the App:** Go to the **[Releases](https://github.com/codernahid/youtube-video-downloader)** page of this repository.
2.  **Get the `.exe`:** Download the latest `YouTubeDownloader.exe` file from the assets.
3.  **Run It:** Double-click the downloaded `.exe` file. Windows Defender might show a warning since the app is not from a recognized publisher—simply click **"More info"** and then **"Run anyway"**.
4.  **Done!** Paste a YouTube URL, choose your format (MP4/MP3), and click "Download".

## 👨‍💻 For Developers (Running & Building from Source)

If you want to run the application from the source code or modify it, follow these steps.

### Prerequisites

-   [Python 3](https://www.python.org/downloads/) installed on your system.
-   [Git](https://git-scm.com/downloads) (optional, for cloning).

### 1. Get the Source Code

Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/your-repo.git
cd [your-repo](https://github.com/codernahid/youtube-video-downloader)
2. Install Dependencies

This project relies on yt-dlp for downloading. Install it using pip:


pip install yt-dlp
3. Run the Application

Execute the Python script to launch the GUI:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
python yt_d.py

(Replace yt_d.py with the actual name of your Python file if you changed it).

🛠️ How I Built the .exe File

I used PyInstaller to package this application into a single executable. You can replicate the process easily.

1. Install PyInstaller

If you don't have it already, install PyInstaller:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
pip install pyinstaller
2. Run the Build Command

Open your terminal in the project's root directory and run the following command.


python -m PyInstaller --onefile --windowed --name "YouTubeDownloader" yt_d.py

Command Breakdown:

--onefile: Bundles everything into a single .exe file.

--windowed: Prevents the black console window from appearing when you run the app.

--name "YouTubeDownloader": Sets the name of the final executable file.

(Optional) You can add --icon="your_icon.ico" to give the app a custom icon.

3. Find Your Executable

Once the process is complete, you will find your standalone YouTubeDownloader.exe inside the newly created dist folder. You can also use the included build.bat script for a one-click build process on Windows!

💻 Technologies Used

Python: The core programming language.

Tkinter: For creating the simple and native GUI.

yt-dlp: The powerful engine for downloading video/audio content.

PyInstaller: For packaging the application into a standalone Windows executable.

🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you have any suggestions.

📄 License

This project is open-source and you are free to use and modify it.

