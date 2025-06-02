"""Flask micro-service exposing /emotionDetector route."""
from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Return emotion scores in friendly sentence form."""
    text = request.args.get("text", "")
    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    resp_msg = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}."
    )
    return jsonify({"answer": resp_msg})

if __name__ == "__main__":
    app.run(port=5000, debug=False)
