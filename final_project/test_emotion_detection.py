from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    
    def test_joy(self):
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], 'joy', "Should be joy")
        
    def test_anger(self):
        self.assertEqual(emotion_detector("I am really mad about this")['dominant_emotion'], 'anger', "Should be anger")
        
    def test_disgust(self):
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], 'disgust', "Should be disgust")
        
    def test_sadness(self):
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'], 'sadness', "Should be sadness")
        
    def test_fear(self):
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'], 'fear', "Should be fear")

if __name__ == '__main__':
    unittest.main()