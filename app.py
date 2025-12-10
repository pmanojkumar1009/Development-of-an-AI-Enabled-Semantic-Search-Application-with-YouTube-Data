from flask import Flask, request, jsonify
from flask_cors import CORS
from video_search_engine import VideoSearchEngine

app = Flask(__name__)
CORS(app)

search_engine = VideoSearchEngine()

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "✅ Semantic Video Search API is running!",
        "usage": "POST to /search with {'query': 'your text', 'top_k': 8, 'sortBy': 'similarity' | 'channel'}"
    })

@app.route("/search", methods=["POST"])
def search_videos():
    try:
        data = request.get_json()
        query = data.get("query", "").strip()
        top_k = int(data.get("top_k", 8))  # ✅ default to 8 videos
        sort_by = data.get("sortBy", "similarity")  # ✅ handle sort type

        if not query:
            return jsonify({"error": "Query cannot be empty"}), 400

        # Perform semantic search
        result_obj = search_engine.search(query, top_k)
        results = result_obj["results"]

        # ✅ Sorting logic
        if sort_by == "channel":
            results = sorted(results, key=lambda x: x["channel_title"].lower())
        else:
            results = sorted(results, key=lambda x: x["similarity_score"], reverse=True)

        return jsonify(results)

    except Exception as e:
        print("❌ Error in /search:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
