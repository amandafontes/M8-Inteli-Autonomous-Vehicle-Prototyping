import soundfile as sf
import simpleaudio as sa
from txtai.pipeline import TextToSpeech

# Carregamento do modelo de conversão de texto para áudio
tts = TextToSpeech("NeuML/ljspeech-jets-onnx")

def user_input():
    # Solicitação do input do usuário, contendo a frase que ele deseja converter para áudio
    frase = input("Digite aqui a frase que você deseja converter para áudio. Caso deseje sair da aplicação, digite 'Sair'.\n")

    if frase != "Sair":
        # Conversão para áudio
        audio = tts(frase)

        # Salva o áudio em um arquivo
        sf.write("output.wav", audio, 22050)

        # Lê o arquivo de áudio gerado
        wave_obj = sa.WaveObject.from_wave_file("output.wav")

        # Toca o áudio para o usuário via terminal
        play_obj = wave_obj.play()
        play_obj.wait_done()

        user_input()

    return print("Você optou por sair da aplicação.")

user_input()