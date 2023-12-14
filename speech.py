import pyttsx3

engine = pyttsx3.init()


def stock_voice():
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)


def config_test():
    engine.say("This is your current audio configuration is this ok?")
    engine.runAndWait( )

