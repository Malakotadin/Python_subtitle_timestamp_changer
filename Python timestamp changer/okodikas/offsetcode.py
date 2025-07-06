print("i love my boyfriend")
import re

def timefixer(sec,min):
          if sec >= 13.2:
             sec=sec - 13.2
             sec=round(sec,3)
             return sec ,min
          else:
             min=min-1
             min=int(lista[1])
             ypoloipo=sec-13.2
             sec= 60 - abs(ypoloipo)
             sec=round(sec,3)
             lista[1]=str(min)
             lista[2]=str(sec)
             lista.insert(3," --> ")
             a=":".join(lista)
             a=a.split(" --> ")
             a[1]=a[1][1:]             
             a[0] = a[0].rstrip(a[0][-1])                         
             a=" --> ".join(a)
             x=a
f = open("the-boy-and-the-heron-2023-1080p-cam-rip-trellas.srt.txt",encoding="utf-8")
i=0
a=""
demo = open("demo.txt", "w", encoding="utf-8")
for x in f: 
    
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
            sec=float(lista[2])
            sec=round(sec,3)
            print(sec)
            if sec >= 13.2:
             sec=sec - 13.2
             sec=round(sec,3)
             lista[2]=str(sec)
             lista.insert(3," --> ")
             a=":".join(lista)
             a=a.split(" --> ")
             a[1]=a[1][1:]             
             a[0] = a[0].rstrip(a[0][-1])                         
             a=" --> ".join(a)

             x=a
             print("egina protos")
            else:
             print("egina deuteros")
             min=int(lista[1])
             
             min=min - 1
             ypoloipo=sec-13.2
             sec= 60 - abs(ypoloipo)
             sec=round(sec,3)
             lista[1]=str(min)
             lista[2]=str(sec)
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