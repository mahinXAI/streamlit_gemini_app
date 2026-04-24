import google.genai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import io


#loading the environment variable
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

#Initializing a client
client=genai.Client(api_key= my_api_key)


#note generator

def note_generator(images):
    prompt= '''"Summarize the picture in note format in language English at max 100 words,
      make sure to add necessary markdown to differentiate different section'''
    

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents =[images,prompt]
    )
    return response.text


def audio_transcription(text):
    speech = gTTS(text, lang='en',slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quize_generator(image, difficulty):
    prompt= '''"Generate 3 quizzes based on the {difficulty}. Make Sure to add markdown to differentiate the options'''
    

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents =[image,prompt]
    )
    return response.text