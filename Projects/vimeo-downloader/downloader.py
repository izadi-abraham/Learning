#!/usr/bin/env python3

import base64
import json
from pathlib import Path
from urllib.parse import urljoin
import requests
import sys


# This is the URL you used with curl.
PLAYLIST_URL = (
    "https://skyfire.vimeocdn.com/1786481027-0x62444678e5dbee2217d0744f4473f4875eaf6252/eb6d3e78-7429-4c0d-86d9-171c65807433/psid=3388c11e76264af29c611af1f53bf2e09e9037141786460847/v2/playlist/av/primary/prot/cXNyPTE/playlist.json?omit=av1-hevc&pathsig=8c953e4f~G7X5kZVMJmHPOebFAPxZsq0PxIICQjrZ-fmsVSVL-IY&qsr=1&r=dXM=&rh=2L60Ox"
)


def load_manifest(path):
    with path.open() as f:
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

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <playslist.json>")
        sys.exit(1)

    playlist = Path(sys.argv[1])

    manifest = load_manifest(playlist)

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

    download_track(video, "video.fmp4", base)
    download_track(audio, "audio.fmp4", base)


if __name__ == "__main__":
    main()
