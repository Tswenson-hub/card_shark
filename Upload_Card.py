import streamlit as st
from ximilar.client import CollectiblesRecognitionClient
import json


capture = st.camera_input('Upload card photo')
pic = [{'_url': capture}]
#pic = [{'_url': 'https://images.ximilar.com/examples/cards/jordan.jpeg'}]

recog_client = CollectiblesRecognitionClient(token="e972a5215c18316047d2113cb13d8462a036c601")
result = recog_client.process(pic)

if result['status']['code'] != 500:
    j = json.dumps(result, indent=4, sort_keys=True)
    st.write(j)

