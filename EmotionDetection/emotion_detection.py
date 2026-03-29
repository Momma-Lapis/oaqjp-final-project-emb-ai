import requests # Import the requests library to handle HTTP requests

# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }


def emotion_detector(text_to_analyze): # Define a function named emotion_detector
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' #URL of the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} #Set the headers required for the API request
    myobj = {"raw_document": { "text": text_to_analyze }} # Create a dictionary with the text to be analyzed
    response = requests.post(url, json = myobj, headers=header) #Send a POST request to the API with the text and headers
    
    # Parse the JSON response
    response_json = response.json()
    
    # Extract emotion scores from the response
    emotions = response_json['emotionPredictions'][0]['emotion']
    
    # Find the dominant emotion (the one with the highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return formatted dictionary with emotion scores and dominant emotion
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
