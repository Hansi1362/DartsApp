import tkinter as t, tts
from tkinter import messagebox
import workwith
import endmatch
import random


def start(name1, name2, rounds, mode):
    global two_player_root
    two_player_root = t.Toplevel()
    two_player_root.title("Two player")

    two_player_root.attributes('-fullscreen', True)

    end = t.Button(two_player_root, text='x', command=workwith.on_closing, font=workwith.font3)
    end.place(relx=1.0, rely=0.0, anchor='ne')

    two_player_root.protocol("WM_DELETE_WINDOW", workwith.on_closing)

    if mode == 'rand':
        number = random.randint(1, 170)
    elif mode == 501:
        number = 501
    elif mode == 301:
        number = 301
    elif mode == 170:
        number = 170
    
    def reset_game(x): 
        if mode not in [501, 301]:
            number = random.randint(1, 170)
        elif mode == 501:
            number = 501
        elif mode == 301:
            number = 301
        elif mode == 170:
            number = 170
               
        points_left_p1.set(number)
        points_left_p2.set(number)
            
        avg_points_p1.set(0)
        checkoutway_p1.set("")
        count_throws_p1.set(0)
        
        avg_points_p2.set(0)
        checkoutway_p2.set("")
        count_throws_p2.set(0)

        workwith.last_points_p1 = []
        workwith.last_points_p2 = []
        workwith.game_start = []
        if x == 'all':
            legs_p1.set(0)
            legs_p2.set(0)
    
    def game_end(winner):
        if winner == 1:
            w = name1
        elif winner == 2:
            w = name2
        reset_game('all')
        endmatch.end(w)

    # Spieler 1 Variablen
    points_left_p1 = t.IntVar(value=number)
    avg_points_p1 = t.IntVar()
    checkoutway_p1 = t.StringVar()
    count_throws_p1 = t.IntVar()
    legs_p1 = t.IntVar()
    
    player_p1 = t.Label(two_player_root, text=name1, font=workwith.font_two)
    points_p1 = t.Label(two_player_root, textvariable=points_left_p1, font=('Summer', 80))
    won_p1 = t.Label(two_player_root, textvariable=legs_p1, font=workwith.font2_two)
    
    t1_p1 = t.Entry(two_player_root, font=workwith.font_two, width=3)
    t2_p1 = t.Entry(two_player_root, font=workwith.font_two, width=3)
    t3_p1 = t.Entry(two_player_root, font=workwith.font_two, width=3)
    
    def last_points_p1():
        last_points, last_avg = workwith.reset(points_left_p1.get(), 1)
        points_left_p1.set(last_points)
        avg_points_p1.set(last_avg)
        t = count_throws_p1.get()
        count_throws_p1.set(t - 3)

    back_p1 = t.Button(two_player_root, text='Return', command=last_points_p1, font=workwith.font3_two)

    def ok1():
        throw, is_winning, points = workwith.calc(t1_p1.get(), t2_p1.get(), t3_p1.get(), points_left_p1.get(), 1)
        average, throws_p1 = workwith.get_average(1)
        t1_p1.delete(0, t.END)
        t2_p1.delete(0, t.END)
        t3_p1.delete(0, t.END)
        points_left_p1.set(throw)
        avg_points_p1.set(average)
        count_throws_p1.set(throws_p1)
        if is_winning:
            legs_p1.set(legs_p1.get() + 1)
            if legs_p1.get() == rounds:
                game_end(1)
            elif legs_p1.get != rounds:
                if workwith.game_start[0] == t1_p1 or workwith.game_start[0] == t2_p1 or workwith.game_start[0] == t3_p1:
                    tts.text_to_speech(f'Game Shot and the leg for {name1}. First dart in the next leg goes to {name2} Game on!', 'en')
                    handle_enter_game_win(2)
                    reset_game(None)
                else:
                    tts.text_to_speech(f'Game Shot and the leg for {name1}. First dart in the next leg goes to {name1} Game on!', 'en')   
                    handle_enter_game_win(1)
                    reset_game(None)         
        else:
            tts.text_to_speech(points, 'en')
        if int(throw) in workwith.dart_checkouts:
            checkoutway_p1.set(", ".join(workwith.dart_checkouts[throw][0].split(", ")))
        else:
            checkoutway_p1.set("")
        if points_left_p2.get() <= 170:
            tts.text_to_speech(f'{name2} requires {points_left_p2.get()}', 'en')

    accept_p1 = t.Button(two_player_root, text='Ok', command=ok1, font=workwith.font3_two)
    count_p1 = t.Label(two_player_root, text='Throw: ', textvariable=count_throws_p1, font=workwith.font_two)
    avg_p1 = t.Label(two_player_root, textvariable=avg_points_p1, font=workwith.font_two)
    checkout_p1 = t.Label(two_player_root, textvariable=checkoutway_p1, font=workwith.font2_two)
    
    # Spieler 2 Variablen
    points_left_p2 = t.IntVar(value=number)
    avg_points_p2 = t.IntVar()
    checkoutway_p2 = t.StringVar()
    count_throws_p2 = t.IntVar()
    legs_p2 = t.IntVar()
    
    player_p2 = t.Label(two_player_root, text=name2, font=workwith.font_two)
    points_p2 = t.Label(two_player_root, textvariable=points_left_p2, font=('Summer', 80))
    won_p2 = t.Label(two_player_root, textvariable=legs_p2, font=workwith.font2_two)
    
    t1_p2 = t.Entry(two_player_root, font=workwith.font_two, width=3)
    t2_p2 = t.Entry(two_player_root, font=workwith.font_two, width=3)
    t3_p2 = t.Entry(two_player_root, font=workwith.font_two, width=3)
    
    def last_points_p2():
        last_points, last_avg = workwith.reset(points_left_p2.get(), 2)
        points_left_p2.set(last_points)
        avg_points_p2.set(last_avg)
        t = count_throws_p2.get()
        count_throws_p2.set(t - 3)

    back_p2 = t.Button(two_player_root, text='Return', command=last_points_p2, font=workwith.font3_two)

    def ok2():
        throw, is_winning, points = workwith.calc(t1_p2.get(), t2_p2.get(), t3_p2.get(), points_left_p2.get(), 2)
        average, throws_p2 = workwith.get_average(2)
        t1_p2.delete(0, t.END)
        t2_p2.delete(0, t.END)
        t3_p2.delete(0, t.END)
        points_left_p2.set(throw)
        avg_points_p2.set(average)
        count_throws_p2.set(throws_p2)
        if is_winning:
            legs_p2.set(legs_p2.get() + 1)
            if legs_p2.get() == rounds:
                game_end(2)
            elif legs_p1.get != rounds:
                if workwith.game_start[0] == t1_p2 or workwith.game_start[0] == t2_p2 or workwith.game_start[0] == t3_p2:
                    tts.text_to_speech(f'Game Shot and the leg for {name2}. First dart in the next leg goes to {name1} Game on!', 'en')
                    handle_enter_game_win(1)
                    reset_game(None)
                else:
                    tts.text_to_speech(f'Game Shot and the leg for {name2}. First dart in the next leg goes to {name2} Game on!', 'en')
                    handle_enter_game_win(2)
                    reset_game(None)
        else:
            tts.text_to_speech(points, 'en')
        if int(throw) in workwith.dart_checkouts:
            checkoutway_p2.set(", ".join(workwith.dart_checkouts[throw][0].split(", ")))
        else:
            checkoutway_p2.set("")
        if points_left_p1.get() <= 170:
            tts.text_to_speech(f'{name1} requires {points_left_p1.get()}', 'en')

    accept_p2 = t.Button(two_player_root, text='Ok', command=ok2, font=workwith.font3_two)
    
    avg_p2 = t.Label(two_player_root, textvariable=avg_points_p2, font=workwith.font_two)
    count_p2 = t.Label(two_player_root, text='Throw: ', textvariable=count_throws_p2, font=workwith.font_two)
    checkout_p2 = t.Label(two_player_root, textvariable=checkoutway_p2, font=workwith.font2_two)
    
    # Positionierung von Spieler 1
    player_p1.grid(row=1, column=0, padx=10, pady=10)
    points_p1.grid(row=1, column=2, padx=10, pady=10)
    
    t1_p1.grid(row=2, column=1, padx=10, pady=10)
    t2_p1.grid(row=2, column=2, padx=10, pady=10)
    t3_p1.grid(row=2, column=3, padx=10, pady=10)
    
    back_p1.grid(row=1, column=3, padx=10, pady=10)
    accept_p1.grid(row=2, column=5, padx=10, pady=10)

    won_p1.grid(row=3, column=3, padx=10, pady=10)
    
    avg_p1.grid(row=2, column=0, padx=10, pady=10)
    count_p1.grid(row=3, column=0, padx=10, pady=10)
    checkout_p1.grid(row=3, column=2, padx=10, pady=10)
    
    # Positionierung von Spieler 2
    player_p2.grid(row=6, column=0, padx=10, pady=10)
    points_p2.grid(row=6, column=2, padx=10, pady=10)
    
    t1_p2.grid(row=7, column=1, padx=10, pady=10)
    t2_p2.grid(row=7, column=2, padx=10, pady=10)
    t3_p2.grid(row=7, column=3, padx=10, pady=10)
    
    back_p2.grid(row=6, column=3, padx=10, pady=10)
    accept_p2.grid(row=7, column=5, padx=10, pady=10)
    
    won_p2.grid(row=8, column=3, padx=10, pady=10)

    avg_p2.grid(row=7, column=0, padx=10, pady=10)
    count_p2.grid(row=8, column=0, padx=10, pady=10)
    checkout_p2.grid(row=8, column=2, padx=10, pady=10)

    entries = [t1_p1, t2_p1, t3_p1, t1_p2, t2_p2, t3_p2]

    def handle_enter_game_win(next_player):
        if next_player == 1:
            next_e = entries[0]
            next_e.focus()
            player_p1.config(fg='green')
            player_p2.config(fg='black')
        elif next_player == 2:
            next_e = entries[-3]
            next_e.focus()
            player_p1.config(fg='black')
            player_p2.config(fg='green')

    def handle_enter(event):
        global current_entry
        current_entry = event.widget
        next_index = (entries.index(current_entry) + 1) 
        if len(workwith.game_start) <= 3:
            workwith.game_start.append(current_entry)

        if current_entry == entries[2]:
            player_p1.config(fg='black')
            player_p2.config(fg='red')
            next_entry = entries[next_index]
            next_entry.focus()
            ok1()
        elif current_entry == entries[-1]:
            player_p2.config(fg='black')
            player_p1.config(fg='red')
            next_entry = entries[0]
            next_entry.focus()
            ok2()
        else:
            next_entry = entries[next_index]  
            next_entry.focus() 

            def transform_input(event):
                current_entry = event.widget
                value = current_entry.get()
                transformed_value = value.replace('/', 'T').replace('*', 'D')
                current_entry.delete(0, t.END)
                current_entry.insert(0, transformed_value)
            
            for entry in entries:
                entry.bind("<KeyRelease>", transform_input)


    for entry in entries:
        entry.bind("<Return>", handle_enter)


    two_player_root.mainloop()