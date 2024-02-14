"""
This module sets up a Flask server for an emotion detection application.
It includes routes for analyzing text and rendering the main page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    """
    Analyze the text from the request for emotional content and return
    a formatted response.
    """
    text_to_analyze = request.args.get('text')
    response = emotion_detector(text_to_analyze)

    if response and all(key in response for key in
                        ('anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion')):
        if response['dominant_emotion'] is None:
            return "Invalid text! Please try again."

        formatted_response = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
            f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )
        return formatted_response

    return "Invalid text or an error occurred. Please try again."

@app.route("/")
def render_index_page():
    """ Render the main index page. """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
