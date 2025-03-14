import google.generativeai as genai

genai.configure(api_key="AIzaSyA92RcfEVj_gnW0eaVS_0OP8m6FRu8_oA8")

models = genai.list_models()
for model in models:
    print(model.name)