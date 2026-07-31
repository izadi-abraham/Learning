#!/usr/bin/env python3

import base64
import json
from pathlib import Path
from urllib.parse import urljoin

import requests


PLAYLIST = Path("playlist-from-curl.json")

# This is the URL you used with curl.
PLAYLIST_URL = (
    "https://vod-adaptive-ak.vimeocdn.com/exp=1785529535~acl=%2F3e33acff-a0d4-491f-9041-0daee47f4f92%2Fpsid%3Ddfa0bb972e97776e0984fb0a9d9469b469cdde9e1785508419%2F%2A~hmac=338ec3f6a1efb56cddda316a33a638fc0b87e97f0dc2dffd579a0c41a88f5e5f/3e33acff-a0d4-491f-9041-0daee47f4f92/psid=dfa0bb972e97776e0984fb0a9d9469b469cdde9e1785508419/v2/playlist/av/primary/prot/cXNyPTE/playlist.json?omit=av1-hevc&pathsig=8c953e4f~9gabxsyofiG13P92xUGFG9pSwn0W5pOMCA0Ue39hw2E&qsr=1&r=dXM=&rh=44IWba"
)


def load_manifest():
    with PLAYLIST.open() as f:
        return json.load(f)


def choose_best_video(manifest):
    return max(manifest["video"], key=lambda v: v["height"])


def choose_best_audio(manifest):
    return max(manifest["audio"], key=lambda a: a["bitrate"])


def build_base_url(base_url: str):
    return urljoin(PLAYLIST_URL, base_url)


def write_init_segment(track, filename):
    init = base64.b64decode(track["init_segment"])

    with open(filename, "wb") as f:
        f.write(init)


def download_segment(base, segment):
    url = urljoin(base, segment["url"])

    r = requests.get(url)
    r.raise_for_status()

    print(f"Downloaded {len(r.content)} bytes")

    return r.content


def download_track(track, filename, base):
    write_init_segment(track, filename)

    total = len(track["segments"])

    for i, segment in enumerate(track["segments"], start=1):
        print(f"{filename}: {i}/{total}")

        data = download_segment(base, segment)
        append_segment(filename, data)


def append_segment(path, data):
    with open(path, "ab") as f:
        f.write(data)


def main():
    manifest = load_manifest()

    base = build_base_url(manifest["base_url"])


    video = choose_best_video(manifest)
    audio = choose_best_audio(manifest)

    print(
        f'Video: {video["width"]}x{video["height"]}'
        f'({len(video["segments"])} segments)'
    )

    print(
        f'Audio: {audio["bitrate"]} bps'
        f'({len(audio["segments"])} segments)'
    )

    #download_track(video, "video.fmp4", base)
    download_track(audio, "audio.fmp4", base)


if __name__ == "__main__":
    main()
