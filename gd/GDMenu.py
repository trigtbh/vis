import blessed 
from PIL import Image
from bottom_menu import colors, draw_square, draw_spike, draw_text
import os

terminal = blessed.Terminal()
os.system('cls')


def draw_gd_icon(width:int, height:int, x: int, y: int, main_color:str, secondary_color:str):

    # Drawing the main body

    draw_square(int(width*1.12), int(height*1.16), int(x*0.88), int(y*0.96), 'light_'+main_color)
    draw_square(width, height, x, y, main_color)
    draw_square(int(width*1.06), int(height*0.08), int(x), int(y*1.92), 'dark_'+main_color)
    draw_square(int(width*0.08), int(height), int(x+width), int(y), 'dark_'+main_color)
    draw_square(int(width*0.08), int(height*0.08), int(x+width), int(y*0.96), 'mid_'+main_color)
    draw_square(int(width*0.08), int(height*0.08), int(x*0.88), int(y*1.92), 'mid_'+main_color)

    # Drawing the eyes

    draw_square(int(width*0.25), int(height*0.3), x+int(width*0.16), y+int(height*0.18), secondary_color)
    draw_square(int(width*0.15), int(height*0.15), x+int(width*0.16), y+int(height*0.18), 'light_'+secondary_color)

    draw_square(int(width*0.25), int(height*0.3), x+int(width*0.6)+1, y+int(height*0.18), secondary_color)
    draw_square(int(width*0.15), int(height*0.15), x+int(width*0.6)+1, y+int(height*0.18), 'light_'+secondary_color)

    # Drawing the mouth

    draw_square(int(width*0.73), 2*int(height*0.18), x+int(width*0.16), y+int(height*0.66), secondary_color)
    draw_square(int(width*0.63), 2*int(height*0.1), x+int(width*0.16), y+int(height*0.66), 'light_'+secondary_color)


def draw_button0(outline=False):

    # If outline is True, draw a white outline around the button

    if outline:

        draw_square(int(terminal.width*0.32), int(terminal.height*0.5), int(terminal.width*0.01), int(terminal.height*0.3), 'white')

    else:
        draw_square(int(terminal.width*0.32), int(terminal.height*0.5), int(terminal.width*0.01), int(terminal.height*0.3), 'black')

    # Drawing the "Customize Icon" button to the screen
        
    draw_square(int(terminal.width*0.295), int(terminal.height*0.46), int(terminal.width*0.02), int(terminal.height*0.32), 'green')

    # Drawing the GD icon on the button

    draw_gd_icon(int(terminal.width*0.21), int(terminal.height*0.34), int(terminal.width*0.06), int(terminal.height*0.38), 'yellow', 'blue2')


def draw_button1(outline=False):

    # If outline is True, draw a white outline around the button

    if outline:

        draw_square(int(terminal.width*0.32), int(terminal.height*0.64), int(terminal.width*0.34), int(terminal.height*0.23), 'white')

    else:
        draw_square(int(terminal.width*0.32), int(terminal.height*0.64), int(terminal.width*0.34), int(terminal.height*0.23), 'black')

    # Drawing the "Play" button to the screen

    draw_square(int(terminal.width*0.3), int(terminal.height*0.6), int(terminal.width*0.35), int(terminal.height*0.24), 'green')

    # Drawing the play icon to the screen

    draw_spike(int(terminal.width*0.05), int(terminal.width*0.43), int(terminal.height*0.35), 'cerulean', True)


def draw_button2(outline=False):

    # If outline is True, draw a white outline around the button

    if outline:

        draw_square(int(terminal.width*0.315), int(terminal.height*0.5), int(terminal.width*0.68), int(terminal.height*0.29), 'white')

    else:
        draw_square(int(terminal.width*0.315), int(terminal.height*0.5), int(terminal.width*0.68), int(terminal.height*0.29), 'black')

    # Drawing the "Level Editor" button to the screen

    draw_square(int(terminal.width*0.29), int(terminal.height*0.46), int(terminal.width*0.69), int(terminal.height*0.32), 'green')

    

    # Yes, I know this part should probably be in a function but it's very late and I'll have to mess with numbers again- problem for future me

    # Drawing the hammer icon onto the screen

    draw_square(int(terminal.width*0.2), int(terminal.height*0.1), int(terminal.width*0.74), int(terminal.height*0.4), 'grey')
    draw_square(int(terminal.width*0.16), int(terminal.height*0.04), int(terminal.width*0.76), int(terminal.height*0.38), 'grey')
    draw_square(int(terminal.width*0.16), int(terminal.height*0.04), int(terminal.width*0.76), int(terminal.height*0.48), 'grey')
    draw_square(int(terminal.width*0.12), int(terminal.height*0.04), int(terminal.width*0.78), int(terminal.height*0.36), 'grey')
    draw_square(int(terminal.width*0.12), int(terminal.height*0.04), int(terminal.width*0.78), int(terminal.height*0.52), 'grey')
    
    draw_square(int(terminal.width*0.04), int(terminal.height*0.2), int(terminal.width*0.82), int(terminal.height*0.54), 'brown')


