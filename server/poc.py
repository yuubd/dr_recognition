#import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

with sr.AudioFile('OSR_us_000_0011_8k.wav') as source:
    
    audio = r.record(source)
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        
        # using google speech recognition
        text = r.recognize_google(audio)
        print('Converting audio transcripts into text ...')
        print(text)
     
    except:
         print('Sorry.. run again...')
         

# #import library
# import speech_recognition as sr

# # Initialize recognizer class (for recognizing the speech)

# r = sr.Recognizer()

# # Reading Microphone as source
# # listening the speech and store in audio_text variable

# with sr.Microphone() as source:
#     print("Talk")
#     audio_text = r.listen(source)
#     print("Time over, thanks")
# # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
#     try:
#         # using google speech recognition
#         print("Text: "+r.recognize_google(audio_text))
#     except:
#          print("Sorry, I did not get that")


# import tensorflow as tf
# # Requires latest tf-1.4 on Windows
# from tf.keras.python.ops import audio_ops as contrib_audio
# def parse_wave_tf(filename):
#     audio_binary = tf.read_file(filename)
#     desired_channels = 1
#     wav_decoder = contrib_audio.decode_wav(
#         audio_binary,
#         desired_channels=desired_channels)
#     with tf.Session() as sess:
#         sample_rate, audio = sess.run([
#             wav_decoder.sample_rate,
#             wav_decoder.audio])
#         first_sample = audio[0][0] * (1 << 15)
#         second_sample = audio[1][0] * (1 << 15)
#         print('''
#             Parsed {filename}
#             -----------------------------------------------
#             Channels: {desired_channels}
#             Sample Rate: {sample_rate}
#             First Sample: {first_sample}
#             Second Sample: {second_sample}
#             Length in Seconds: {length_in_seconds}'''.format(
#                         filename=filename,
#                         desired_channels=desired_channels,
#                         sample_rate=sample_rate,
#                         first_sample=first_sample,
#                         second_sample=second_sample,
#                         length_in_seconds=len(audio) / sample_rate))
# parse_wave_tf('eg_1min.wav')
