import os
import zipfile
from datetime import datetime


def archiver(action, file_path, dir_path):
    match action:
        case 'dearchive_button':
            print('dearchiving')
            try:
                with zipfile.ZipFile(file_path, 'r') as archive:
                    archive.extractall(dir_path)
                print(f'Files extracted to {dir_path}')
            except Exception as e:
                print(f'An error occurred while dearchiving: {e}')

        case 'archive_button':
            print('archiving')
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            archive_file_path = os.path.join(dir_path, f'archived_{timestamp}.zip')
            file_paths = file_path.split(';')  # Zakładamy, że pliki są oddzielone średnikami

            try:
                with zipfile.ZipFile(archive_file_path, 'w', zipfile.ZIP_DEFLATED) as archive:
                    for file_path in file_paths:
                        # Upewniamy się, że ścieżki są poprawne
                        file_path_to_add = os.path.abspath(file_path)
                        if os.path.exists(file_path_to_add):
                            arcname = os.path.relpath(file_path_to_add, dir_path)
                            print(f'Adding {file_path_to_add} to archive as {arcname}')
                            archive.write(file_path_to_add, arcname)
                        else:
                            print(f'File {file_path_to_add} does not exist and will be skipped')
                print(f'Selected files in {dir_path} archived into {archive_file_path}')
            except Exception as e:
                print(f'An error occurred while archiving: {e}')
    return
