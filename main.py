from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import poke_api


root = Tk()

win_width = 1200

win_height = 800

root.geometry(f'{win_width}x{win_height}')

root.title('Pokemon Information')

#messagebox.showinfo(message='Fortnite')

info_group = LabelFrame(root, height = int(2/3*win_height), 
                        width = int(1/3*win_width), text="Info")
info_group.grid(column=0, row=1, padx=10, pady=10)

Label(info_group, text="Height:").grid(column=0, row=0, padx=10, pady=10)
Label(info_group, text="Weight:").grid(column=0, row=1, padx=10, pady=10)
Label(info_group, text="Type: ").grid(column=0, row=2, padx=10, pady=10)

stats_group = LabelFrame(root, text="Stats")
stats_group.grid(column=1, row=1, padx=10, pady=10)

Label(stats_group, text="HP: ").grid(column=0, row=0, padx=10, pady=10)
Label(stats_group, text="Attack: ").grid(column=0, row=1, padx=10, pady=10)
Label(stats_group, text="Defense: ").grid(column=0, row=2, padx=10, pady=10)
Label(stats_group, text="Special Attack: ").grid(column=0, row=3, padx=10, pady=10)
Label(stats_group, text="Special Defense: ").grid(column=0, row=4, padx=10, pady=10)
Label(stats_group, text="Speed: ").grid(column=0, row=5, padx=10, pady=10)

weight = StringVar()
height = StringVar()
types = StringVar()

weight=''
height-''
types=''

height_label = Label(info_group, height)
height_label.grid(column=1, row=0, padx=10, pady=10)
weight_label = Label(info_group, weight)
weight_label.grid(column=1, row=1, padx=10, pady=10)
type_label = Label(info_group, types)
type_label.grid(column=1, row=2, padx=10, pady=10)

pokemon = StringVar()

def get_pokemon_info():
    try:
        poke_info = poke_api.get_pokemon_info(pokemon.get())
    except:
        messagebox.showerror(title="Error", message=f'Unable to fetch information for {pokemon.get()} from the PokeAPI')
    height = poke_info['height']
    weight = poke_info['weight']
    type_list = []
    for slot in poke_info['types']:
        type_list.append(slot['type']['name'])

    print(type_list)
    


poke_entry = Entry(root, textvariable=pokemon)
poke_entry.grid(column = 1, row=0, padx=10, pady=10)

poke_name_label = Label(root, text='Pokemon Name:')
poke_name_label.grid(column=0, row=0, padx=10, pady=10)

search_button = Button(root, text='Get Info', command=lambda: get_pokemon_info())
search_button.grid(column=2, row=0, padx=10, pady=10)


root.mainloop()