<<<<<<< HEAD
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import subprocess
import uuid

from vitalbrain import openai_offline_reply, detect_language
import asyncio

def text_to_speech(text, lang_code, out_path):
    """
    Edge TTS wrapper that writes speech to out_path.mp3.
    """
    async def _speak():
        from edge_tts import Communicate
        # choose a voice based on lang_code (default English)
        voice = {
            "ar": "ar-EG-SalmaNeural",
            "fa": "fa-IR-DilaraNeural",
            "hi": "hi-IN-SwaraNeural"
        }.get(lang_code, "en-US-JennyNeural")
        tts = Communicate(text, voice=voice)
        await tts.save(out_path)
    asyncio.run(_speak())

# ————— CONFIG —————
WHISPER_PATH = os.getcwd()
MODEL_NAME   = "ggml-base.en.bin"
TEMP_DIR     = os.path.join(WHISPER_PATH, "temp")

app = Flask(__name__)
CORS(app)

# Ensure temp folder exists
os.makedirs(TEMP_DIR, exist_ok=True)

@app.route("/transcribe", methods=["POST"])
def transcribe_voice():
    try:
        # 1. Save uploaded blob
        audio = request.files["audio"]
        audio_id = str(uuid.uuid4())
        webm_path = os.path.join(TEMP_DIR, f"{audio_id}.webm")
        wav_path  = os.path.join(TEMP_DIR, f"{audio_id}.wav")
        txt_path  = wav_path + ".txt"
        mp3_path  = os.path.join(TEMP_DIR, f"{audio_id}.mp3")

        audio.save(webm_path)

        # 2. Convert to 16-bit, 16 kHz mono WAV via ffmpeg
        subprocess.run([
            "ffmpeg", "-y", "-i", webm_path,
            "-ar", "16000", "-ac", "1", "-sample_fmt", "s16",
            wav_path
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # 3. Transcribe with whisper.cpp
        subprocess.run([
            os.path.join(WHISPER_PATH, "main.exe"),
            "-m", os.path.join(WHISPER_PATH, MODEL_NAME),
            "-f", wav_path,
            "-otxt"
        ], check=True, stdout=subprocess.DEVNULL)

        # 4. Read transcript
        with open(txt_path, "r", encoding="utf-8") as f:
            text = f.read().strip()

        # 5. Generate reply
        reply = openai_offline_reply(text)

        # 6. Text-to-speech (if not Kurdish)
        lang = detect_language(text)
        if lang not in ("ku", "ckb"):
            # This calls into your vitalbrain.text_to_speech
            text_to_speech(reply, lang, out_path=mp3_path)

        # 7. Return JSON
        return jsonify({
            "text":  text,
            "reply": reply,
            "lang":  lang,
            "mp3":   f"/audio/{audio_id}.mp3" if os.path.exists(mp3_path) else None
        })

    except Exception as e:
        print("ERROR in /transcribe:", e)
        return jsonify({"error": str(e)}), 500

@app.route("/audio/<filename>")
def send_audio(filename):
    # Serve the generated MP3 back to the browser
    return send_file(os.path.join(TEMP_DIR, filename), mimetype="audio/mpeg")

if __name__ == "__main__":
    # Run on all interfaces, port 5000
    app.run(host="0.0.0.0", port=5000)
=======
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import subprocess
import uuid

from vitalbrain import openai_offline_reply, detect_language
import asyncio

def text_to_speech(text, lang_code, out_path):
    """
    Edge TTS wrapper that writes speech to out_path.mp3.
    """
    async def _speak():
        from edge_tts import Communicate
        # choose a voice based on lang_code (default English)
        voice = {
            "ar": "ar-EG-SalmaNeural",
            "fa": "fa-IR-DilaraNeural",
            "hi": "hi-IN-SwaraNeural"
        }.get(lang_code, "en-US-JennyNeural")
        tts = Communicate(text, voice=voice)
        await tts.save(out_path)
    asyncio.run(_speak())

# ————— CONFIG —————
WHISPER_PATH = os.getcwd()
MODEL_NAME   = "ggml-base.en.bin"
TEMP_DIR     = os.path.join(WHISPER_PATH, "temp")

app = Flask(__name__)
CORS(app)

# Ensure temp folder exists
os.makedirs(TEMP_DIR, exist_ok=True)

@app.route("/transcribe", methods=["POST"])
def transcribe_voice():
    try:
        # 1. Save uploaded blob
        audio = request.files["audio"]
        audio_id = str(uuid.uuid4())
        webm_path = os.path.join(TEMP_DIR, f"{audio_id}.webm")
        wav_path  = os.path.join(TEMP_DIR, f"{audio_id}.wav")
        txt_path  = wav_path + ".txt"
        mp3_path  = os.path.join(TEMP_DIR, f"{audio_id}.mp3")

        audio.save(webm_path)

        # 2. Convert to 16-bit, 16 kHz mono WAV via ffmpeg
        subprocess.run([
            "ffmpeg", "-y", "-i", webm_path,
            "-ar", "16000", "-ac", "1", "-sample_fmt", "s16",
            wav_path
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # 3. Transcribe with whisper.cpp
        subprocess.run([
            os.path.join(WHISPER_PATH, "main.exe"),
            "-m", os.path.join(WHISPER_PATH, MODEL_NAME),
            "-f", wav_path,
            "-otxt"
        ], check=True, stdout=subprocess.DEVNULL)

        # 4. Read transcript
        with open(txt_path, "r", encoding="utf-8") as f:
            text = f.read().strip()

        # 5. Generate reply
        reply = openai_offline_reply(text)

        # 6. Text-to-speech (if not Kurdish)
        lang = detect_language(text)
        if lang not in ("ku", "ckb"):
            # This calls into your vitalbrain.text_to_speech
            text_to_speech(reply, lang, out_path=mp3_path)

        # 7. Return JSON
        return jsonify({
            "text":  text,
            "reply": reply,
            "lang":  lang,
            "mp3":   f"/audio/{audio_id}.mp3" if os.path.exists(mp3_path) else None
        })

    except Exception as e:
        print("ERROR in /transcribe:", e)
        return jsonify({"error": str(e)}), 500

@app.route("/audio/<filename>")
def send_audio(filename):
    # Serve the generated MP3 back to the browser
    return send_file(os.path.join(TEMP_DIR, filename), mimetype="audio/mpeg")

if __name__ == "__main__":
    # Run on all interfaces, port 5000
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 7cb058c207c6b6ed161b514703ee245b665d0829
