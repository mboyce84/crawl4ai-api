from flask import Flask, request, jsonify
import asyncio
from crawl4ai import AsyncWebCrawler

app = Flask(__name__)

async def fetch_answer(question):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://help.gohighlevel.com/support/solutions", query=question)
        return result.markdown

@app.route('/crawl', methods=['POST'])
def crawl():
    data = request.json
    question = data.get("question", "")
    response = asyncio.run(fetch_answer(question))
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
