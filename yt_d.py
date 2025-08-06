import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import yt_dlp
import threading
import os

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        # Style
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # URL Entry
        ttk.Label(main_frame, text="YouTube URL:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.url_entry = ttk.Entry(main_frame, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Download Path
        ttk.Label(main_frame, text="Download Path:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.path_entry = ttk.Entry(main_frame, width=40)
        self.path_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.path_entry.insert(0, os.path.join(os.path.expanduser("~"), "Downloads"))
        ttk.Button(main_frame, text="Browse", command=self.browse_path).grid(row=1, column=2, padx=5, pady=5)

        # Format Selection
        ttk.Label(main_frame, text="Format:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.format_var = tk.StringVar(value="mp4")
        ttk.Radiobutton(main_frame, text="MP4", variable=self.format_var, value="mp4").grid(row=2, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(main_frame, text="MP3", variable=self.format_var, value="mp3").grid(row=2, column=1, padx=5, pady=5, sticky="e")

        # Download Button
        self.download_button = ttk.Button(main_frame, text="Download", command=self.start_download)
        self.download_button.grid(row=3, column=1, pady=10)

        # Progress Bar
        self.progress = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.grid(row=4, column=0, columnspan=3, pady=10)

        # Status Label
        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.grid(row=5, column=0, columnspan=3)

    def browse_path(self):
        directory = filedialog.askdirectory()
        if directory:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, directory)

    def start_download(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return

        self.download_button.config(state=tk.DISABLED)
        self.progress['value'] = 0
        self.status_label.config(text="Starting download...")

        download_thread = threading.Thread(target=self.download_video, args=(url,))
        download_thread.start()

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            if total_bytes:
                percentage = (d['downloaded_bytes'] / total_bytes) * 100
                self.progress['value'] = percentage
                self.status_label.config(text=f"Downloading: {int(percentage)}%")
                self.root.update_idletasks()
        elif d['status'] == 'finished':
            self.progress['value'] = 100
            self.status_label.config(text="Download finished. Processing...")
            self.root.update_idletasks()

    def download_video(self, url):
        download_path = self.path_entry.get()
        file_format = self.format_var.get()

        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'progress_hooks': [self.progress_hook],
            'noplaylist': True,
        }

        if file_format == 'mp3':
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.config(text="Download complete!")
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            self.status_label.config(text="An error occurred.")
            messagebox.showerror("Error", f"An error occurred:\n{e}")
        finally:
            self.download_button.config(state=tk.NORMAL)
            self.progress['value'] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()