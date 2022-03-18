import os
from PIL import Image
import io
from io import BytesIO
import base64
from pydaisi import Daisi
import streamlit as st

# os.environ["ACCESS_TOKEN"] = "pQMB40ZJrwPs7HeHI9IXuz61Ra2T4qxx"
daisi = Daisi("GoogleNews", base_url = "https://dev3.daisi.io")
wc = Daisi("WordCloud", base_url = "https://dev3.daisi.io")


def get_wc(query):
    
    n = daisi.get_news(query=query,num="100")
    a = n.get_result()
    out = wc.compute(texts_path=a)
    img = out.get_result()
    bytestring_image = img[2]['src'].strip('data:image/png;base64,').strip(' ')
    imgdata = base64.b64decode(bytestring_image)
    image = Image.open(io.BytesIO(imgdata)).convert('RGBA')

    return image

st.title('WordCloud from Google News')

query = st.text_input(label = "Google News query", value = "Apple")

image = get_wc(query)

st.image(image)