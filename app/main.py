import requests
import json
from format_logs import format_logs

def predict_sentiment(reviews):
    """
    Predicts the sentiment of imdb reviews

    Parameters:
        instances: a list of one or more reviews e.g. ["great movie", "horrible movie", "horrible and great movie"]
    
    Returns:
        reviews: a list of objects showing each review alongside a sentiment (i.e. positive or negative) and a sentiment score.
    """
    try:               
        global logger
        logger = format_logs()

        # tf serving rest endpoint
        port = '8501'
        base_url = f'http://localhost:{port}/v1/models/'
        model_name = 'text_classifier'
        
        # model version to be served.
        # update to a different version as you please. 
        # all versions are shown in model.config. 
        # available versions: 1 and 2.
        version = 1
        url = f'{base_url}{model_name}/versions/{version}:predict'

        logger.info(f'serving version {version} of the text classifier model')

        total_reviews = len(reviews)
        logger.info(f'fetching sentiment for {total_reviews} {"reviews" if total_reviews > 1 else "review"}')
        
        # construct data string and headers        
        data = json.dumps({"signature_name": "serving_default", "instances": reviews})
        headers = {"content-type": "application/json"}

        # ping the model endpoint
        json_response = requests.post(url, data=data, headers=headers)
        status_code = json_response.status_code

        if status_code >= 400:                        
            return f'server returned {status_code}.\nconfirm that version {version} of the model exists and is being served in the model.config file'
        
        classified_reviews = []
        for idx in range(0, total_reviews):            
            predictions = json.loads(json_response.text)['predictions'][idx]  
            review_score = predictions[0]      

            if review_score >= 0:
                classified_reviews.append({'review': reviews[idx], 'sentiment': 'positive review', 'sentiment_score': review_score})
            if review_score < 0:
                classified_reviews.append({'review': reviews[idx], 'sentiment': 'negative review', 'sentiment_score': review_score})        
        return classified_reviews

    except Exception as e:
        logger.info(e)

if __name__=='__main__':
    # update the review sample to test out different reviews
    review_samples = ['As others have mentioned, all the women that go nude in this film are mostly absolutely gorgeous. The plot very ably shows the hypocrisy of the female libido. When men are around they want to be pursued, but when no "men" are around, they become the pursuers of a 14 year old boy. And the boy becomes a man really fast (we should all be so lucky at this age!). He then gets up the courage to pursue his true love',
    'Seriously the best show I\'ve ever seen, it has a slow burn effect, where it can *appear* slow, but once it hits you, it hits like a truck. The dynamics between the characters, the rich world that they\'ve been put it, how it blends the lines of something sketchy that benefits Walter and his family, to a black hole of senseless crime and profit, it\'s addicting as all hell. Every single character is compelling to watch, even the lesser-known/less memorable characters such as Skyler and Gale. So many fan favorite personalities have spawned from this show, Saul, Gus, Walter, Walter JR, Huell, Mike, Jessie, Gale. All of these characters carefully added to compelling storytelling, Easter eggs that only the most astute viewers will find and appreciate, and beautiful soundtrack full of original songs, and now iconic ones that you will listen to over and over again. The ending alone is the most satisfying way it could ever conclude, this show will keep you up at night for hours reminiscing at how it all took place, and it will NEVER leave your mind after watching it. Truly a masterpiece,']    
    review_sentiment = predict_sentiment(review_samples)    
    logger.info(review_sentiment)