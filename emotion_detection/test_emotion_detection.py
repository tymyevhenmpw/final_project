import unittest
from EmotionDetection import emotion_detector

TEST_DATA = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear"),
]

class EmotionTestCase(unittest.TestCase):
    def test_emotions(self):
        for sentence, expected in TEST_DATA:
            with self.subTest(sentence=sentence):
                result = emotion_detector(sentence)
                self.assertEqual(result["dominant_emotion"], expected)

if __name__ == "__main__":
    unittest.main()
