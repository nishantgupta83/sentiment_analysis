from flask import Flask, request, render_template, url_for, redirect
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods = ['GET'])
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze', '')
    if not text_to_analyze:
        return render_template('index.html')

    emotions = emotion_detector(text_to_analyze)
    response = f"For the given statement, the system response is " 
    response += f"'anger': {emotions.get('anger')}, "
    response += f"'disgust': {emotions.get('disgust')}, "
    response += f"'fear': {emotions.get('fear')}, "
    response += f"'joy': {emotions.get('joy')}, "
    response += f"'sadness': {emotions.get('sadness')}. "
    response += f"The dominant emotion is {emotions.get('dominant_emotion')}"

    return response
    
if __name__ == "__main__":
    app.run(debug=True)