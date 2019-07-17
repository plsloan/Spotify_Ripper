import os
import glob


def main():
    response = input('Song or playlist? ')
    if response.lower()[0] == 's':
        song_link = input('Enter the song link: ')
        command = 'spotdl --song ' + song_link
        os.system(command)
    elif response.lower()[0] == 'p':
        txt_files = glob.glob("*.txt")
        playlist_link = input('Enter the playlist link: ')
        command = 'spotdl --playlist ' + playlist_link
        os.system(command)
        list_file = ''
        for txt in glob.glob("*.txt"):
            if txt not in txt_files:
                list_file = txt
        command = 'spotdl --list ' + list_file
        os.system(command)
        os.remove(list_file)


if __name__ == '__main__':
    main()
