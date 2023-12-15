import gradio as gr
from langchain.llms import Ollama
from gtts import gTTS
from io import BytesIO
import pygame

pygame.mixer.init()

def speak(text, language):
    # Objeto BytesIO
    audio = BytesIO()
    # Salva o audio no objeto BytesIO
    audio_confg = gTTS(text=text, lang=language)
    audio_confg.write_to_fp(audio)
    audio.seek(0)
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Crie uma instância do Ollama
ollama = Ollama(base_url='http://localhost:11434', model="ajudante")

def response(prompt, history):
    speak("teste", 'pt')
    response = ""
    for chunk in ollama.stream(prompt):
        speak(prompt, 'pt')
        response += chunk
        speak(str(response), 'pt')
        return response

# Crie uma instância da interface de chat Gradio com a função do Ollama
demo = gr.ChatInterface(response)

# Lance a interface de chat
demo.launch()