import FreeSimpleGUI as fsg

import backend_zip as bz

label_1 = fsg.Text("Choose the way I work:")
chosen_type_text = fsg.Text("", key='chosen_type_text')
# file_text = ''
active_button = ''

archive_button = fsg.Button("Archive", size=15, button_color='grey', key='archive_button')
dearchive_button = fsg.Button("Dearchive", size=15, button_color='grey', key='dearchive_button')
file_path = fsg.FilesBrowse("Choose the file", size=15, key='file_path', target='file_text')
file_text = fsg.Text(key='file_text')
dir_path = fsg.FolderBrowse("Choose the folder", size=15, key='dir_path', target='dir_text')
dir_text = fsg.Text(key='dir_text')
action_button = fsg.Button("Do the job", size=15, key='action_button', button_color='green')

layout = [
    [label_1],
    [archive_button, dearchive_button],
    [chosen_type_text],
    [file_path],
    [file_text],
    [fsg.Text()],
    [dir_path],
    [dir_text],
    [fsg.Text()],
    [action_button]
]

window = fsg.Window('Archiver', layout=layout, size=(400, 300))
while True:
    event, values = window.read()

    if event == fsg.WIN_CLOSED:
        break
    match event:
        case 'action_button':
            print(event, values)
            print(values['file_path'])
            print(values['dir_path'])
            if values['file_path'] == '' or values['dir_path'] == '':
                fsg.popup('Podaj ścieżkę do pliku i folderu!', no_titlebar=True, keep_on_top=True,
                          background_color='grey')
                continue
            if active_button == '':
                fsg.popup('Wybierz działanie!', no_titlebar=True, keep_on_top=True, background_color='grey')
                continue
            print(values['file_path'])
            print(values['dir_path'])
            bz.archiver(active_button, values['file_path'], values['dir_path'])

        case 'archive_button':
            # print("archive_button")
            active_button = 'archive_button'
            window['archive_button'].update(button_color=('white', 'black'))
            window['dearchive_button'].update(button_color=('white', 'grey'))

        case 'dearchive_button':
            # print("dearchive_button")
            active_button = 'dearchive_button'
            window['dearchive_button'].update(button_color=('white', 'black'))
            window['archive_button'].update(button_color=('white', 'grey'))

window.close()
