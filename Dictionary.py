from ntpath import split
import os.path
from os import path

#thetoume to arxeio sto idio directory me to arxeio python.
directory = os.path.dirname(__file__) # directory of script
FILEPATH=directory+"/dict.txt"

#sunarthsh pou prosthetei lekseis sto leksilogio
def add():
        a=input("Please insert a word here: ") #xristis eisagei ti leksh (sta agglika arxika.)
       
        with  open(FILEPATH, "r") as myfile: #anoigei to arxeio
                if a in myfile.read(): #elegxei prwta an uprarxei h leksh. an uparxei paei pali sth main.
                        print("Word already exists")
                        myfile.close()
                      
                        main()
                elif(a.isnumeric()): #elegxei an o xristis plhktrologhse arithmo. an nai ksana sti main
                        print("You can't add numbers.")
                        myfile.close()
                        main()
                else: #alliws, tou zita na grapsei ti metafrash tis leskhs pou plhktrologhse.
                        myfile.close()
                        f = open(FILEPATH, "a")
                        b=input("Give the translation of the word: ")
                        f.write(a+','+b+'\n');
                        print("Word added succesfully!")

                        f.close() 
                        main()
        
#sunarthsh pou psaxnei sto arxeio an uparxoun oi lekseis pou pliktrologei o xrhsths
def search():
        c=input("Write the word you want to search for: ")
        found=False
        with  open(FILEPATH, "r") as file: #anoigoume to arxeio.
                for line in file: #gia kathe grammi sto arxeio
                        x=line.strip('\n').split(',') #kovoume ta kena kai to ,
                        if c in x: #an vrethei i leksh, tin tupwnei.
                                print('The translation of word '+c+' is: '+x[1]+'\n')
                                found=True
                                file.close() #kleinei to arxeio, vgainei apo tin epanalhpsh.
                                break
                                
        if found == False:       #an de vrethei, typwnei to analogo minuma.        
                print("Word not found in dictionary.\n")
        main() #odhgei ton xrhsth stis arxikes epiloges sth main gia na epileksei pws thelei na sunexisei.
        





#sunarthsh main.
#dinei 3 epiloges ston xristi, add, search h' eksodos. analoga me to ti pliktrologhsei tha kalesei tin antistoixh sunarthsh h' tha kleisei
def main():
        choice=input("Do you want to add or search a word in the dictionary? \nType anything else to exit.\n")
        if(choice=='add'):
                add()
        elif(choice=='search'):
                search()
        else:
                exit()


#orizoume poia sunarthsh tha pairnei ws main to programma.

if __name__== "__main__":
        #elegxei arxika an uparxei to arxeio dict.
        #an den yparxei to dimiourgei.
        print(FILEPATH)
        if os.path.isfile(FILEPATH):
                 print ("File exists")
        else:
                print ("Creating File with name: dict.txt ")
                f = open(FILEPATH, "w+") 
                f.close()
                
        main()











