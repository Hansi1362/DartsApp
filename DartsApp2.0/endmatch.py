import tkinter as t, gui, workwith, tts


def end (w):
    end = t.Toplevel()
    end.title('End')

    w = w[0:-2]

    tts.text_to_speech(f'Game Shot and the Match for {w}', 'en')    

    winner = t.Label(end, text=f'Game Shot!\n {w}', font=workwith.font)
    winner.grid(row=0, column=1, padx=10, pady=10)

    restart = t.Button(end, text='Restart', font=workwith.font2, command=end.destroy)
    restart.grid(row=1, column=0, padx=10, pady=10)

    end = t.Button(end, text='End', font=workwith.font2, command=gui.select.destroy)
    end.grid(row=1, column=2, padx=10, pady=10)

    end.mainloop()