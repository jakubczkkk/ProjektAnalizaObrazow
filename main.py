import os

try:
    import PySimpleGUI as sg
    import test
except Exception as e:
    agree = input("Czy zgadzasz sie na zainstalowanie modulow (PySimpleGUI oraz scikit-image)? (y/n): ")
    if(agree == 'y'):
        if not os.system('python -m pip install pysimplegui'):
            import PySimpleGUI as sg
        if not os.system('python -m pip install scikit-image'):
            import test
    else:
        print('Koncze dzialanie programu')
        exit(1)
    

def chooseAction(event, window):
    if event == 'OK':
        inputField: sg.Input = window[FILEPATH]
        test.load_image(inputField.get())
    if event == 'searchForCat!':
        print('searching for cat!')



#keys
FILEPATH = 'fpath'


sg.theme('Dark Blue 3')
layout = [
    [sg.FileBrowse(), sg.Input(key=FILEPATH)],
    [sg.OK()],
    [sg.Button('searchForCat!'), sg.Text(key='text')]
]

window = sg.Window('KotoSzukaczoInator', layout, size=(1280, 720))

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED:
        break

    chooseAction(event, window)

window.close()