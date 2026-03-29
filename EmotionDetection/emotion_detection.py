import requests # Import the requests library to handle HTTP requests

# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }


def emotion_detector(text_to_analyze): # Define a function named emotion_detector
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' #URL of the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} #Set the headers required for the API request
    myobj = {"raw_document": { "text": text_to_analyze }} # Create a dictionary with the text to be analyzed
    response = requests.post(url, json=myobj, headers=header) #Send a POST request to the API with the text and headers

    empty_result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    # If status is 400 (blank/invalid input), return all keys with None values.
    if response.status_code == 400:
        return empty_result

    # If status is 500, return all keys with None values.
    if response.status_code == 500:
        return empty_result

    # If the response status code is 200, parse and return the emotion scores.
    if response.status_code == 200:
        response_json = response.json()
        emotions = response_json['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }

    # For any other unexpected status code, return all keys with None values.
    return empty_result
