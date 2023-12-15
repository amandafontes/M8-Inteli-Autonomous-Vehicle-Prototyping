import whisper
import soundfile as sf
import simpleaudio as sa
from txtai.pipeline import TextToSpeech

# Carrega o modelo de conversão STT
stt = whisper.load_model("small")

# Carrega o modelo de conversão TTS
tts = TextToSpeech("NeuML/ljspeech-jets-onnx")

# Obtém o input do usuário
audio = input("Qual arquivo de áudio você deseja utilizar?")

# Converte o input do usuário em texto, no mesmo idioma
texto = stt.transcribe(audio, language="pt-BR")

# Converte o input do usuário em texto, traduzindo para o inglês
texto_traduzido = stt.transcribe(audio, language="pt-BR", task="translate")

# Exibe os resultados
print("Texto em português: ", texto["text"])
print("Texto traduzido: ", texto_traduzido["text"])

# Converte o texto traduzido em áudio
speech = tts(texto_traduzido["text"])

# Salva o áudio em um arquivo
sf.write("out.wav", speech, 22050)

# Lê o arquivo
wave_obj = sa.WaveObject.from_wave_file("out.wav")

# Toca o áudio
play_obj = wave_obj.play()
play_obj.wait_done()