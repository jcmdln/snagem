# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from os import cpu_count

import youtube_dl

from humanfriendly import format_size, format_timespan


class Audio:
    """Middleware for extracting audio from a URL."""

    def __init__(self) -> None:
        self.__config: dict = {
            "format": "bestaudio/best",
            "no_warnings": True,
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessor_args": [{"-threads": cpu_count()}],
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "0",
                }
            ],
            "quiet": True,
            "retries": 1,
            "writesubtitles": False,
            "writethumbnail": False,
        }

    def get(self, urls: list[str]) -> None:
        """Download audio from URLs in the best available quality."""
        index: int = 1
        length: int = len(urls)
        size: str = ""
        width: int = len(str(length))
        ydl: youtube_dl.YoutubeDL = youtube_dl.YoutubeDL(self.__config)

        for url in urls:
            info: dict = ydl.extract_info(url, download=False)

            if info and "filesize" in info and info["filesize"]:
                size = format_size(info["filesize"], binary=True)
            else:
                size = "?? MiB"

            print(
                'Downloading %*d of %*d: %s: "%s.%s"'
                % (width, index, width, length, size, info["title"], info["ext"])
            )

            ydl.download([url])

            index += 1

    def options(self, config: dict) -> None:
        """Set custom options."""
        if config:
            self.__config = config


class Info:
    """Middleware for collecting info about the media at a URL."""

    def __init__(self) -> None:
        self.data: dict = {}

    def __gather(self, i: dict) -> None:
        """Gather the extracted information and add it to data{}."""
        if i["uploader_id"] not in self.data:
            self.data[i["uploader_id"]] = {}

        self.data[i["uploader_id"]][i["id"]] = {
            "categories": i["categories"],
            "description": i["description"],
            "duration": format_timespan(i["duration"]),
            "subtitles": i["subtitles"],
            "tags": i["tags"],
            "title": i["title"],
            "url": i["webpage_url"],
        }

    def get(self, urls: list[str]) -> None:
        """Triage the data extracted by youtube_dl."""
        info: dict = {}
        ydl: youtube_dl.YoutubeDL = youtube_dl.YoutubeDL({"no_warnings": True, "quiet": True})

        for url in urls:
            info = ydl.extract_info(url, download=False)

            # Skip this iteration of the loop if no information was
            # collected.  This should almost never happen.
            if not info:
                print("skipped", url)
                continue

            # When retrieving information by url, one or more videos
            # might be found.  In such cases we need to determine if
            # there are multiple items to collect info for or not.
            if "entries" in info:
                for entry in info["entries"]:
                    # Skip over blank entries
                    if not entry:
                        continue

                    self.__gather(entry)
            else:
                self.__gather(info)


class Video:
    """Video."""

    def __init__(self) -> None:
        self.__config: dict = {
            "format": "bestvideo+bestaudio/best",
            "no_warnings": True,
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessor_args": [{"-threads": cpu_count()}],
            "postprocessors": [{"key": "FFmpegEmbedSubtitle"}],
            "quiet": True,
            "retries": 1,
            "subtitleslangs": ["en", "en-US", "es", "fr", "de", "ja", "zh"],
            "writesubtitles": True,
            "writethumbnail": False,
        }

    def get(self, urls: list[str]) -> None:
        """Download video from URLs in the best available quality."""
        index: int = 1
        info: dict = {}
        length: int = len(urls)
        size: str = ""
        width: int = len(str(length))
        ydl: youtube_dl.YoutubeDL = youtube_dl.YoutubeDL(self.__config)

        for url in urls:
            info = ydl.extract_info(url, download=False)

            if "filesize" in info and info["filesize"] is int:
                size = format_size(info["filesize"], binary=True)
            else:
                size = "?? MiB"

            print(
                'Downloading %*d of %*d: %s: "%s.%s"'
                % (width, index, width, length, size, info["title"], info["ext"])
            )

            ydl.download([url])

            index += 1

    def options(self, config: dict) -> None:
        """Set custom options."""
        if config:
            self.__config = config
