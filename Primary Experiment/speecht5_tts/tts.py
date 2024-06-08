# Code used to generate the audio files for the Microsoft SpeechT5 voice for the primary listening test.
from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch
import torchvision

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

speech = synthesiser("TEXT PROMPT HERE", forward_params={"speaker_embeddings": speaker_embedding})

sf.write("speecht5_multisent.wav", speech["audio"], samplerate=speech["sampling_rate"])
