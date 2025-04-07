import os
import faiss
import numpy as np
import pickle
from clip_embedding import embed_frame


def store_embeddings(image_dir, video_id, output_dir="embeddings"):
    index = faiss.IndexFlatL2(512)
    metadata = []

    for fname in sorted(os.listdir(image_dir)):
        if fname.endswith(".jpg"):
            fpath = os.path.join(image_dir, fname)
            embedding = embed_frame(fpath)
            index.add(np.array([embedding]))
            metadata.append({"video_id": video_id, "frame_path": fpath})

    os.makedirs(f"{output_dir}/faiss_index", exist_ok=True)
    os.makedirs(f"{output_dir}/metadata", exist_ok=True)

    faiss.write_index(index, f"{output_dir}/faiss_index/{video_id}.index")
    with open(f"{output_dir}/metadata/{video_id}.pkl", "wb") as f:
        pickle.dump(metadata, f)
