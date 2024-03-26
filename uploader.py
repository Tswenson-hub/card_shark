import requests
import json
from ximilar.client import RestClient
from ximilar.client.constants import *
from ximilar.client.exceptions import XimilarClientInvalidDataException
from ximilar.client import CollectiblesRecognitionClient
import pandas as pd


GRADING_ENDPOINT = "card-grader/v2/grade"

COLLECTIBLES_PROCESS = "collectibles/v2/process"
COLLECTIBLES_CARD_ID = "collectibles/v2/tcg_id"
COLLECTIBLES_SPORT_ID = "collectibles/v2/sport_id"
COLLECTIBLES_DETECT = "collectibles/v2/detect"
COLLECTIBLES_SLAB_ID = "collectibles/v2/slab_id"
COLLECTIBLES_OCR_ID = "collectibles/v2/ocr_id"
COLLECTIBLES_ANALYZE = "collectibles/v2/analyze"



pic = [{'_url': 'https://images.ximilar.com/examples/cards/jordan.jpeg'}]
recog_client = CollectiblesRecognitionClient(token="e972a5215c18316047d2113cb13d8462a036c601")
result = recog_client.process(pic)
j = json.dumps(result, indent=2, sort_keys=True)
print(j)


