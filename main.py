from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import poke_api


root = Tk()


#This is leftover from when I started making the script - now it's just used for size of info group. probably totally unecessary
win_width = 1200

win_height = 800

root.title('Pokemon Information')

pokemon = StringVar()

entry_group = Frame(root)
entry_group.grid(column=0, row=0, columnspan=2)

poke_entry = Entry(entry_group, textvariable=pokemon)
poke_entry.grid(column = 1, row=0, padx=10, pady=10)

poke_name_label = Label(entry_group, text='Pokemon Name:')
poke_name_label.grid(column=0, row=0, padx=10, pady=10)

search_button = Button(entry_group, text='Get Info', command=lambda: get_pokemon_info())
search_button.grid(column=2, row=0, padx=10, pady=10)

info_group = LabelFrame(root, height = int(2/3*win_height), 
                        width = int(1/3*win_width), text="Info")
info_group.grid(column=0, row=1, padx=10, pady=10, sticky='n')

Label(info_group, text="Height:").grid(column=0, row=0, padx=10, pady=10)
Label(info_group, text="Weight:").grid(column=0, row=1, padx=10, pady=10)
Label(info_group, text="Type: ").grid(column=0, row=2, padx=10, pady=10)

stats_group = LabelFrame(root, text="Stats")
stats_group.grid(column=1, row=1, padx=10, pady=10, sticky='n')

Label(stats_group, text="HP: ").grid(column=0, row=0, padx=10, pady=10, sticky='e')
Label(stats_group, text="Attack: ").grid(column=0, row=1, padx=10, pady=10, sticky='e')
Label(stats_group, text="Defense: ").grid(column=0, row=2, padx=10, pady=10, sticky='e')
Label(stats_group, text="Special Attack: ").grid(column=0, row=3, padx=10, pady=10, sticky='e')
Label(stats_group, text="Special Defense: ").grid(column=0, row=4, padx=10, pady=10, sticky='e')
Label(stats_group, text="Speed: ").grid(column=0, row=5, padx=10, pady=10, sticky='e')



def get_pokemon_info():
    
    if pokemon.get() == '' or pokemon.get().isspace():
        return
    poke_info = poke_api.get_pokemon_info(pokemon.get())
    if poke_info is None:
        messagebox.showerror(title="Error", message=f'Unable to fetch information for {pokemon.get()} from the PokeAPI')
        return
        

    height = poke_info['height']
    weight = poke_info['weight']
    types = ''
    if len(poke_info['types']) > 1:
        for slot in poke_info['types']:
            if types=='':
                types+=slot['type']['name'].capitalize()
            else:
                types+=', '+slot['type']['name'].capitalize()
    else:
        types = poke_info['types'][0]['type']['name'].capitalize()
    height_label = Label(info_group, text=str(height)+' dm')
    height_label.grid(column=1, row=0, padx=10, pady=10)
    weight_label = Label(info_group, text=str(weight)+' hg')
    weight_label.grid(column=1, row=1, padx=10, pady=10)
    type_label = Label(info_group, text=types)
    type_label.grid(column=1, row=2, padx=10, pady=10)

    max_hp = 255
    max_at = 190
    max_def = 230
    max_spat = 194
    max_spdef = 230
    max_speed = 180


    HP = poke_info['stats'][0]['base_stat']
    Attack = poke_info['stats'][1]['base_stat']
    Defense = poke_info['stats'][2]['base_stat']
    SpAttack = poke_info['stats'][3]['base_stat']
    SpDefense = poke_info['stats'][4]['base_stat']
    Speed = poke_info['stats'][5]['base_stat']

    HPbar = Progressbar(stats_group, orient=HORIZONTAL, length = 200, value=(HP/max_hp * 100))
    HPbar.grid(column=1, row=0, padx=10, pady=10)
    Attackbar = Progressbar(stats_group, orient=HORIZONTAL, length = 200, value = (Attack/max_at * 100))
    Attackbar.grid(column=1, row=1, padx=10, pady=10)
    Defensebar = Progressbar(stats_group, orient=HORIZONTAL, length = 200, value = (Defense/max_def * 100))
    Defensebar.grid(column=1, row=2, padx=10, pady=10)
    SpAttackbar = Progressbar(stats_group, orient=HORIZONTAL, length = 200, value = (SpAttack/max_spat * 100))
    SpAttackbar.grid(column=1, row=3, padx=10, pady=10)
    SpDefensebar = Progressbar(stats_group, orient=HORIZONTAL, length = 200, value = (SpDefense/max_spdef * 100))
    SpDefensebar.grid(column=1, row=4, padx=10, pady=10)
    Speedbar = Progressbar(stats_group, orient=HORIZONTAL, length = 200, value = (Speed/max_speed * 100))
    Speedbar.grid(column=1, row=5, padx=10, pady=10)
    

root.mainloop()