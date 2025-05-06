import unittest
from EmotionDetection.emotion_detection import emotion_detector  # Import the function from the package

class TestEmotionDetector(unittest.TestCase):
    """
    This class contains unit tests for the emotion_detector function.
    It tests the function with various statements and checks if the
    returned dominant emotion matches the expected emotion.
    """

    def test_joy(self):
        """
        Tests the emotion_detector function with a statement that should
        result in 'joy' as the dominant emotion.
        """
        text = "I am glad this happened"
        result = emotion_detector(text)
        # Check the 'dominant_emotion' key in the returned dictionary
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """
        Tests the emotion_detector function with a statement that should
        result in 'anger' as the dominant emotion.
        """
        text = "I am really mad about this"
        result = emotion_detector(text)
        # Check the 'dominant_emotion' key in the returned dictionary
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        """
        Tests the emotion_detector function with a statement that should
        result in 'disgust' as the dominant emotion.
        """
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        # Check the 'dominant_emotion' key in the returned dictionary
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """
        Tests the emotion_detector function with a statement that should
        result in 'sadness' as the dominant emotion.
        """
        text = "I am so sad about this"
        result = emotion_detector(text)
        # Check the 'dominant_emotion' key in the returned dictionary
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """
        Tests the emotion_detector function with a statement that should
        result in 'fear' as the dominant emotion.
        """
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        # Check the 'dominant_emotion' key in the returned dictionary
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_empty_string(self):
        """
        Tests the emotion_detector function with an empty string.
        """
        text = ""
        result = emotion_detector(text)
        # Check that the 'dominant_emotion' key in the returned dictionary is None
        self.assertIsNone(result['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()
