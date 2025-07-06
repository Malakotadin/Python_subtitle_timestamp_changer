print("i love my boyfriend")
def timefixer(offset,sec,min): #συνάρτηση που κάνει τις πραξόυλες μας
          if sec >= offset:
             sec=sec - offset
             sec=round(sec,3)
             sec=str(sec)
             min=str(min)
             return sec ,min # αφήνει τα λεπτά απείραχτα
          else:
             min=min-1           #σεναριο που αλλαζω τα λεπτα
             ypoloipo=sec-offset
             sec= 60 - abs(ypoloipo)
             sec=round(sec,3)
             sec=str(sec)
             min=str(min)
             return sec,min
             
f = open("the-boy-and-the-heron-2023-1080p-cam-rip-trellas.srt.txt",encoding="utf-8") #όνομα αρχέιου , πάντα utf8 γιατι γραφεις και διαβαζεις σε ελληνικα
i=0
a=""
offset=input()
offset=float(offset)
demo = open("demo.txt", "w", encoding="utf-8")
for x in f: # για κάθε γραμμή του αρχέιου θα κανειςς το εξης και θα φορτωνεις την γραμμη στο χ
    print(x)
    if len(x)>3:
        x=x.replace(" --> ",":")
        lista=x.split(":")
        #print(lista)
        if len(lista)>1:
          #  lista[2]=lista[2].replace(" --> ","','")
            print(lista)
           # try:
            lista[2]=lista[2].replace(",",".")
            print(lista)
            print("mpika")
              # int(lista1[2])
           # except:
              #  print("ohoh")
            #else:
           #  print("egina")
            print(lista[2])
            print(lista[2][0])
            print(lista[2][1])
            lista[5]=lista[5].replace(",",".")
            sec=float(lista[2])
            
            
            lista[5]=lista[5].rstrip(lista[5][-1]) 
            lista[5]=lista[5].rstrip(lista[5][-1]) 

            min=int(lista[1])
            lista[2],lista[1]=timefixer(offset,sec,min)
            sec=float(lista[5])
            min=int(lista[4])

            lista[5],lista[4]=timefixer(offset,sec,min)
            lista[5]=lista[5]+"\n"
            lista[5]=lista[5].replace(".",",")
            lista[2]=lista[2].replace(".",",")
            #lista[1]=str(lista[1])
           # lista[2]=str(lista[2])
            print(lista)
            print("egina protos")
        
            print("egina deuteros")
            
            

            lista.insert(3," --> ")
            a=":".join(lista)
            a=a.split(" --> ")
            a[1]=a[1][1:]             
            a[0] = a[0].rstrip(a[0][-1])                         
            a=" --> ".join(a)
            x=a

    i=i+1
    print(a)
    print(f"egina {i} fores")
    
    demo.write(x)
      
  
         
    


f.close()
demo.close()
#print(lista)