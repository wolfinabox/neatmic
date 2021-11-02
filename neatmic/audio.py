import soundcard

def mic_from_name(name:str):
    for mic in soundcard.all_microphones():
        if name.lower() in mic.name.lower():
            return mic

def speaker_from_name(name:str):
    for speaker in soundcard.all_speakers():
        if name.lower() in speaker.name.lower():
            return speaker