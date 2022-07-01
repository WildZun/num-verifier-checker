#Import numero verifier phonenumbers
from tkinter import mainloop
from phonenumbers import carrier, is_valid_number
import phonenumbers
#Import f
import sys

def readfile(filename):
    file = open(filename,'r')
    while True:
        next_line = file.readline()

        if not next_line:
            break
        ro_number = phonenumbers.parse(next_line.strip(), "FR")
        print(next_line.strip() + ": " + carrier.name_for_number(ro_number, "FR"))
        #If no carrier
        if carrier.name_for_number(ro_number, "FR") == "":
            print("No carrier")
    file.close()
    #write in output.txt number: carrier
    fileout = open("output.txt",'w')
    fileout.write("Si il ne vous affiche aucun opérateur, cela veut dire que le numéro n'est pas valide\r")
    
    for line in open(filename):
        ro_number = phonenumbers.parse(line.strip(), "FR")
        fileout.write(line.strip() + ": " + carrier.name_for_number(ro_number, "FR") + "\n")
        #If no carrier


readfile("numbers.txt")