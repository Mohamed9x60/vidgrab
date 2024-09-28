import os
import random
from pytube import YouTube
import yt_dlp as youtube_dl
import colorama
from colorama import Fore, Style, Back
import pyfiglet
import sys

# Initialize colorama
colorama.init()

class VideoDownloader:
    def __init__(self):
        self.banner_texts = [
            "Video Downloader",
            "Media Fetcher",
            "Quick Download",
            "vidgrab",
            "Mohamed"
        ]
        self.clear_screen()
        self.display_banner()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_banner(self):
        banner = pyfiglet.figlet_format(random.choice(self.banner_texts))
        print(Fore.CYAN + banner + Style.RESET_ALL)
        print(Fore.BLUE + Back.LIGHTWHITE_EX + "   Developed : Mohamed Fouad " + Style.RESET_ALL)
        print(Fore.RED + Back.LIGHTWHITE_EX + "        Free Palestine       " + Style.RESET_ALL)

    def download_video(self, url, format_choice, quality=None, output_path=None):
        try:
            if format_choice == 'MP3':
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(output_path or '.', '%(title)s.%(ext)s'),
                    'progress_hooks': [self.show_progress],
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'continue_dl': True,
                    'noplaylist': True,
                }
            else:
                ydl_opts = {
                    'format': f'bestvideo[height<={quality}]+bestaudio/best',
                    'outtmpl': os.path.join(output_path or '.', '%(title)s.%(ext)s'),
                    'progress_hooks': [self.show_progress],
                    'continue_dl': True,
                    'noplaylist': True,
                }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(Fore.GREEN + "Download completed!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)

    def download_playlist(self, url, format_choice, quality=None, output_path=None):
        try:
            if format_choice == 'MP3':
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(output_path or '.', '%(title)s.%(ext)s'),
                    'progress_hooks': [self.show_progress],
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'continue_dl': True,
                }
            else:
                ydl_opts = {
                    'format': f'bestvideo[height<={quality}]+bestaudio/best',
                    'outtmpl': os.path.join(output_path or '.', '%(title)s.%(ext)s'),
                    'progress_hooks': [self.show_progress],
                    'continue_dl': True,
                }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(Fore.GREEN + "Playlist download completed!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)

    def show_progress(self, d):
        if d['status'] == 'downloading':
            total_size = d.get('total_bytes', 0)
            downloaded_size = d.get('downloaded_bytes', 0)
            progress = downloaded_size / total_size if total_size > 0 else 0
            bar_length = 40
            arrow = '█' * int(round(bar_length * progress))
            spaces = ' ' * (bar_length - len(arrow))
            percent = round(progress * 100)
            remaining_time = d.get('eta', 0)
            speed = d.get('speed', 0) / (1024 * 1024)

            print(Fore.YELLOW + f"\r[{arrow}{spaces}] {percent}% | Speed: {speed:.2f} MB/s | ETA: {remaining_time:.0f}s" + Style.RESET_ALL, end='')
        elif d['status'] == 'finished':
            print(Fore.GREEN + "\nDownload completed!" + Style.RESET_ALL)

    def choose_format(self):
        while True:
            print(Fore.CYAN + "\nChoose the format(s) to download:" + Style.RESET_ALL)
            print(Fore.GREEN + "1. Download as MP3" + Style.RESET_ALL)
            print(Fore.BLUE + "2. Download as MP4" + Style.RESET_ALL)
            print(Fore.YELLOW + "3. Back" + Style.RESET_ALL)
            print(Fore.RED + "4. Exit" + Style.RESET_ALL)

            choice = input(Fore.CYAN + "\nEnter your choice (1, 2 to choose both): " + Style.RESET_ALL).replace(" ", "")

            if '1' in choice and '2' in choice:
                return ['MP3', 'MP4']
            elif '1' in choice:
                return ['MP3']
            elif '2' in choice:
                return ['MP4']
            elif '3' in choice:
                return 'Back'
            elif '4' in choice:
                self.farewell_message()
                sys.exit()
            else:
                print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)

    def choose_quality(self):
        while True:
            print(Fore.CYAN + "\nChoose the quality to download:" + Style.RESET_ALL)
            print(Fore.GREEN + "1. 120p" + Style.RESET_ALL)
            print(Fore.GREEN + "2. 240p" + Style.RESET_ALL)
            print(Fore.GREEN + "3. 360p" + Style.RESET_ALL)
            print(Fore.GREEN + "4. 480p" + Style.RESET_ALL)
            print(Fore.GREEN + "5. 720p" + Style.RESET_ALL)
            print(Fore.GREEN + "6. 1080p" + Style.RESET_ALL)
            print(Fore.YELLOW + "7. Back" + Style.RESET_ALL)
            print(Fore.RED + "8. Exit" + Style.RESET_ALL)

            choice = input(Fore.CYAN + "\nEnter your choice: " + Style.RESET_ALL)

            if choice == '1':
                return 120
            elif choice == '2':
                return 240
            elif choice == '3':
                return 360
            elif choice == '4':
                return 480
            elif choice == '5':
                return 720
            elif choice == '6':
                return 1080
            elif choice == '7':
                return 'Back'
            elif choice == '8':
                self.farewell_message()
                sys.exit()
            else:
                print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)

    def choose_output_path(self):
        default_path = os.getcwd()
        print(Fore.BLUE + f"\nDefault save location: {default_path}" + Style.RESET_ALL)
        output_path = input(Fore.BLUE + "Enter a custom path or press Enter to use the default: " + Style.RESET_ALL)

        if not output_path:
            return default_path
        elif not os.path.exists(output_path):
            print(Fore.RED + "Invalid path, using default location." + Style.RESET_ALL)
            return default_path
        return output_path

    def farewell_message(self):
        print(Fore.LIGHTRED_EX + Back.LIGHTWHITE_EX + "        Palestine is Free      " + Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX + Back.LIGHTWHITE_EX + "   Developed : Mohamed Fouad   " + Style.RESET_ALL)
        print(Fore.RED + Back.LIGHTWHITE_EX + "        Goodbye!               " + Style.RESET_ALL)

    def main_menu(self):
        while True:
            print(Fore.GREEN + "1. Download a single video" + Style.RESET_ALL)
            print(Fore.BLUE + "2. Download a playlist" + Style.RESET_ALL)
            print(Fore.YELLOW + "3. Show instructions" + Style.RESET_ALL)
            print(Fore.RED + "4. Exit" + Style.RESET_ALL)

            choice = input(Fore.CYAN + "\nEnter your choice: " + Style.RESET_ALL)

            if choice == '1':
                url = input(Fore.BLUE + "Enter the video URL: " + Style.RESET_ALL)
                format_choices = self.choose_format()

                if format_choices != 'Back':
                    if 'MP3' in format_choices and 'MP4' in format_choices:
                        quality = self.choose_quality()  # Show quality options for MP4
                        if quality != 'Back':
                            output_path = self.choose_output_path()
                            # Download MP3 and MP4 concurrently
                            self.download_video(url, 'MP3', output_path=output_path)
                            self.download_video(url, 'MP4', quality, output_path)

                    elif 'MP3' in format_choices:
                        output_path = self.choose_output_path()
                        self.download_video(url, 'MP3', output_path=output_path)

                    elif 'MP4' in format_choices:
                        quality = self.choose_quality()  # Show quality options for MP4
                        if quality != 'Back':
                            output_path = self.choose_output_path()
                            self.download_video(url, 'MP4', quality, output_path)

            elif choice == '2':
                url = input(Fore.BLUE + "Enter the playlist URL: " + Style.RESET_ALL)
                format_choices = self.choose_format()

                if format_choices != 'Back':
                    if 'MP3' in format_choices and 'MP4' in format_choices:
                        quality = self.choose_quality()  # Show quality options for MP4
                        if quality != 'Back':
                            output_path = self.choose_output_path()
                            self.download_playlist(url, 'MP3', output_path=output_path)
                            self.download_playlist(url, 'MP4', quality, output_path)

                    elif 'MP3' in format_choices:
                        output_path = self.choose_output_path()
                        self.download_playlist(url, 'MP3', output_path=output_path)

                    elif 'MP4' in format_choices:
                        quality = self.choose_quality()  # Show quality options for MP4
                        if quality != 'Back':
                            output_path = self.choose_output_path()
                            self.download_playlist(url, 'MP4', quality, output_path)

            elif choice == '3':
                print(Fore.CYAN + "Instructions: Choose an option from the menu to download a video or playlist." + Style.RESET_ALL)
                input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)

            elif choice == '4':
                self.farewell_message()
                sys.exit()
            else:
                print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)


if __name__ == "__main__":
    downloader = VideoDownloader()
    downloader.main_menu()
