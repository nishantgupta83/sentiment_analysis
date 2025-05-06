
import requests
import json


def emotion_detector(text_to_analyze):
    #def <function_name>(<input_args>):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    # return response.text
    formatted_response = json.loads(response.text)
    final_response = {
        'anger': formatted_response["emotionPredictions"][0]['emotion']['anger'],
        'fear': formatted_response["emotionPredictions"][0]['emotion']['fear'],
        'joy': formatted_response["emotionPredictions"][0]['emotion']['joy'],
        'sadness': formatted_response["emotionPredictions"][0]['emotion']['sadness'],
        'disgust': formatted_response["emotionPredictions"][0]['emotion']['disgust'],
    }
    dominant_score, dominant_emotion = 0, ''
    for key in final_response.keys():
        if final_response[key] > dominant_score:
            dominant_score = final_response[key]
            dominant_emotion = key
    
    final_response['dominant_emotion'] = dominant_emotion
    return final_response