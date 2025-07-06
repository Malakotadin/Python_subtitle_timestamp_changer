print("i love my boyfriend") #άμα θέλεις και να πηγαίνει μπροστά και όχι μόνο πίσω μπορείς απλώς να βάλεις άλλα δυο if σε λατρεύω 
def timefixer(offset,sec,min): #συνάρτηση που κάνει τις πραξόυλες μας
          if sec >= offset:#σεναριο που αλλαζω τα δευτερόλεπτα
             sec=sec - offset
             sec=round(sec,3)
             sec=str(sec)
             min=str(min)
             return sec ,min # αφήνει τα λεπτά απείραχτα #επιστρέφει δευτερολεπτά και λεπτά στην πρώτη και δευτερη μεταβλητή αντίστοιχα
          else:
             min=min-1           #σεναριο που αλλαζω τα δευτερόλεπτα και τα λεπτά
             ypoloipo=sec-offset
             sec= 60 - abs(ypoloipo)
             sec=round(sec,3)
             sec=str(sec) #τα ξανακάνω strings
             min=str(min)
             return sec,min #επιστρέφει δευτερολεπτά και λεπτά στην πρώτη και δευτερη μεταβλητή αντίστοιχα 
             
input_file = open("the-boy-and-the-heron-2023-1080p-cam-rip-trellas.srt.txt",encoding="utf-8") #όνομα αρχέιου , πάντα utf8 γιατι γραφεις και διαβαζεις σε ελληνικα
counter=0
modified_fileline=""
offset=input()
offset=float(offset)
output_file = open("demo.txt", "w", encoding="utf-8")
for fileline in input_file: # για κάθε γραμμή του αρχέιου θα κανειςς το εξης και θα φορτωνεις την γραμμη στο χ
    
    if len(fileline)>3: # θέλω να αλλάξω μόνο τιε γραμμές που έχουν νούμερα άρα αυτές που έχουν τον αριθμό του υπότιτλου δεν μεν οιαζουν
        fileline=fileline.replace(" --> ",":")
        lista=fileline.split(":") #δημιουργείται λίστα όπου κάθε της αντικείμενο είναι τεμάχιο του χ που θα ήταν γραμμή κώδικα
        #print(lista)
        if len(lista)>1: # Έτσι επιλέγω τις γραμμές με τα time stamps και όχι με τον διάλογο ( αφόυ ο διαλογος δεν έχει : άρα θα επέστρεφε  μόνο ένα στοιχείο)
          #  lista[2]=lista[2].replace(" --> ","','")
            print(lista)
           # try:
            lista[2]=lista[2].replace(",",".")#για να μπορώ να κάνω δεκαδικές πράξεις 
            sec=float(lista[2])#με αυτή την εντολή μετατρέπω τα στοιχεία της νοητης θέσης τον δευερολέπτωνλεπτών σε δεκαδικους αριθμους
           # print(lista)
          #  print("mpika")
              # int(lista1[2])
           # except:
              #  print("ohoh")
            #else:
           #  print("egina")
            #print(lista[2])
           #print(lista[2][0])
           # print(lista[2][1])
            lista[5]=lista[5].replace(",",".")#για να μπορώ να κάνω δεκαδικές πράξεις , κανονικά θα έπρεπε να το βάλω μέσα στην συνάρτηση μου αλλα βαριέμαι
            lista[5]=lista[5].rstrip(lista[5][-1]) #αφαιρώ το δεξί στοιχειο δυο φορές , δεν θυμαμαι γιατι
            lista[5]=lista[5].rstrip(lista[5][-1]) # θυμήθηκα υπάρχει το γαμβ \n στο τελος που προσθέτει μια γραμμή 
            sec=float(lista[5])#με αυτή την εντολή μετατρέπω τα στοιχεία της νοητης θέσης τον δευερολέπτωνλεπτών σε δεκαδικους αριθμους
            min=int(lista[1])#μετατρέπω την θέση των λεπτών απο string σε λεπτα
            lista[2],lista[1]=timefixer(offset,sec,min) # καλώ την συναρτησόυλα μου οπού γυρναει το sec στο λιστα2 και τον μιν στο λιστα1 
            
            min=int(lista[4])#μετατρέπω την θέση των λεπτών απο string σε λεπτα

            lista[5],lista[4]=timefixer(offset,sec,min)# καλώ την συναρτησόυλα μου οπού γυρναει το sec στο λιστα5 και τον μιν στο λιστα4 
            lista[5]=lista[5]+"\n"#προσθέτω το endline symbol 
            lista[5]=lista[5].replace(".",",")#ξαναβαζω τα κόμματα 
            lista[2]=lista[2].replace(".",",")
            #lista[1]=str(lista[1])
           # lista[2]=str(lista[2])
            print(lista)
           # print("egina protos")
        
           # print("egina deuteros")
            
            

            lista.insert(3," --> ")#ξαναβάζω το βέλος ανάμεσα
            modified_fileline=":".join(lista)#ξαναενώνω την λίστα σε ένα στρινγκ με : ανάμεσα του 
            modified_fileline=modified_fileline.split(" --> ") # την ξαναχωρίζω γιατί ήταν της μορφής  (δευτερολεπτα:βελος:ωρες τελος διαλογου) ωστέ να βγάλω τις δύο τελείες γύρω από το βέλος
            modified_fileline[1]=modified_fileline[1][1:]   #τις βγαζω          
            modified_fileline[0] = modified_fileline[0].rstrip(modified_fileline[0][-1])     #και με δύο διαφορετικές τεχνικές γιατι ειμαι ηλιθιος                    
            modified_fileline=" --> ".join(modified_fileline)#ξαναενώνω την λίστα μου χωρίς περεταίρω τελειες
            fileline=modified_fileline#δίνω στην μεταβλητή που έχει το string που πήρα απο το αρχικό αρχείο , την νέα χρονικά τροποποιημένη String
#ειναι το μόνο "έξυπνο" πράγμα που γίνεται σε αυτόν τον κώδικα , όταν δεν μπαίνει στο if τυπώνει ότι διάβασε , αλλά όταν μπαίνει τυπώνει την τροποποιημένη μορφή
    counter=counter+1#μιας και μόνο μέσα στο if αλλάζει τιμή η μεταβλητή της fileline
    print(modified_fileline)#άρα 2στις 3 modified_fileline==fileline
    print(f"egina {counter} fores")
    
    output_file.write(fileline)#γράφω στο νέο μου αρχείο
      
  
         
    


input_file.close()#σαν καλή πρακτική πάντα όταν ανοίγεις/φτιαχνεις ένα αρχείο πρέπει και να το κλείνεις στο τέλος του κωδικά σου
output_file.close()
#print(lista)