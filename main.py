import os
try:
    import PySimpleGUI as sg
    import PIL
except Exception as e:
    agree = input("Czy zgadzasz sie na zainstalowanie modulow (PySimpleGUI oraz Pillow)? (y/n): ")
    if(agree == 'y'):
        if not os.system('python -m pip install pysimplegui'):
            import PySimpleGUI as sg
        if not os.system('python -m pip install pillow'):
            import PIL
    else:
        print('Koncze dzialanie programu')
        exit(1)
    

def loadImage(window):
    inputField: sg.Input = window['filename']
    image: sg.Image = window['image']
    try:
        image.update(inputField.get(), size=(400, 300))
    except:
        print('no such file')

def chooseAction(event, window):
    if event == 'OK':
        print('Changing image')
        loadImage(window)
    if event == 'searchForCat!':
        print('searching for cat!')



sg.theme('Dark Blue 3')
layout = [
    [sg.FileBrowse(), sg.Input(key='filename')],
    [sg.OK()],
    [sg.Image(key='image', size=(400, 300), background_color='gray')],
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