import tkinter as t, workwith, one_player as one_player, two_player, bot_player as b

def start():
    global select
    select = t.Tk()
    select.title('Player Selection')
    select.configure(bg=workwith.background)
    
    def one():
        player = f"{p1.get()}: "
        mode = mode_variable.get()
        if mode == '501':
            mode = 501
        elif mode == '301':
            mode = 301
        elif mode == '170':
            mode = 170
        elif mode == 'Random':
            mode = 'rand'
        one_player.start(player, mode)
        
    def two():
        player1 = f"{p1.get()}: "
        player2 = f"{p2.get()}: "
        if rounds_entry.get() != "":
            rounds = int(rounds_entry.get())
        else:
            rounds = None
        mode = mode_variable.get()
        if mode == '501':
            mode = 501
        elif mode == '301':
            mode = 301
        elif mode == '170':
            mode = 170
        elif mode == 'Random':
            mode = 'rand'
        two_player.start(player1, player2, rounds, mode)
        
    def bot():
        player1 = f"{p1.get()}: "
        player2 = f"Bot Player:"
        if rounds_entry.get() != "":
            rounds = int(rounds_entry.get())
        else:
            rounds = None
        mode = mode_variable.get()
        if mode == '501':
            mode = 501
        elif mode == '301':
            mode = 301
        elif mode == '170':
            mode = 170
        elif mode == 'Random':
            mode = 'rand'
        if lvl_var.get() == 'Hobby':
            bot_mode = 'h'
        else:
            bot_mode = 'p'
        if first_player.get() == 'Bot':
            first = 2
        elif first_player.get() == 'Player':
            first = 1
        elif first_player.get() == 'Random':
            first = 0
        else:
            first = 0
        b.start(player1, player2, rounds, mode, bot_mode, first)
        
    p1variable = t.StringVar()
    p2variable = t.StringVar()

    p1variable.set('Player 1')
    p2variable.set('Player 2')

    p1 = t.Entry(select, textvariable=p1variable, font=workwith.font2, bg=workwith.background)
    p2 = t.Entry(select, textvariable=p2variable, font=workwith.font2, bg=workwith.background)

    lvl_var = t.StringVar(select)
    lvl_var.set('Hobby')
    first_player = t.StringVar(select)
    first_player.set('Random')

    select_one = t.Button(select, text='1 player', font=workwith.font2, command=one, bg=workwith.background)
    select_two = t.Button(select, text='2 player', font=workwith.font2, command=two, bg=workwith.background)
    select_bot = t.Button(select, text='Bot', font=workwith.font2, command=bot, bg=workwith.background)
    select_lvl = t.OptionMenu(select, lvl_var, 'Hobby', 'Pro')
    select_first = t.OptionMenu(select, first_player, 'Player', 'Bot', 'Random')
    
    p1.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
    p2.grid(row=1, column=0, padx=10, pady=10, sticky='ne')

    select_one.grid(row=2, column=0, padx=10, pady=10, sticky='nw')
    select_two.grid(row=2, column=0, padx=10, pady=10, sticky='ne')
    select_bot.grid(row=2, column=1, padx=10, pady=10, sticky='ne')
    select_lvl.grid(row=2, column=2, padx=10, pady=10, sticky='nw')
    select_first.grid(row=2, column=2, padx=10, pady=10, sticky='sw')

    mode = t.Label(select, text='Mode:', font=workwith.font2, bg=workwith.background)
    mode.grid(row=0, column=1, padx=10, pady=10, sticky='ne')

    mode_variable = t.StringVar(select)
    mode_variable.set('501')

    mode_dropdown = t.OptionMenu(select, mode_variable, '501', '301', '170', 'Random')
    mode_dropdown.config(font=workwith.font2, bg=workwith.background)
    mode_dropdown.grid(row=0, column=2, padx=10, pady=10)

    rounds = t.Label(select, text='Legs:', font=workwith.font2, bg=workwith.background)
    rounds.grid(row=1, column=1, padx=10, pady=10, sticky='ne')

    rounds_entry = t.Entry(select, font=workwith.font2, bg=workwith.background, width=5)
    rounds_entry.grid(row=1, column=2, padx=10, pady=10, sticky='nw')

    select.mainloop()
