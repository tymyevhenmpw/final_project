import json
import requests

_URL = "https://sn-watson-emotion.labs.skills.network/v1/" \
       "watson.runtime.nlp.v1/NlpService/EmotionPredict"
_HEADERS = {"grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze: str) -> dict:
    """Return Watson scores + dominant emotion.

    Keys: anger, disgust, fear, joy, sadness, dominant_emotion
    """
    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(_URL, headers=_HEADERS,
                             json=payload, timeout=10)

    if response.status_code != 200:
        response.raise_for_status()

    data = response.json()
    emotions = data["emotionPredictions"][0]["emotion"]
    scores = {e["emotion"]: e["score"] for e in emotions}
    dominant = max(scores, key=scores.get)

    return {
        "anger":   scores.get("anger"),
        "disgust": scores.get("disgust"),
        "fear":    scores.get("fear"),
        "joy":     scores.get("joy"),
        "sadness": scores.get("sadness"),
        "dominant_emotion": dominant,
    }
