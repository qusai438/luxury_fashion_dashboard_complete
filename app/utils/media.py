import os
import subprocess
from typing import List

GENERATED_VIDEOS_DIR = "static/generated_videos"
os.makedirs(GENERATED_VIDEOS_DIR, exist_ok=True)

def generate_video_from_images(image_urls: List[str], video_id: str) -> str:
    frame_dir = f"{GENERATED_VIDEOS_DIR}/{video_id}_frames"
    os.makedirs(frame_dir, exist_ok=True)

    for idx, url in enumerate(image_urls):
        subprocess.run(["curl", "-s", url, "-o", f"{frame_dir}/{idx:03d}.png"])

    output_path = f"{GENERATED_VIDEOS_DIR}/{video_id}.mp4"
    cmd = [
        "ffmpeg",
        "-y",
        "-framerate", "1",
        "-i", f"{frame_dir}/%03d.png",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path
