from flask import Flask, request, jsonify
import asyncio
from crawl4ai import AsyncWebCrawler
import traceback  # For error logging

app = Flask(__name__)

async def fetch_answer(question):
    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url="https://help.gohighlevel.com/support/solutions", query=question)
            return result.markdown
    except Exception as e:
        print(f"Error in fetch_answer: {traceback.format_exc()}")  # Log error
        return None

@app.route('/crawl', methods=['POST'])
def crawl():
    try:
        # Validate JSON request
        data = request.json
        if not data or "question" not in data:
            return jsonify({"error": "Missing 'question' field in request"}), 400

        question = data["question"]
        response = asyncio.run(fetch_answer(question))

        if response:
            return jsonify({"answer": response})
        else:
            return jsonify({"error": "Failed to retrieve answer"}), 500
    except Exception as e:
        print(f"API Error: {traceback.format_exc()}")  # Log API errors
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
