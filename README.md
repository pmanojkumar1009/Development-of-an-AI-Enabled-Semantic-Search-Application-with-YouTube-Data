YouTube Semantic Search Engine
AI‑Enabled Semantic Search Application with YouTube Data

1. Project Overview
This project is an AI‑enabled YouTube Semantic Search Engine that helps users find videos based on the meaning of their query, not just keyword matches.
The system converts video titles, descriptions, and transcripts, as well as user queries, into semantic embeddings and uses a vector database + cosine similarity to retrieve the most relevant videos.

This application was developed as part of Infosys Springboard Virtual Internship 6.0 (B2): Development of AI‑Enabled Semantic Search Application with YouTube Data.

2. Objectives
Enable semantic search over YouTube videos using natural‑language queries.

Use transformer‑based sentence embeddings instead of plain keyword search.

Store and search embeddings efficiently using a vector database.

Provide a modern, responsive UI for interacting with search results.

Expose useful features like similarity scores, recent searches, sorting, and direct navigation to YouTube.

3. High‑Level Architecture
Frontend (React App)

Built with React, Tailwind CSS, and Framer Motion.

Communicates with the backend via REST API (/search).

Backend (Flask API)

Built with Python + Flask + Flask‑CORS.

Loads a sentence‑transformer model to generate embeddings.

Connects to a vector database (e.g., ChromaDB) where all video embeddings are stored.

YouTube Data & Vector Store

YouTube video metadata and transcripts are pre‑processed.

Each video is converted into an embedding and stored in the vector DB with:

video_id, video_title, description, channel_title, thumbnail, yt_link, embedding.

Semantic Search Flow

User enters a query → frontend calls /search.

Backend embeds query → runs similarity search in vector DB → ranks results using cosine similarity → returns top‑K videos with their similarity_score.

Frontend renders ranked video cards and allows sorting/filtering.

4. Backend Details
4.1 Tech Stack
Language: Python

Framework: Flask, Flask‑CORS

ML / NLP: sentence-transformers (e.g., MiniLM‑based model)

Vector DB: ChromaDB (or similar)

Others: requests, numpy, pydantic (optional)

4.2 Core Concepts
Embeddings

Sentences (titles, transcripts, queries) are converted into high‑dimensional vectors.

These vectors capture semantic meaning and allow similarity comparison.

Vector Database

Stores all video embeddings with metadata.

Supports fast k‑nearest neighbor search for a given query embedding.

Cosine Similarity

Measures how close two vectors are in direction.

Values near 1.0 → highly similar; near 0.0 → unrelated.

Used to compute similarity_score for each video.

4.3 API Design (Example)
GET /

Health check. Returns API status and usage info.

POST /search

Body:

json
{
  "query": "data structures in python",
  "top_k": 8,
  "sortBy": "similarity"   // or "channel"
}
Steps:

Validate query.

Generate query embedding using sentence‑transformer.

Search vector DB for top‑K similar videos.

Sort:

by similarity_score (desc) when sortBy = "similarity", or

by channel_title when sortBy = "channel".

Return JSON list of videos.

Response (simplified):

json
[
  {
    "video_title": "...",
    "description": "...",
    "channel_title": "...",
    "thumbnail": "https://...",
    "yt_link": "https://youtube.com/watch?v=...",
    "similarity_score": 0.842
  },
  ...
]
4.4 Error Handling
Empty query → HTTP 400 with {"error": "Query cannot be empty"}.

Unexpected exceptions → HTTP 500 with error message logged server‑side.

5. Frontend Details
5.1 Tech Stack
React (Vite or CRA)

Tailwind CSS for styling

Framer Motion for animations

Axios for HTTP requests

LocalStorage for saving recent searches

5.2 Main Components
App.jsx

Global layout, theme (dark/light mode), sidebar + main content.

Holds core state: query, videos, loading, sortBy, darkMode, recentSearches, sidebarOpen.

Implements handleSearch to call backend and update UI.

SearchBar.jsx

Input field + search button + sort dropdown (Sort by Similarity / Sort by Channel).

VideoCard.jsx

Displays:

Thumbnail

Video title

Description (clamped)

Channel name

Similarity score badge

"Watch on YouTube" button (opens yt_link in a new tab).

Sidebar.jsx

Shows Recent Searches.

Clicking an item re‑triggers a search with that term.

Uses localStorage to persist across refreshes.

Navbar.jsx

Project title, dark/light mode toggle, sidebar toggle.

ParticlesBg / visual components

Animated background for a modern look.

5.3 Frontend Behaviour
On load:

Read recentSearches from localStorage.

Show empty state or last results.

On search:

Validate query (non‑empty).

Show loading spinner.

Send POST /search.

On success: update videos, update recentSearches (max 5 unique items).

On sort change:

Re‑sort videos array locally by:

similarity_score (descending), or

channel_title (A–Z).

On clicking "Watch on YouTube":

Open video.yt_link in a new browser tab.

6. Query Processing Pipeline (End‑to‑End)
User Input

User types a natural question or phrase into the search bar.

Frontend Request

React sends POST request to /search with { query, top_k, sortBy }.

Backend Embedding

Backend embeds the query using the sentence‑transformer model.

Vector Search

Query embedding is passed to vector DB to retrieve top‑K nearest video embeddings.

Similarity scores (cosine similarity) are computed.

Ranking & Sorting

Results are ranked by similarity; optional secondary sort by channel.

Response to Frontend

Backend returns a JSON list of video objects.

Rendering

React maps over the list and displays VideoCard components.

User can refine, re‑sort, or click through to YouTube.

7. Installation & Setup (Example)
7.1 Backend
bash
git clone <repo-url>
cd backend

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt

# configure model name, DB path, and YouTube data in config file or env vars

python app.py  # runs on http://127.0.0.1:8000
7.2 Frontend
bash
cd frontend
npm install
npm run dev  # runs on http://localhost:5173 (or similar)
Ensure the frontend .env or config points VITE_API_BASE_URL (or similar) to the backend URL.

8. Future Enhancements
Add user authentication and personalized history.

Support filters (duration, upload date, channel, language).

Integrate query rewriting to auto‑correct and expand user queries.

Add analytics dashboard for search trends.

Deploy backend (e.g., on Render/Heroku) and frontend (e.g., on Vercel/Netlify).

9. Credits
Developed as part of Infosys Springboard Virtual Internship 6.0 (B2).

Uses open‑source libraries: sentence-transformers, Flask, React, Tailwind CSS, Framer Motion, and a vector database (ChromaDB).
