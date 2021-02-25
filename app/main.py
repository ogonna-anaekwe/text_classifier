import requests
import json

def predict_sentiment(instances):
    """
    Predicts the sentiment of imdb reviews

    Parameters:
        instances: a list of one or more reviews e.g. ["great movie", "horrible movie", "horrible and great movie"]
    
    Returns:
        predictions: an array of predictions scores for each of the reviews
    """
    try:
        # tf serving rest endpoint
        base_url = 'http://localhost:8501/v1/models/'
        model_name = 'text_classifier'
        
        # model version to be served.
        # update to a different version as you please. 
        # all versions are shown in model.config
        version = 1
        url = f'{base_url}{model_name}/versions/{version}:predict'

        print(f'serving version {version} of the text classifier model')

        # construct data string and headers        
        data = json.dumps({"signature_name": "serving_default", "instances": instances})
        headers = {"content-type": "application/json"}

        # ping the model endpoint
        json_response = requests.post(url, data=data, headers=headers)
        status_code = json_response.status_code

        if status_code >= 400:            
            return f'server returned {status_code}.\nconfirm that version {version} of the model exists and is being served in the model.config file'
        
        predictions = json.loads(json_response.text)['predictions']        
        review = ''
        review_score = predictions[0][0]
        if review_score > 0:
            review = f'postive movie review with a score of {review_score}'
        else:
            review = f'negative movie review with a score of {review_score}'            
        
        return review

    except Exception as e:
        print(e)

if __name__=='__main__':
    # update the review sample to test out different reviews
    # review_sample = 'As others have mentioned, all the women that go nude in this film are mostly absolutely gorgeous. The plot very ably shows the hypocrisy of the female libido. When men are around they want to be pursued, but when no "men" are around, they become the pursuers of a 14 year old boy. And the boy becomes a man really fast (we should all be so lucky at this age!). He then gets up the courage to pursue his true love'
    review_sample = 'Well, after the first episode of watching Aden Young embody the character of Daniel Holden, I\'m hooked. Daniel Holden was arrested for the rape and murder of his girlfriend at the age of 16, convicted and sent to live on death row at the age of 18, and 20 years later after living on death row in a cell by himself, preparing himself to die and be forever gone from this earth, has survived 5 stays of execution long enough for technology to catch up with forensic science and, unbelievably, Daniel Holden is released to his family because it is determined that his DNA was not found at the scene of the crime. So now the big question is: Will the current prosecutor re-try a 20 year old case? The whole town has an opinion, and while Daniel Holden walks around like a man in his own dream, quietly and painfully processing freedom, relating to a family that is 20 years older, and adjusting to the overwhelming overload of his sensory perceptions, danger is lurking as those involved in the original case begin to realize what is at risk if a new trial takes place. It\'s too soon for all of us, the audience, to know what is at risk because, wisely, the story is unfolding slowly and painstakingly like a new flower. The actors are all superb as they falter and try to think of how to talk to Daniel. Daniel is unsure, awkward, and quiet...very, very quiet. Aden Young\'s face can show about 5 emotions all at the same time, and in one scene as he is describing in a perfect soft, southern drawl his prison "initiation" experience for his shallow step-brother, Teddy, Daniel\'s expression changed from placid, to subdued, to quietly earnest, to a moment of sheer madness, before he snapped back to placid, leaving Teddy speechless and a little bit afraid. Totally alone and silent, this tall man with the haunted eyes drew me in as he walked to a baseball field and just laid down in the grass. How can such a gentle person be guilty of such a heinous crime? Who committed this crime and let this sweet soul suffer 24/7 for 20 years waiting to die, stealing his youth? Is this man guilty, innocent, reformed, or just a stone cold killer with a good con going? I don\'t know yet. So I will stay tuned.'    
    review_sentiment = predict_sentiment([review_sample])
    print(review_sentiment)