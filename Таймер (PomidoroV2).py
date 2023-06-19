from tkinter import *
from CTkMessagebox import CTkMessagebox
from customtkinter import *
import math, customtkinter

class App(CTk):
    def read_data_in_file(self):
        self.name = str(self.ename.get())
        
        print (f'Додати {self.name}')
        self.alltime += 1
        file = open(f'{self.name}_Work.txt','a+')
        file.write(f'/n{self.name} + {self.alltime}')
        file.close()
    def timer(self):
        seconds = math.fmod(self.timerStart,60) # Получаем секунды
        minutes = math.fmod(self.timerStart/60, 60) # Получаем минуты
        hour = math.fmod(self.timerStart/60/60, 60) # Получаем часы
        
    
        # Условие если время закончилось то...
        if (self.timerStart <= 0):
            # Таймер удаляется
            self.timerStart = 0;
            # Выводит сообщение что время закончилось
            print ("Время закончилось");
        else: # Иначе
            # Создаём строку с выводом времени
            self.timeNow = str(math.trunc(hour)) + ' : ' + str(math.trunc(minutes)) + ' : ' + str(math.trunc(seconds));
            # Выводим строку в блок для показа таймера
            self.time.configure(text = '{}'.format(self.timeNow))
            self.timerStart += 1
            self.after(1000, self.pause)
            if self.timerStart % 60 == 0:
                self.read_data_in_file()
            if minutes % 10 == 0:
                # Default messagebox for showing some information
                CTkMessagebox(title="Info", message="Зроби паузу")
                self.p +=1
            
    def pause(self, m = 0):
        self.PauseButton.pack()
        self.entry.pack_forget()
        self.button.pack_forget()
        self.p += m
        
        #print(m, self.p % 2)
        if self.p % 2 == 0:            
            self.timer()
        else:
            pass
            
        
            
    
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        
        self.title("CTk example")
        self.alltime = 0
        self.name = ''        
        self.ename = StringVar() 
        self.timerS = 1 # Кількість хвилин
        self.timerStart = self.timerS * 1 # Кількість хвилин
        self.geometry("600x150")
        self.time = CTkLabel(self, text = "", font = ('Arial', 84))    
        self.time.pack()
        self.entry = CTkEntry(self,  textvariable = self.ename, placeholder_text="Назва проєкту")
        self.entry.pack()
        self.button = CTkButton(self, text="Почати", command=lambda: self.pause() )
        #self.button = CTkButton(self, text="Почати", command=lambda: [self.read_data_in_file(), self.timer()])
        self.button.pack()
        self.p = 0
        self.PauseButton = CTkButton(self, text="Пауза", command=lambda: self.pause(1) )
         
        

    # add methods to app
    def button_click(self):
        print("button click")


app = App()
app.mainloop()