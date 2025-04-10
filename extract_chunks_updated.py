import os
import imageio.v3 as iio
from PIL import Image
from pathlib import Path


def extract_chunks(video_path, output_base_dir, chunk_duration=15, fps=1):
    video_id = Path(video_path).stem
    os.makedirs(output_base_dir, exist_ok=True)

    try:
        meta = iio.immeta(video_path, plugin="pyav")
        duration = int(meta["duration"])
    except Exception as e:
        print(f"❌ Could not read video metadata: {e}")
        return []

    chunk_metadata = []
    chunk_count = max(1, duration // chunk_duration)  # Ensure at least one chunk

    for chunk_idx in range(chunk_count):
        start_sec = chunk_idx * chunk_duration
        end_sec = min(duration, (chunk_idx + 1) * chunk_duration)
        chunk_name = f"{video_id}_chunk{chunk_idx}"
        chunk_dir = os.path.join(output_base_dir, chunk_name)
        os.makedirs(chunk_dir, exist_ok=True)

        for second in range(start_sec, end_sec):
            try:
                frame = iio.imread(video_path, index=second * fps, plugin="pyav")
                img = Image.fromarray(frame)
                frame_path = os.path.join(chunk_dir, f"frame_{second}.jpg")
                img.save(frame_path)
            except Exception as e:
                print(f"❌ Could not read frame at {second}s: {e}")

        chunk_metadata.append(
            {
                "video_id": video_id,
                "chunk_id": chunk_name,
                "start_time": start_sec,
                "end_time": end_sec,
                "frame_dir": chunk_dir,
            }
        )

    return chunk_metadata
