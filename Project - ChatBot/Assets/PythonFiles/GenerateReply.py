import Assets.PythonFiles.Variables as vary
import os
import subprocess as sp
import requests
import wikipedia
try:
    import pywhatkit as kit
except Exception as e:
    print(e)


def checking_history(text):
    vary.reply = ''
    vary.do_not_understand = True

    for i in vary.history:
        if not ('what' in text) and ('is' in text) and ('name' in text) in i:
            a, b = i.split('-')
            if a in text:
                vary.reply = b
                vary.do_not_understand = False
                break

    if vary.do_not_understand:
        start(text)


def start(text):
    vary.reply = ''
    vary.do_not_understand = True

    if ('hello' in text) or ('hi' in text):
        vary.reply = 'Hello there, What can I do for you?'
        vary.do_not_understand = False

    elif ('what' in text) and ('can' in text) and ('you' in text) and ('do' in text):
        vary.reply = 'I am a simple chatbot. I can open apps you like and can provide information you need using internet. I can also perform internet searches for you.'
        vary.do_not_understand = False

    elif ('what' in text) and ('is' in text) and ('my' in text) and ('name' in text):
        vary.reply = f'Your name is {vary.user_name}'
        vary.do_not_understand = False

    elif ('what' in text) and ('is' in text) and ('your' in text) and ('name' in text):
        vary.reply = f'My name is {vary.bot_name}'
        vary.do_not_understand = False

    elif ('how' in text) and ('are' in text) and ('you' in text):
        vary.reply = 'I am fine. Thank you for asking. How are you doing?'
        vary.do_not_understand = False

    elif ('i' in text) and ('am' in text) and ('fine' in text):
        vary.reply = 'Good to hear about that.'
        vary.do_not_understand = False

    elif 'bye' in text:
        vary.reply = 'Bye. Have a nice day.'
        vary.do_not_understand = False

    if vary.do_not_understand:
        open_apps(text)


def open_apps(text):
    if 'open' in text:
        if 'camera' in text:
            vary.reply = 'Opening Camera...'
            sp.run('start microsoft.windows.camera:', shell=True)
            vary.do_not_understand = False
        elif 'notepad' in text:
            vary.reply = 'Opening Notepad...'
            os.system('start notepad')
            vary.do_not_understand = False
        elif 'explorer' in text:
            vary.reply = 'Opening File Explorer...'
            os.system('start explorer')
            vary.do_not_understand = False
        elif ('task' in text) and ('manager' in text):
            vary.reply = 'Opening Task Manager...'
            os.system('start taskmgr')
            vary.do_not_understand = False
        elif 'calculator' in text:
            vary.reply = 'Opening Calculator...'
            os.system('start calc')
            vary.do_not_understand = False
        elif 'edge' in text:
            vary.reply = 'Opening Microsoft Edge...'
            os.startfile(vary.paths['edge'])
            vary.do_not_understand = False
        elif 'chrome' in text:
            vary.reply = 'Opening Google Chrome...'
            os.startfile(vary.paths['chrome'])
            vary.do_not_understand = False
        elif 'zoom' in text:
            vary.reply = 'Opening Zoom...'
            os.startfile(vary.paths['zoom'])
            vary.do_not_understand = False
        elif ('vscode' in text) or ('code' in text):
            vary.reply = 'Opening Visual Studio Code...'
            os.startfile(vary.paths['vscode'])
            vary.do_not_understand = False
        elif 'pycharm' in text:
            vary.reply = 'Opening PyCharm...'
            os.startfile(vary.paths['pycharm'])
            vary.do_not_understand = False
        elif 'intellij' in text:
            vary.reply = 'Opening IntelliJ IDEA...'
            os.startfile(vary.paths['intellij'])
            vary.do_not_understand = False
        elif 'krita' in text:
            vary.reply = 'Opening Krita...'
            os.startfile(vary.paths['krita'])
            vary.do_not_understand = False
        elif 'steam' in text:
            vary.reply = 'Opening Steam...'
            os.startfile(vary.paths['steam'])
            vary.do_not_understand = False
        elif 'word' in text:
            vary.reply = 'Opening Microsoft Word...'
            os.startfile(vary.paths['word'])
            vary.do_not_understand = False
        elif 'excel' in text:
            vary.reply = 'Opening Microsoft Excel...'
            os.startfile(vary.paths['excel'])
            vary.do_not_understand = False
        elif 'powerpoint' in text:
            vary.reply = 'Opening Microsoft Powerpoint...'
            os.startfile(vary.paths['powerpoint'])
            vary.do_not_understand = False
        elif ('terminal' in text) or ('cmd' in text) or ('command' and 'prompt' in text):
            vary.reply = 'Opening a Terminal...'
            os.system('start cmd')
            vary.do_not_understand = False

    if vary.do_not_understand:
        search_youtube_video(text)


def search_youtube_video(text):
    if 'play' and 'youtube' in text:
        try:
            text = text.replace('play', '')
            text = text.replace('youtube', '')
            text = text[2:]
            kit.playonyt(text)
            vary.reply = 'Playing video...'
        except:
            vary.reply = 'Your computer is not connected to a network at this moment. So I am unable to provide an answer to your question.'

        vary.do_not_understand = False

    if vary.do_not_understand:
        search_in_google(text)


def search_in_google(text):
    if 'search' in text:
        try:
            text = text.replace('search', '')
            text = text[1:]
            kit.playonyt(text)
            vary.reply = 'Searching...'
            kit.search(text)
        except:
            vary.reply = 'Your computer is not connected to a network at this moment. So I am unable to provide an answer to your question.'

        vary.do_not_understand = False

    if vary.do_not_understand:
        tell_a_joke(text)


def tell_a_joke(text):
    if 'joke' in text:
        try:
            headers = {
                'Accept': 'application/json'
            }
            res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
            vary.reply = res['joke']
        except:
            vary.reply = 'Your computer is not connected to a network at this moment. So I am unable to provide an answer to your question.'
        vary.do_not_understand = False

    if vary.do_not_understand:
        do_not_understand(text)


def do_not_understand(text):
    try:
        vary.reply = wikipedia.summary(text, sentences=2)
    except:
        vary.reply = 'Sorry, I am having troubles to understand what you are saying. Please repeat the question.'

