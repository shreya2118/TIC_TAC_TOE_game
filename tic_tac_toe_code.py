import tkinter as tk
import tkinter.messagebox


class StartGame:

    def __init__(self):

        self.game = tk.Tk()
        self.game.configure(background='black')
        self.game.title("Tic Tac Toe")
        self.game.geometry("443x460")

        # initializing components of Tkinter
        self.game.Label = tk.Label
        self.game.DISABLED = tk.DISABLED
        self.game.Entry = tk.Entry
        self.game.Button = tk.Button
        self.game.playera = tk.StringVar()
        self.game.playerb = tk.StringVar()
        self.game.p1 = tk.StringVar()
        self.game.p2 = tk.StringVar()
        self.game.bclick = True
        self.game.flag = 0
        self.game.buttons = tk.StringVar()
        self.game.ask_to_quit = False

        # Create a Player 1 Name: label
        self.game.label1 = self.game.Label(self.game, text="Player 1 Name (X):",
                                           fg='black', bg='light blue')

        # Create a Player 2 Name: label
        self.game.label2 = self.game.Label(self.game, text="Player 2 Name (Y): ",
                                           fg='black', bg='light blue')

        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        self.game.label1.grid(row=1, column=0, sticky="E")
        self.game.label2.grid(row=2, column=0, sticky="E")

        # Create a text entry box
        # for filling or typing the information.
        self.game.player1_name = self.game.Entry(self.game, textvariable=self.game.p1, bd=5)
        self.game.player1_name.grid(row=1, column=1, columnspan=8)
        self.game.player2_name = self.game.Entry(self.game, textvariable=self.game.p2, bd=5)
        self.game.player2_name.grid(row=2, column=1, columnspan=8)

        self.game.button1 = self.game.Button(self.game, text=" ", font='Times 23 bold', bg='gray', fg='black', height=4,
                                             width=12,
                                             command=lambda: self.btnClick(self.game.button1))
        self.game.button1.grid(row=3, column=0)

        self.game.button2 = self.game.Button(self.game, text=' ', font='Times 23 bold', bg='gray', fg='black', height=4,
                                             width=12,
                                             command=lambda: self.btnClick(self.game.button2))
        self.game.button2.grid(row=3, column=1)

        self.game.button3 = self.game.Button(self.game, text=' ', font='Times 23 bold', bg='gray', fg='black', height=4,
                                             width=12,
                                             command=lambda: self.btnClick(self.game.button3))
        self.game.button3.grid(row=3, column=2)

        self.game.button4 = self.game.Button(self.game, text=' ', font='Times 23 bold', bg='gray', fg='black', height=4,
                                             width=12,
                                             command=lambda: self.btnClick(self.game.button4))
        self.game.button4.grid(row=4, column=0)

        self.game.button5 = self.game.Button(self.game, text=' ', font='Times 23 bold', bg='gray', fg='black', height=4,
                                             width=12,
                                             command=lambda: self.btnClick(self.game.button5))
        self.game.button5.grid(row=4, column=1)

        self.game.button6 = self.game.Button(self.game, text=' ', font='Times 23 bold', bg='gray', fg='black', height=4,
                                             width=12,
                                             command=lambda: self.btnClick(self.game.button6))
        self.game.button6.grid(row=4, column=2)

        self.game.button7 = self.game.Button(self.game, text=' ', font='Times 23 bold', bg='gray', fg='black', height=4,
                                             width=12,
                                             command=lambda: self.btnClick(self.game.button7))
        self.game.button7.grid(row=5, column=0)

        self.game.button8 = self.game.Button(self.game, text=' ', font='Times 23 bold', bg='gray', fg='black', height=4,
                                             width=12,
                                             command=lambda: self.btnClick(self.game.button8))
        self.game.button8.grid(row=5, column=1)

        self.game.button9 = self.game.Button(self.game, text=' ', font='Times 23 bold', bg='gray', fg='black', height=4,
                                             width=12,
                                             command=lambda: self.btnClick(self.game.button9))
        self.game.button9.grid(row=5, column=2)

        self.game.play_again_button = self.game.Button(self.game, text='Reset', font='Times 20 bold', bg='light blue',
                                                       fg='black', height=2, width=24,
                                                       command=lambda: self.btnClick(self.game.play_again_button))
        self.game.play_again_button.grid(row=6, columnspan=3)

        # Start the GUI
        self.game.mainloop()

    def disableButton(self):
        self.game.button1.configure(state=self.game.DISABLED)
        self.game.button2.configure(state=self.game.DISABLED)
        self.game.button3.configure(state=self.game.DISABLED)
        self.game.button4.configure(state=self.game.DISABLED)
        self.game.button5.configure(state=self.game.DISABLED)
        self.game.button6.configure(state=self.game.DISABLED)
        self.game.button7.configure(state=self.game.DISABLED)
        self.game.button8.configure(state=self.game.DISABLED)
        self.game.button9.configure(state=self.game.DISABLED)

    def btnClick(self, buttons):

        if buttons["text"] == " " and self.game.bclick == True:
            buttons["text"] = "X"
            self.game.bclick = False
            self.game.playerb = self.game.p2.get() + " Wins!"
            self.game.playera = self.game.p1.get() + " Wins!"
            self.checkForWin()
            self.game.flag += 1

        elif buttons["text"] == " " and self.game.bclick == False:
            buttons["text"] = "O"
            self.game.bclick = True
            self.checkForWin()
            self.game.flag += 1

        elif buttons["text"] == "Reset":
            self.game.destroy()
            StartGame()

        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

    def checkForWin(self):
        if (self.game.button1['text'] == 'X' and self.game.button2['text'] == 'X' and self.game.button3[
            'text'] == 'X' or
                self.game.button4['text'] == 'X' and self.game.button5['text'] == 'X' and self.game.button6[
                    'text'] == 'X' or
                self.game.button7['text'] == 'X' and self.game.button8['text'] == 'X' and self.game.button9[
                    'text'] == 'X' or
                self.game.button1['text'] == 'X' and self.game.button5['text'] == 'X' and self.game.button9[
                    'text'] == 'X' or
                self.game.button3['text'] == 'X' and self.game.button5['text'] == 'X' and self.game.button7[
                    'text'] == 'X' or
                self.game.button1['text'] == 'X' and self.game.button2['text'] == 'X' and self.game.button3[
                    'text'] == 'X' or
                self.game.button1['text'] == 'X' and self.game.button4['text'] == 'X' and self.game.button7[
                    'text'] == 'X' or
                self.game.button2['text'] == 'X' and self.game.button5['text'] == 'X' and self.game.button8[
                    'text'] == 'X' or
                self.game.button7['text'] == 'X' and self.game.button6['text'] == 'X' and self.game.button9[
                    'text'] == 'X'):
            self.disableButton()
            self.game.ask_to_quit = True
            tkinter.messagebox.showinfo("Tic-Tac-Toe", self.game.playera)

        elif self.game.flag == 8:
            self.game.ask_to_quit = True
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

        elif (self.game.button1['text'] == 'O' and self.game.button2['text'] == 'O' and self.game.button3[
            'text'] == 'O' or
              self.game.button4['text'] == 'O' and self.game.button5['text'] == 'O' and self.game.button6[
                  'text'] == 'O' or
              self.game.button7['text'] == 'O' and self.game.button8['text'] == 'O' and self.game.button9[
                  'text'] == 'O' or
              self.game.button1['text'] == 'O' and self.game.button5['text'] == 'O' and self.game.button9[
                  'text'] == 'O' or
              self.game.button3['text'] == 'O' and self.game.button5['text'] == 'O' and self.game.button7[
                  'text'] == 'O' or
              self.game.button1['text'] == 'O' and self.game.button2['text'] == 'O' and self.game.button3[
                  'text'] == 'O' or
              self.game.button1['text'] == 'O' and self.game.button4['text'] == 'O' and self.game.button7[
                  'text'] == 'O' or
              self.game.button2['text'] == 'O' and self.game.button5['text'] == 'O' and self.game.button8[
                  'text'] == 'O' or
              self.game.button7['text'] == 'O' and self.game.button6['text'] == 'O' and self.game.button9[
                  'text'] == 'O'):
            self.disableButton()
            self.game.ask_to_quit = True
            tkinter.messagebox.showinfo("Tic-Tac-Toe", self.game.playerb)

        if self.game.ask_to_quit:
            msgbox = tk.messagebox.askquestion('End Game', 'Do you want to End game?')
            if msgbox == 'yes':
                self.game.destroy()
            else:
                tk.messagebox.showinfo('Return', 'You will now return to the application screen')
                self.game.destroy()
                StartGame()


StartGame()
