width = 350
height = 530

with open('Assets\Data\colors.txt', 'r') as f:
    lines = f.read().splitlines()

with open('Assets\Data\\names.txt', 'r') as f:
    lines_1 = f.read().splitlines()

with open('Assets\Data\\fonts.txt', 'r') as f:
    lines_2 = f.read().splitlines()

with open('Assets\Data\\history.txt', 'r') as f:
    history = f.read().splitlines()

chat_inp = []
chat_rep = []

icon = open('Assets\Data\icon.txt', 'r').read()

bg_clr = lines[0]
widget_clr = lines[1]
widget_hover_clr = lines[2]
chat_bg_clr = lines[3]
chat_send_clr = lines[4]
chat_receive_clr = lines[5]

bot_name = lines_1[0]
user_name = lines_1[1]

font_name = lines_2[0]
font_size = int(lines_2[1])
font_clr = lines_2[2]

iterator = 1
inp = ''
reply = ''

menu_show = False
settings_show = False
do_not_understand = True

paths = {
    'zoom': 'C:\\Users\DELL\AppData\Roaming\Zoom\\bin\Zoom.exe',
    'edge': "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    'vscode': '"C:\\Users\DELL\AppData\Local\Programs\Microsoft VS Code\Code.exe"',
    'pycharm': "C:\Program Files\JetBrains\PyCharm Community Edition 2023.1.2\\bin\pycharm64.exe",
    'intellij': "C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2023.1.2\\bin\idea64.exe",
    'krita': "C:\Program Files\Krita (x64)\\bin\krita.exe",
    'steam': "C:\Program Files (x86)\Steam\steam.exe",
    'chrome': "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    'excel': "C:\Program Files\Microsoft Office\\root\Office16\EXCEL.EXE",
    'powerpoint': "C:\Program Files\Microsoft Office\\root\Office16\POWERPNT.EXE",
    'word': "C:\Program Files\Microsoft Office\\root\Office16\WINWORD.EXE"
}

user_show = False
chat_show = False
