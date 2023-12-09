from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os

mixer.init()

def play_song(song_name_var: StringVar, songs_listbox: Listbox, status_var: StringVar):
    song_name_var.set(songs_listbox.get(ACTIVE))

    mixer.music.load(songs_listbox.get(ACTIVE))
    mixer.music.play()

    status_var.set("Song PLAYING")

def stop_song(status_var: StringVar):
    mixer.music.stop()
    status_var.set("Song STOPPED")

def load_songs(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))

    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)

def pause_song(status_var: StringVar):
    mixer.music.pause()
    status_var.set("Song PAUSED")

def resume_song(status_var: StringVar):
    mixer.music.unpause()
    status_var.set("Song RESUMED")

root = Tk()
root.geometry('700x220')
root.title('Music Player')
root.resizable(0, 0)

song_frame = LabelFrame(root, text='Current Song', bg='LightBlue', width=400, height=80)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons', bg='Turquoise', width=400, height=120)
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text='Playlist', bg='RoyalBlue')
listbox_frame.place(x=400, y=0, height=200, width=300)

current_song_var = StringVar(root, value='<Not selected>')
song_status_var = StringVar(root, value='<Not Available>')

playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)

Label(song_frame, text='CURRENTLY PLAYING:', bg='LightBlue', font=('Times', 10, 'bold')).place(x=5, y=20)

song_label = Label(song_frame, textvariable=current_song_var, bg='Goldenrod', font=("Times", 12), width=25)
song_label.place(x=150, y=20)

pause_button = Button(button_frame, text='Pause', bg='Aqua', font=("Georgia", 13), width=7,
                      command=lambda: pause_song(song_status_var))
pause_button.place(x=15, y=10)

stop_button = Button(button_frame, text='Stop', bg='Aqua', font=("Georgia", 13), width=7,
                    command=lambda: stop_song(song_status_var))
stop_button.place(x=105, y=10)

play_button = Button(button_frame, text='Play', bg='Aqua', font=("Georgia", 13), width=7,
                    command=lambda: play_song(current_song_var, playlist, song_status_var))
play_button.place(x=195, y=10)

resume_button = Button(button_frame, text='Resume', bg='Aqua', font=("Georgia", 13), width=7,
                      command=lambda: resume_song(song_status_var))
resume_button.place(x=285, y=10)

load_button = Button(button_frame, text='Load Directory', bg='Aqua', font=("Georgia", 13), width=35,
                    command=lambda: load_songs(playlist))
load_button.place(x=10, y=55)

Label(root, textvariable=song_status_var, bg='SteelBlue', font=('Times', 9), justify=LEFT).pack(side=BOTTOM, fill=X)

root.update()
root.mainloop()
