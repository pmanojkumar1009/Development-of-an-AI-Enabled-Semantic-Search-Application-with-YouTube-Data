# YouTube Semantic Search Engine

### AI-Enabled Semantic Search Application with YouTube Data

This project is an **AI-powered YouTube Semantic Search Engine** that
retrieves videos based on the *meaning* of a user's query using
transformer-based embeddings.\
It was developed as part of **Infosys Springboard Virtual Internship 6.0
(B2)**.

## 1. Project Overview

Traditional YouTube search works on keywords.\
This project uses **semantic search**, which understands *context* and
*intent*.

The system: - Reads YouTube metadata & transcripts\
- Converts them into embeddings\
- Stores them in a vector database\
- Searches the most relevant videos using cosine similarity

## 2. Objectives

-   Enable natural-language semantic search for YouTube videos\
-   Use transformer-based sentence embeddings\
-   Store embeddings efficiently using a vector database (ChromaDB)\
-   Provide a modern UI to browse search results\
-   Show similarity scores, recent searches, and sorting options

## 3. High-Level Architecture

### Frontend (React)

-   Built using **React, Tailwind CSS, Framer Motion**
-   Communicates with backend via POST `/search`
-   Displays video results, similarity scores, sorting, dark mode, etc.

### Backend (Flask)

-   Loads **sentence-transformer model** for embeddings\
-   Connects to **ChromaDB** for vector search\
-   Returns top-K relevant videos with similarity scores

### Vector Database (ChromaDB)

Stores:

    video_id  
    title  
    description  
    channel  
    thumbnail  
    yt_link  
    embedding  

### Semantic Search Workflow

    User Query → Embedding → Vector Search → Ranked Results → UI Display

## 4. Backend Details

### Tech Stack

-   Python\
-   Flask, Flask-CORS\
-   sentence-transformers\
-   ChromaDB\
-   NumPy

### API Endpoints

#### GET /

Health check.

#### POST /search

Request:

``` json
{
  "query": "machine learning basics",
  "top_k": 8,
  "sortBy": "similarity"
}
```

Response:

``` json
[
  {
    "video_title": "...",
    "description": "...",
    "channel_title": "...",
    "thumbnail": "...",
    "yt_link": "...",
    "similarity_score": 0.842
  }
]
```

### Error Handling

  Condition         Response
  ----------------- -----------------------------------------
  Empty query       400: {"error": "Query cannot be empty"}
  Internal errors   500 with message

## 5. Frontend Details

### Tech Stack

-   React\
-   Tailwind CSS\
-   Axios\
-   Framer Motion\
-   LocalStorage

### Key Components

  Component       Description
  --------------- --------------------------------------
  App.jsx         Main UI, API calls, state management
  SearchBar.jsx   Search input + sort dropdown
  VideoCard.jsx   Displays each video result
  Sidebar.jsx     Shows recent searches
  Navbar.jsx      Title, dark/light mode
  ParticlesBg     Background animations

### Features

-   Search YouTube videos semantically\
-   Show similarity scores\
-   Dark / Light mode\
-   Sorting (Similarity / Channel Name)\
-   Recent search history\
-   Open videos on YouTube

## 6. Query Processing Pipeline

1.  User enters a natural-language query\
2.  React sends POST request to Flask\
3.  Flask embeds the query\
4.  Vector DB returns top-K similar videos\
5.  Backend ranks & sorts\
6.  Frontend displays interactive results

## 7. Installation & Setup

### Backend Setup

    git clone <repo-url>
    cd backend
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python app.py

### Frontend Setup

    cd frontend
    npm install
    npm run dev

Set API endpoint in `.env`:

    VITE_API_BASE_URL=http://127.0.0.1:8000

## 8. Future Enhancements

-   User login + personalized search history\
-   Filters (duration, upload date, language)\
-   Advanced NLP (query expansion / correction)\
-   Deployment on cloud platforms\
-   Admin dashboard for analytics

## 9. Credits

Developed as part of:\
**Infosys Springboard Virtual Internship 6.0 (B2)**\
Uses open-source tools: - Flask\
- React\
- sentence-transformers\
- ChromaDB\
- Tailwind CSS\
- Framer Motion
