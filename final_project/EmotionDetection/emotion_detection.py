import requests

def emotion_detector(text_to_analyse):
    # Check if the input text is None or blank
    if text_to_analyse is None or not text_to_analyse.strip():
        return {key: None for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']}

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 200:
        formatted_response = response.json()  # Directly parse JSON without json.loads()
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        return {key: None for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']}
