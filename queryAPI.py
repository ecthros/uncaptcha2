import speech_recognition as sr

global r
r = sr.Recognizer()

#################### SPEECH-TO-TEXT WEB APIS ####################
###### The following functions interact with the APIs we used to query for each segment ########
###### Keys have been removed from this section #######

#Query Wit
def wit(audio):
	# recognize speech using Wit.ai
	WIT_AI_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"  # Wit.ai keys are 32-character uppercase alphanumeric strings
	try:
		#print("Wit.ai: ")
		return r.recognize_wit(audio, key=WIT_AI_KEY)
	except sr.UnknownValueError:
		print("Wit.ai could not understand audio")
		return "None"
	except sr.RequestError as e:
		print("Could not request results from Wit.ai service; {0}".format(e))
		return "None"

def bing(audio):
	BING_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	# recognize speech using Microsoft Bing Voice Recognition
	try:
		#print("Microsoft Bing Voice Recognition: ")
		return r.recognize_bing(audio, key=BING_KEY)
	except sr.UnknownValueError:
		print("Microsoft Bing Voice Recognition could not understand audio")
		return "None"
	except sr.RequestError as e:
		print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
		return "None"
	
# Query IBM
def ibm(audio):

	# recognize speech using IBM Speech to Text
	IBM_USERNAME = "xxxxxxxxxxxxxxxxxxxxxxxxxx"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
	IBM_PASSWORD = "xxxxxxxxxxxxxxxxx"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
	try:
		#print("IBM Speech to Text: ")
		return r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, show_all=False)
	except sr.UnknownValueError:
		print("IBM Speech to Text could not understand audio")
		return "None"
	except sr.RequestError as e:
		print("Could not request results from IBM Speech to Text service; {0}".format(e))
		return "None"
	
	
#Query Google Speech-To-Text
def google(audio):
	try:
		#print("Google: ")
		return r.recognize_google(audio)
	except:
		print("Google could not understand")
		return "None"
