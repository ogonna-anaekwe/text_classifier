import requests
import json
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

def predict_sentiment(instances):
    """
    Predicts the sentiment of imdb reviews

    Parameters:
        instances: a list of one or more reviews e.g. ["great movie", "horrible movie", "horrible and great movie"]
    
    Returns:
        reviews: a list of objects showing each review alongside a sentiment (i.e. positive or negative) and a sentiment score.
    """
    try:
        # tf serving rest endpoint
        port = '8501'
        base_url = f'http://localhost:{port}/v1/models/'
        model_name = 'text_classifier'
        
        # model version to be served.
        # update to a different version as you please. 
        # all versions are shown in model.config. 
        # available versions: 1 and 2.
        version = 2
        url = f'{base_url}{model_name}/versions/{version}:predict'

        logging.info(f'serving version {version} of the text classifier model')

        total_reviews = len(instances)
        logging.info(f'fetching sentiment for {total_reviews} {"reviews" if total_reviews > 1 else "review"}')
        # construct data string and headers        
        data = json.dumps({"signature_name": "serving_default", "instances": instances})
        headers = {"content-type": "application/json"}

        # ping the model endpoint
        json_response = requests.post(url, data=data, headers=headers)
        status_code = json_response.status_code

        if status_code >= 400:            
            return f'server returned {status_code}.\nconfirm that version {version} of the model exists and is being served in the model.config file'
        
        reviews = []
        for idx in range(0, total_reviews):            
            predictions = json.loads(json_response.text)['predictions'][idx]  
            review_score = predictions[0]      

            if review_score >= 0:
                reviews.append({'review': instances[idx], 'sentiment': 'positive review', 'sentiment_score': review_score})
            else:
                reviews.append({'review': instances[idx], 'sentiment': 'negative review', 'sentiment_score': review_score})        
        return reviews

    except Exception as e:
        logging.info(e)

if __name__=='__main__':
    # update the review sample to test out different reviews
    review_samples = ['As others have mentioned, all the women that go nude in this film are mostly absolutely gorgeous. The plot very ably shows the hypocrisy of the female libido. When men are around they want to be pursued, but when no "men" are around, they become the pursuers of a 14 year old boy. And the boy becomes a man really fast (we should all be so lucky at this age!). He then gets up the courage to pursue his true love']    
    review_sentiment = predict_sentiment(review_samples)
    logging.info(review_sentiment)