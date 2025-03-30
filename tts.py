from gtts import gTTS
import pygame
import io

def text_to_speech(text, lang='en'):
    if isinstance(text, int):
        text = str(text)
    text = text + '!'
    tts = gTTS(text=text, lang=lang)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    
    pygame.mixer.init()
    pygame.mixer.music.load(fp, 'mp3')
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)