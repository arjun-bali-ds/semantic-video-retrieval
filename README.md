# semantic-video-retrieval
Search within a Video - RAG + Text to SQL 

🔍 Search within videos using semantic language queries.

This project implements a prototype of a multimodal retrieval system that:
- Converts video frames to embeddings using CLIP
- Stores them in a FAISS vector database
- Supports semantic text search
- Will be extended to generate SQL queries and answers using LLMs

## Project Structure
```
semantic-video-retrieval/
│
├── data/
│   ├── videos/                  # Contains video files for processing
│   ├── frames/                  # Contains extracted frames from videos (chunked)
│   └── chunks/                  # Folder containing frames for each chunk
│
├── embeddings/                   # Folder to store FAISS index and embeddings
│   ├── faiss_index/             # FAISS index of video embeddings
│   └── metadata/                # Metadata for chunked videos
│
├── notebooks/                    # Jupyter Notebooks for experimentation
│
├── .venv/                        # Python virtual environment
├── clip_embedding.py             # Functions to handle frame embeddings using CLIP
├── extract_chunks_updated.py     # Video chunking functionality
├── store_embeddings.py           # Store embeddings into FAISS index
├── search_top_chunks.py          # Search top matching video chunks
├── requirements.txt              # List of Python dependencies
└── .gitignore                    # Ignore large video and embeddings folders

```
To prevent large files (such as videos and embeddings) from being uploaded to the remote repository, add the following to .gitignore:

data/videos/
embeddings/

## How to Use
### Step 1: Install dependencies
To get started, first install the dependencies:

pip install -r requirements.txt

Step 2: Extract video frames
You can extract frames from your videos using the extract_chunks_updated.py script. This will chunk your videos and extract frames.

Step 3: Generate embeddings
Once the frames are extracted, the clip_embedding.py script will process each frame and generate embeddings using CLIP.

Step 4: Store embeddings in FAISS
Use the store_embeddings.py script to store the generated embeddings into a FAISS index for fast similarity search.

Step 5: Search for videos
Finally, use the search_top_chunks.py script to search through your indexed video chunks with semantic queries.

Step 6: Visualize results
You can visualize the search results and open the relevant video chunks with the play_results.py script.


The notebook SemanticSearchDemo.ipynb actually follows all these steps and implments it.
