"""Flask server for Emotion Detection Application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Endpoint to analyze the emotion in a given text.
    Returns formatted emotion scores and dominant emotion,
    or an error message for invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    # Handle blank input case
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

@app.route("/")
def render_index_page():
    """
    Serves the main HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask app on localhost at port 5000.
    app.run(host="0.0.0.0", port=5000)
    