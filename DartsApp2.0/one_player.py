import tkinter as t, workwith, tts

#row=1, column=1, padx=10, pady=10

def start(name, mode):
    global one_player_root
    one_player_root = t.Toplevel()
    one_player_root.title('Single player')

    one_player_root.attributes('-fullscreen', True)
    one_player_root.protocol("WM_DELETE_WINDOW", workwith.on_closing)

    end = t.Button(one_player_root, text='x', command=workwith.on_closing, font=workwith.font3)
    end.place(relx=1.0, rely=0.0, anchor='ne')

    def reset_game():
        workwith.last_points_p1.clear()
        points_left.set(mode)
        avg_points.set(0)
        count_throws.set(0)
        checkoutway.set("")

    points_left = t.IntVar(value=mode)
    avg_points = t.IntVar()
    checkoutway = t.StringVar()
    count_throws = t.IntVar()

    player = t.Label(one_player_root,text=name, font=workwith.font)
    points = t.Label(one_player_root, textvariable=points_left, font=('Summer', 80))

    t1 = t.Entry(one_player_root, font=workwith.font, width=3)
    t2 = t.Entry(one_player_root, font=workwith.font, width=3)
    t3 = t.Entry(one_player_root, font=workwith.font, width=3)

    def last_points():
        last_points, last_avg = workwith.reset(points_left.get(), 1)
        points_left.set(last_points)
        avg_points.set(last_avg)
        t = count_throws.get()
        count_throws.set(t - 3)

    back = t.Button(one_player_root, text='Return', command=last_points, font=workwith.font3)
    

    avg = t.Label(one_player_root, textvariable=avg_points, font=workwith.font)
    count = t.Label(one_player_root, textvariable=count_throws, font=workwith.font)

    checkout = t.Label(one_player_root, textvariable=checkoutway, font=workwith.font2)

    player.grid(row=1, column=0, padx=10, pady=10)
    points.grid(row=1, column=2, padx=10, pady=10)

    t1.grid(row=2, column=1, padx=10, pady=10)
    t2.grid(row=2, column=2, padx=10, pady=10)
    t3.grid(row=2, column=3, padx=10, pady=10)

    back.grid(row=1, column=3, padx=10, pady=10)

    avg.grid(row=2, column=0, padx=10, pady=10)
    count.grid(row=3, column=0, padx=10, pady=10)
    checkout.grid(row=3, column=2, padx=10, pady=10)                   

    def ok():
        throw, win, points = workwith.calc(t1.get(), t2.get(), t3.get(), points_left.get(), 1)
        average, throws = workwith.get_average(1)
        t1.delete(0, t.END)
        t2.delete(0, t.END)
        t3.delete(0, t.END)
        points_left.set(throw)
        avg_points.set(average)
        count_throws.set(throws)
        if win == True:
            tts.text_to_speech('Game Shot', 'en')
            reset_game()
        else:
            tts.text_to_speech(points, 'en')
        if throw in workwith.dart_checkouts:
            checkoutway.set(", ".join(workwith.dart_checkouts[throw][0].split(", ")))
        else:
            checkoutway.set("")
        if throw <= 170 and win == False:
            tts.text_to_speech(f'{name} you requier {throw}', 'en')

    accept = t.Button(one_player_root, text='Ok', command=ok, font=workwith.font3)
    accept.grid(row=2, column=5, padx=10, pady=10)

    entries = [t1, t2, t3]
    def handle_enter(event):
        global next_entry
        current_entry = event.widget  
        next_index = (entries.index(current_entry) + 1)  

        if current_entry == entries[-1]:  # Falls aktuelles Feld t3 ist
            ok()
            next_entry = entries[0]
            next_entry.focus() 
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
 

        
    one_player_root.mainloop()