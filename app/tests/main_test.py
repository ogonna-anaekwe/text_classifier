import unittest
import sys
import os
# add the app folder to the sys path to help import the main.py file
sys.path.append(os.path.abspath('../app'))
import main
import parse_arguments

# parse arguments
global args
args = parse_arguments.parse_arguments() 

class TestPrediction(unittest.TestCase):   
    def setUp(self):
        """
        Defines class variable that can be shared across all test methods
        """
        self.review_samples = ['As others have mentioned, all the women that go nude in this film are mostly absolutely gorgeous. The plot very ably shows the hypocrisy of the female libido. When men are around they want to be pursued, but when no "men" are around, they become the pursuers of a 14 year old boy. And the boy becomes a man really fast (we should all be so lucky at this age!). He then gets up the courage to pursue his true love',
    'Seriously the best show I\'ve ever seen, it has a slow burn effect, where it can *appear* slow, but once it hits you, it hits like a truck. The dynamics between the characters, the rich world that they\'ve been put it, how it blends the lines of something sketchy that benefits Walter and his family, to a black hole of senseless crime and profit, it\'s addicting as all hell. Every single character is compelling to watch, even the lesser-known/less memorable characters such as Skyler and Gale. So many fan favorite personalities have spawned from this show, Saul, Gus, Walter, Walter JR, Huell, Mike, Jessie, Gale. All of these characters carefully added to compelling storytelling, Easter eggs that only the most astute viewers will find and appreciate, and beautiful soundtrack full of original songs, and now iconic ones that you will listen to over and over again. The ending alone is the most satisfying way it could ever conclude, this show will keep you up at night for hours reminiscing at how it all took place, and it will NEVER leave your mind after watching it. Truly a masterpiece,']            


    def test_version(self):
        """
        Checks that the version number is at least 1
        """
        self.assertGreater(args.version, 0)

    def test_review(self):
        """
        Checks if the reviews are in a list and that there is at least one review
        """        
        self.assertEqual(isinstance(self.review_samples, list), True)
        self.assertGreaterEqual(len(self.review_samples), 1)

    def test_prediction(self):
        """
        Checks if the server gives a response and if the resulting responses are valid
        """      
        result = main.predict_sentiment(self.review_samples)        
        self.assertIsNotNone(result)      
        self.assertEqual(isinstance(result, str), False)
        self.assertEqual(isinstance(result, list), True)
        self.assertEqual(isinstance(result[0], dict), True)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)