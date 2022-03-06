# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from os import cpu_count
from typing import Optional

import youtube_dl

from humanfriendly import format_size, format_timespan


class Media:
    def __init__(
        self,
        format: str = "best",
        no_warnings: bool = True,
        outtmpl: str = "%(title)s.%(ext)s",
        postprocessor_args: list[dict] = [{"-threads": cpu_count()}],
        postprocessors: Optional[list[dict]] = None,
        quiet: bool = True,
        retries: int = 1,
        subtitleslangs: Optional[list[str]] = None,
        writesubtitles: bool = False,
        writethumbnail: bool = True,
    ) -> None:
        self.youtube_dl: youtube_dl.YoutubeDL = youtube_dl.YoutubeDL(
            params={
                "format": format,
                "no_warnings": no_warnings,
                "outtmpl": outtmpl,
                "postprocessor_args": postprocessor_args,
                "postprocessors": postprocessors,
                "quiet": quiet,
                "retries": retries,
                "subtitleslangs": subtitleslangs,
                "writesubtitles": writesubtitles,
                "writethumbnail": writethumbnail,
            }
        )

    def get(self, urls: list[str]) -> None:
        index: int = 1
        length: int = len(urls)
        size: str = ""

        for url in self.info(urls).keys():

            if url.get("size"):
                size = format_size(url.get("size"), binary=True)
            else:
                size = "?? MiB"

            print(
                'Downloading {} of {}: {}: "{}.{}"'.format(
                    index, length, size, url.get("title"), url.get("ext")
                )
            )

            self.youtube_dl.download([url])

            index += 1

    def info(self, source_urls: list[str]) -> dict:
        results: dict = {}

        def __gather(item: dict) -> None:
            if not item.get("webpage_url"):
                return

            results[item.get("webpage_url")] = {
                "categories": item.get("categories"),
                "description": item.get("description"),
                "duration": format_timespan(item.get("duration", 0)),
                "subtitles": item.get("subtitles"),
                "size": item.get("filesize", 0),
                "tags": item.get("tags"),
                "title": item.get("title"),
            }

        for url in source_urls:
            info = self.youtube_dl.extract_info(url, download=False)

            if not info:
                print("skipped", url)
                continue

            if info.get("entries"):
                for entry in info.get("entries"):
                    if not entry:
                        continue

                    __gather(entry)
            else:
                __gather(info)

        return results


class Audio(Media):
    def __init__(
        self,
        format: str = "bestaudio/best",
        postprocessors: Optional[list[dict]] = [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "0"}
        ],
    ) -> None:
        super().__init__(format=format, postprocessors=postprocessors)


class Video(Media):
    def __init__(
        self,
        format: str = "bestvideo+bestaudio/best",
        postprocessors: list[dict] = [{"key": "FFmpegEmbedSubtitle"}],
        subtitleslangs: list[str] = ["en", "en-US", "es", "fr", "de", "ja", "zh"],
        writesubtitles: bool = True,
    ) -> None:
        super().__init__(
            format=format,
            postprocessors=postprocessors,
            subtitleslangs=subtitleslangs,
            writesubtitles=writesubtitles,
        )


__all__: list[str] = ["Audio", "Media", "Video"]
