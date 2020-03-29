from sys import stdin
import py_midicsv
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# timidity was used for playing MIDI files while testing in linux
# I am using >timidity example_converted.mid< in linux to play .mid files
def midi_csv(filename):
    csv_string = py_midicsv.midi_to_csv(filename)
    count=0
    for i in csv_string:
        line=i.strip().split(", ")
        if line[2] == 'Note_on_c' or line[2] == 'Note_off_c':
            count+=1
    return csv_string, count

def csv_midi(csv_file):
    midi_object = py_midicsv.csv_to_midi(csv_file)
    with open("Steganography.mid", "wb") as output_file:
        midi_writer = py_midicsv.FileWriter(output_file)
        midi_writer.write(midi_object)

def choosefile():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return filename

def hide(csv_string,bits):
    csv_hide=[]
    count=0
    countloop=0
    while countloop < len(csv_string):
        message = csv_string[countloop]
        new = message.strip().split(", ")
        if new[2] == 'Note_on_c':
            if int(new[5]) < 10 :
                new[5]=bits[count]
            else:
                new[5]=new[5][:-1]+bits[count]
            count+=1
        csv_hide.append((', '.join(new)+'\n'))
        countloop+=1
        if count==len(bits):
            break
    csv_hide += csv_string[countloop:]
    return csv_hide

def unhide(csv_hide):
    message_bits=''
    countloop=0
    while countloop < len(csv_hide):
        message = csv_hide[countloop]
        new = message.strip().split(", ")
        if new[2] == 'Note_on_c':
            if int(new[5]) < 10 :
                if int(new[5]) > 1 :
                    break
                else:
                    message_bits+=new[5]
            else:
                if int(new[5][-1]) > 1:
                    break
                else:
                    message_bits+=new[5][-1]
        countloop+=1
    decodebits(message_bits)

def decodebits(message_bits):
    message=''
    for j in range(0,len(message_bits)-1,7):
        message+=chr(int(message_bits[j:j+7],2))
    print('**************************************************************\n')
    print('The message hide in the .midi file is:', message)
    print('**************************************************************\n')


def choice1(csv,size):
    print('**************************************************************')
    print('You have',size, 'bits for write your hide message, use it with discretion.')
    print('Give me the text you want to hide in the MIDI file, whitout whitespace!\nIf the text is written in some language that uses diacritical marks I recommend rather not using it.')
    print('**************************************************************\n')
    text = stdin.readline().strip()
    bits = (' '.join(format(ord(x), 'b') for x in text))
    lbits = len(bits.replace(' ', ''))
    while lbits >= size :
        print('\n \nThe text is too big for hide in the file')
        print('Give me the text you want to hide in the MIDI file \n')
        text = stdin.readline().strip()
        bits = (' '.join(format(ord(x), 'b') for x in text))
        lbits = len(bits.replace(' ', ''))
    csv_hide =  hide(csv,bits.replace(' ', ''))

    print("\n****************The message was sucefully hide****************")
    csv_midi(csv_hide)
    # unhide(csv_hide)

def menu():
    choice='a'
    while choice!='1' and choice!='2':
        choice = input("""

                1: Hide some message in a MIDI file
                2: Expose the hide message in a MIDI file\n\nPlease enter your choice: """)

    print('Select the MIDI file\n')
    midi_file_direction = choosefile()
    csv_song,maxbits=midi_csv(midi_file_direction)
    if choice== '1':
        choice1(csv_song,maxbits)
    elif choice=='2':
        unhide(csv_song)
    pass

if __name__ == "__main__":
    print("**********************MIDI Steganography**********************")
    exit='n'
    while exit!='Y' and exit!='y':
        menu()
        exit=input('\n**************If you want to exit please enter Y/y************* ')
    print('\nBye!')
