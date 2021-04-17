import tkinter
import random



# zmienna, którą ułatwię sobie manipulowanie oknem
t = tkinter.Tk()

# ustawienia okna programu
t.title("Trener tabliczki mnożenia")
t.geometry("400x300")

#Definicja zdobytych punktów i wykonanych prób:
points=0 # na początku nie mamy punktów
trial=1 # a próba jest pierwsza



# definicje potrzebne aby wyświetlić działanie:
a = random.randint(2,9)
b = random.randint(2,9)
popr_wynik = a*b
dzial = "%s mnożone przez %s wynosi...\n\n Wpisz właściwy wynik:"%(a,b)

#Etykieta z działaniem
etykieta = tkinter.Label(t, text = dzial)
etykieta.pack(fill=tkinter.BOTH,expand=tkinter.YES)

def noweMnozenie(): #funkcja potrzebna by wyświetlić kolejne mnożenie
    global a
    a = random.randint(2,9)
    global b
    b = random.randint(2,9)
    global popr_wynik
    popr_wynik = a*b
    global dzial
    dzial = "%s mnożone przez %s wynosi...\n\n Wpisz właściwy wynik:"%(a,b)
    etykieta.configure(text = dzial)



#dodaj miejsce na dane od użytkownika
podany_wynik = tkinter.Entry(t)
podany_wynik.pack(expand=tkinter.YES)

#dodaj komentarz początkowy
koment = "wpisz i sprawdź wynik" 
etykieta2 = tkinter.Label(t, text = koment)
etykieta2.pack(fill=tkinter.BOTH,expand=tkinter.YES)

def commentRef(): #funkcja, która pozwoli przywracać komentarz do początkowej formy:
    koment = "wpisz i sprawdź wynik lub naciśnij zakończ by podsumować"
    etykieta2.configure(text = koment)
    przycisk1.configure(state="normal", text="Sprawdź odpowiedź")
    przycisk2.configure(state="normal", text="Zakończ") #to dlatego, że po wpisaniu wyniku na czas komentarza wyłączymy przyciski, a potem chcemy je przywrócić


#funkcja, która sprawdzi zgodność wyników i zadziała odpowiednio
def check():
    try:
        x = int(podany_wynik.get())
        if x == popr_wynik:
            koment = "podałeś poprawny wynik! \nWpisz wynik kolejnego działania!"
            global points
            points=points+1
            global trial
            trial=trial+1
            noweMnozenie()
            etykieta2.configure(text = koment)
        else:
            koment = "Źle! Powinno być %d\nWpisz wynik kolejnego działania"%(popr_wynik)
            trial=trial+1
            noweMnozenie()
            etykieta2.configure(text = koment)
    except:
        koment = "Błąd! Podano jakieś coś innego niż liczba całkowita! \n próba nie wlicza się"
        noweMnozenie()
        etykieta2.configure(text = koment)
        t.after(3000, commentRef)
    finally:
        podany_wynik.delete(0, len(podany_wynik.get())) #usunięcie dotychczasowego wyniku
        przycisk1.configure(state="disabled", text ="loading")
        przycisk2.configure(state="disabled", text ="loading") #na moment nie można nacisnąć przycisków, a tekst wskazuje, że to się zmieni
        #bez tego można było kliknąć zakończ zanim zrobił się "after" i błędy w konsoli wyskakiwały
        t.after(2000, commentRef)



#funckja, która pokaże ilość punktów na koniec
def howIdo():
    etykieta.destroy()
    etykieta2.destroy()
    przycisk1.destroy()
    przycisk2.destroy()
    podany_wynik.destroy()
    Finkoment = "Dziękujemy! \n liczba zdobytych punktów wynosi: %s \n zakończono po próbie nr: %s"%(points, trial-1)
    #odejmuje 1 od prób żeby pokazał liczbę ukończonych
    etykieta3 = tkinter.Label(t, text = Finkoment)
    etykieta3.pack(fill=tkinter.BOTH,expand=tkinter.YES)


#dodaj przycisk do akceptacji sprawdzonych danych
przycisk1 = tkinter.Button(t,text="Sprawdź odpowiedź", command=check)
przycisk1.pack(expand=tkinter.YES)

#dodaj przycisk do zakończenia:
przycisk2 = tkinter.Button(t,text="Zakończ", command=howIdo)
przycisk2.pack(expand=tkinter.YES)

#wyświetlaj główne okno cały czas:
t.mainloop()


