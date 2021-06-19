import pyttsx3
import ffmpeg

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate) 
engine.say("hello world. こんにちは世界")
engine.save_to_file("hello world. こんにちは世界", 'hello.mp3')
engine.runAndWait()

stream = ffmpeg.input('hello.mp3')
stream = ffmpeg.output(stream,"hello2.mp3")
ffmpeg.run(stream)