import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        try:
            emotions = response_dict['emotionPredictions'][0]['emotion']
            anger_score = emotions.get('anger', 0.0)
            disgust_score = emotions.get('disgust', 0.0)
            fear_score = emotions.get('fear', 0.0)
            joy_score = emotions.get('joy', 0.0)
            sadness_score = emotions.get('sadness', 0.0)

            # Find the dominant emotion
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            # Handle case where all scores might be 0 or None if API behaves unexpectedly
            if not any(emotion_scores.values()):
                 dominant_emotion = None
            else: 
                 dominant_emotion = max(emotion_scores, key=lambda k: emotion_scores[k] if emotion_scores[k] is not None else -1)

            # Format the output dictionary
            output = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
            return output
        except (KeyError, IndexError, TypeError) as e:
            # Handle cases where the expected structure is not found
            print(f"Error processing response: {e}")
            return {
                'anger': None, 'disgust': None, 'fear': None, 
                'joy': None, 'sadness': None, 'dominant_emotion': None
            }
            
    elif response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }
    else:
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

