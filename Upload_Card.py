import streamlit as st
from ximilar.client import CollectiblesRecognitionClient


capture = st.camera_input('Upload card photo')
pic = [{'_url': capture}]
#pic = [{'_url': 'https://images.ximilar.com/examples/cards/jordan.jpeg'}]

if pic != None:
    recog_client = CollectiblesRecognitionClient(token="e972a5215c18316047d2113cb13d8462a036c601")
    print(recog_client.process(pic))