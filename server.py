"""
This module provides a function to detect emotions in text using a Watson NLP API.
It handles requests to the API and processes the response to extract emotion scores
and determine the dominant emotion. Error handling for invalid input and API issues
is included.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    """
    Renders the index.html page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    It takes text input, runs emotion detection, and returns the result.
    """
    # Get the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if text_to_analyze is None or empty
    if not text_to_analyze:
        return "Invalid text! Please try again!!!." # Or return a specific error message/format

    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)

    # Check if the result is None or if dominant_emotion is None
    if result is None or result['dominant_emotion'] is None:
        return "For the given text, the emotion result is None."

    # Format the output string as requested by the customer
    formatted_output = (
        f"anger: {result['anger']:.2f}, "
        f"disgust: {result['disgust']:.2f}, "
        f"fear: {result['fear']:.2f}, "
        f"joy: {result['joy']:.2f}, "
        f"sadness: {result['sadness']:.2f}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
