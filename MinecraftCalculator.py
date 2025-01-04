from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt,QSize
import os
import sys
import random
import pygame
current_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_folder)

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setFixedSize(380,500)
        self.setWindowTitle("Minecraft Calculator")
        self.setWindowIcon(QIcon(icon_path))
        pygame.mixer.init()
        
        try:
            self.sound = pygame.mixer.Sound(sound_path)
            self.sound.set_volume(1)
        except pygame.error as e:
            print(f"Error loading sound file: {e}")
            self.sound = None  # Handle case where sound is not loaded
        
        
        self.sound_pop = pygame.mixer.Sound(sound_pathpop)
        self.sound_pop.set_volume(0.3)
        
        
        self.sound_villager = pygame.mixer.Sound(button_villager)
        self.sound_villager.set_volume(0.4)
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        
        
        self.soundcreep = pygame.mixer.Sound(creeper_path)
        self.soundcreep.set_volume(0.5)
        self.background_image()

        # Create and configure the input field
        self.input = QLineEdit()
        self.input.setReadOnly(True)
        self.grid.addWidget(self.input, 0, 0, 1, 3)  # Spans across 3 columns
        self.input.setFixedSize(360,50)
        self.input.setStyleSheet("""QLineEdit{
            color: white;
            font-size: 20px;
            font-family: impact;
            background-image: url(config/wood.jpg);
        }""")
        
        # Button 1
        button1 = QPushButton()
        self.grid.addWidget(button1, 1, 0)
        button1.setIcon(QIcon(button_path1))
        button1.setFixedSize(60, 60)
        button1.setIconSize(button1.size())
        button1.setStyleSheet("""
            QPushButton {
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            background-color:green;
           }
            QPushButton:hover{
                background-color: goldenrod;
           } 
            QPushButton:pressed {
                background-color:goldenrod;
           }""")
        
        # Button 2
        button2 = QPushButton()
        self.grid.addWidget(button2, 1, 1)
        button2.setFixedSize(60, 60)
        button2.setIcon(QIcon(button_path2))
        button2.setIconSize(button2.size())
        button2.setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")
        
        # Button 3
        button3 = QPushButton()
        self.grid.addWidget(button3, 1, 2)
        button3.setFixedSize(60, 60)
        button3.setIcon(QIcon(button_path3))
        button3.setIconSize(button3.size())
        button3.setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")

        # Button 4
        button4 = QPushButton()
        self.grid.addWidget(button4, 1, 3)
        button4.setFixedSize(60, 60)
        button4.setIcon(QIcon(button_path4))
        button4.setIconSize(button4.size())
        button4.setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
          
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")

        # Button 5
        button5 = QPushButton()
        self.grid.addWidget(button5, 2, 0)
        button5.setFixedSize(60, 60)
        button5.setIcon(QIcon(button_path5))
        button5.setIconSize(button5.size())
        button5.setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")

        # Button 6
        button6 = QPushButton()
        self.grid.addWidget(button6, 2, 1)
        button6.setFixedSize(60, 60)
        button6.setIcon(QIcon(button_path6))
        button6.setIconSize(button6.size())
        button6.setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")

        # Button 7
        button7 = QPushButton()
        self.grid.addWidget(button7, 2, 2)  # Fixed placement of button7
        button7.setFixedSize(60, 60)
        button7.setIcon(QIcon(button_path7))
        button7.setIconSize(button7.size())
        button7.setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")

        
        # Button 8
        button8 = QPushButton()
        self.grid.addWidget(button8, 2, 3)  # Fixed placement of button8
        button8.setFixedSize(60, 60)
        button8.setIcon(QIcon(button_path8))
        button8.setIconSize(button8.size())
        button8.setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")
        
        # Button 9
        button9 = QPushButton()
        self.grid.addWidget(button9, 3, 0)  # Fixed placement of button9
        button9.setFixedSize(60, 60)
        button9.setIcon(QIcon(button_path9))
        button9.setIconSize(button9.size())
        button9.setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")
        
        # Button 0
        button0 = QPushButton()
        self.grid.addWidget(button0, 3, 1)  # Fixed placement of button0
        button0.setFixedSize(60, 60)
        button0.setIcon(QIcon(button_path0))
        button0.setIconSize(button0.size())
        button0.setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")
        
        # Button +
        buttonplus = QPushButton()
        self.grid.addWidget(buttonplus, 3, 2)  # Fixed placement of button+
        buttonplus.setFixedSize(60, 60)
        buttonplus.setIcon(QIcon(button_pathplus))
        buttonplus.setIconSize(buttonplus.size())
        buttonplus.setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")
        
        # Button -
        buttonminus = QPushButton()
        self.grid.addWidget(buttonminus, 3, 3)  # Fixed placement of button-
        buttonminus.setFixedSize(60, 60)
        buttonminus.setIcon(QIcon(button_pathminus))
        buttonminus.setIconSize(buttonminus.size())
        buttonminus.setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")
        
        # Button divide
        buttondivide = QPushButton()
        self.grid.addWidget(buttondivide, 4, 0)  # Fixed placement of button divide
        buttondivide.setFixedSize(60, 60)
        buttondivide.setIcon(QIcon(button_pathdivide))
        buttondivide.setIconSize(buttondivide.size())
        buttondivide.setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")
        
        # Button multiply
        buttonmultiply = QPushButton()
        self.grid.addWidget(buttonmultiply, 4, 1)  # Fixed placement of button divide
        buttonmultiply .setFixedSize(60, 60)
        buttonmultiply .setIcon(QIcon(button_pathmultiply))
        buttonmultiply .setIconSize(buttonmultiply .size())
        buttonmultiply .setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")
        
         # Button equals
        buttonequal = QPushButton()
        self.grid.addWidget(buttonequal, 4, 2)  # Fixed placement of button divide
        buttonequal .setFixedSize(60, 60)
        buttonequal.setIcon(QIcon(button_pathequal))
        buttonequal .setIconSize(buttonequal .size())
        buttonequal .setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")
        
         # Button clear
        buttonclear = QPushButton()
        self.grid.addWidget(buttonclear, 4, 3)  # Fixed placement of button divide
        buttonclear .setFixedSize(60, 60)
        buttonclear.setIcon(QIcon(button_pathclear))
        buttonclear .setIconSize(buttonclear .size())
        buttonclear .setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")
        
         # Button Music
        buttonmusic = QPushButton()
        self.grid.addWidget(buttonmusic, 5, 0)  # Fixed placement of button divide
        buttonmusic .setFixedSize(60, 60)
        buttonmusic.setIcon(QIcon(button_pathmusic))
        buttonmusic .setIconSize(buttonmusic .size())
        buttonmusic .setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")
        
        # Button stop Music
        buttonstopmusic = QPushButton()
        self.grid.addWidget(buttonstopmusic, 5, 1)  # Fixed placement of button divide
        buttonstopmusic .setFixedSize(60, 60)
        buttonstopmusic.setIcon(QIcon(button_stopmusic))
        buttonstopmusic .setIconSize(buttonstopmusic .size())
        buttonstopmusic .setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: goldenrod;
                }
            QPushButton:pressed{
                background-color:goldenrod;
                }""")
        # Button Villager
        buttonvillager = QPushButton()
        self.grid.addWidget(buttonvillager, 5, 2)  # Fixed placement of button divide
        buttonvillager .setFixedSize(60, 60)
        buttonvillager.setIcon(QIcon(villager_photo ))
        buttonvillager .setIconSize(buttonvillager .size())
        buttonvillager .setStyleSheet("""
            QPushButton{
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            }
            QPushButton:hover{
                background-color: transparent;
                }
            QPushButton:pressed{
                background-color:transparent;
                }""")
        
        
        # Button Creeper
        buttoncreeper = QPushButton()
        self.grid.addWidget(buttoncreeper, 5, 3)
        buttoncreeper.setIcon(QIcon(creeper_icon))
        buttoncreeper.setFixedSize(60, 60)
        buttoncreeper.setIconSize(buttoncreeper.size())
        buttoncreeper.setStyleSheet("""
            QPushButton {
            color : black;
            font-family: impact;
            font-size:19px;
            border-radius:14px;
            background-color:green;
           }
            QPushButton:hover{
                background-color: goldenrod;
           } 
            QPushButton:pressed {
                background-color:goldenrod;
           }""")
        
        button1.clicked.connect(lambda:self.show_input("1")) 
        button2.clicked.connect(lambda:self.show_input("2")) 
        button3.clicked.connect(lambda:self.show_input("3")) 
        button4.clicked.connect(lambda:self.show_input("4")) 
        button5.clicked.connect(lambda:self.show_input("5")) 
        button6.clicked.connect(lambda:self.show_input("6")) 
        button7.clicked.connect(lambda:self.show_input("7")) 
        button8.clicked.connect(lambda:self.show_input("8")) 
        button9.clicked.connect(lambda:self.show_input("9")) 
        button0.clicked.connect(lambda:self.show_input("0")) 
        buttonplus.clicked.connect(lambda:self.show_input("+")) 
        buttonminus.clicked.connect(lambda:self.show_input("-")) 
        buttonmultiply.clicked.connect(lambda:self.show_input("×")) 
        buttondivide.clicked.connect(lambda:self.show_input("÷"))
        buttonclear.clicked.connect(lambda:self.clear())
        buttonclear.clicked.connect(lambda:self.pop())
        buttonequal.clicked.connect(lambda:self.add())
        buttonmusic.clicked.connect(lambda:self.play_music())
        buttonmusic.clicked.connect(lambda:self.pop())
        buttonstopmusic.clicked.connect(lambda:self.stop_music())
        buttonvillager.clicked.connect(lambda:self.villager())
        buttoncreeper.clicked.connect(lambda:self.creeper())
        
    def background_image(self):
        # Create a QLabel for the background
        self.background_label = QLabel(self)
        pixmap = QPixmap(bg_path)
        
        # Scale the pixmap to fit the window
        pixmap = pixmap.scaled(self.width(), self.height(), Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        self.background_label.setPixmap(pixmap)
        
        # Make the QLabel fill the entire window
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.lower()  # Sends the image to the back so that widgets can be shown on it
        
        
    def creeper(self):
        self.soundcreep.play()
    def villager(self):
        self.sound_villager.play()
    def pop(self):
        self.sound_pop.play()    
    def show_input(self,value):
        current_text = self.input.text()
        self.input.setText(current_text+value)
        self.sound_pop.play()
    
    def clear(self,):    
        self.input.clear()
    def stop_music(self):
        self.sound.stop()    
    def add(self):
     try:
        # Get the current text from the input field
        current_text = self.input.text()
        current_text = current_text.replace('×',"*").replace('÷','//')

        # Use eval to evaluate the expression entered by the user
        result = eval(current_text)
        result = float(result)
        # Set the result to the input field
        self.input.setText(f"{result:10f}".rstrip('0').rstrip('.'))
        
     except Exception as e:
        # If there is an error in the evaluation, show an error message
        self.input.setText("Error")
       
    def play_music(self):
        self.sound.play()
        
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# Define the paths to the icon and images
icon_path = os.path.join(base_path, "Config", "Minecraft.ico")
bg_path = os.path.join(base_path, "Config", "Minecraft1.jpg")
button_path1 = os.path.join(base_path, "Config", "Dirt1.png")
button_path2 = os.path.join(base_path, "Config", "Dirt2.png")
button_path3 = os.path.join(base_path, "Config", "Dirt3.png")
button_path4 = os.path.join(base_path, "Config", "Dirt4.png")
button_path5 = os.path.join(base_path, "Config", "Dirt5.png")
button_path6 = os.path.join(base_path, "Config", "Dirt6.png")
button_path7 = os.path.join(base_path, "Config", "Dirt7.png")
button_path8 = os.path.join(base_path, "Config", "Dirt8.png")
button_path9 = os.path.join(base_path, "Config", "Dirt9.png")
button_path0 = os.path.join(base_path, "Config", "Dirt0.png")
button_pathplus = os.path.join(base_path, "Config", "Dirtplus.png")
button_pathminus = os.path.join(base_path, "Config", "Dirtminus.png")
button_pathdivide = os.path.join(base_path, "Config", "Dirtdivide.png")
button_pathmultiply = os.path.join(base_path, "Config", "Dirtmultiply.png")
button_pathequal = os.path.join(base_path, "Config", "Dirt=.png")
button_pathclear = os.path.join(base_path, "Config", "Dirtlava.png")
button_pathmusic = os.path.join(base_path,"Config","Dirtimage.png")
sound_path = os.path.join(base_path,"Config","Music.mp3")
sound_pathpop = os.path.join(base_path,"Config","Pop.mp3")
button_stopmusic = os.path.join(base_path,"Config","stop.png")
button_villager = os.path.join(base_path,"Config","Villager.mp3")
villager_photo = os.path.join(base_path,"Config","villager.png")
creeper_path = os.path.join(base_path,"Config","creeper.mp3")
creeper_icon = os.path.join(base_path,"Config","creeper.png")


if __name__ == "__main__":
    
    
    
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
