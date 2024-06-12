import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.1.0')  # wersja Kivy

class TicTacToeApp(App):
    def build(self):
        self.title = "Tic-Tac-Toe"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        self.main_layout = BoxLayout(orientation='vertical')
        
        # Informacja o aktualnym graczu
        self.info_label = Label(text=f"Tura gracza: [color=ff0000]{self.current_player}[/color]", markup=True, font_size=15, size_hint_y=0.1)
        self.main_layout.add_widget(self.info_label)

        # Plansza do gry
        self.layout = GridLayout(cols=3, size_hint_y=0.9)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for row in range(3):
            for col in range(3):
                button = Button(font_size=32)
                button.bind(on_press=lambda instance, r=row, c=col: self.on_button_click(r, c))
                self.layout.add_widget(button)
                self.buttons[row][col] = button

        self.main_layout.add_widget(self.layout)
        Window.size = (400, 400)
        return self.main_layout

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].text = self.current_player
            self.buttons[row][col].color = (1, 0, 0, 1) if self.current_player == "X" else (0, 0, 1, 1)
            if self.check_winner(self.board, self.current_player):
                self.show_popup(f"[color={'ff0000' if self.current_player == 'X' else '0000ff'}]Gracz {self.current_player} wygrywa![/color]")
                self.reset_game()
            elif self.is_board_full(self.board):
                self.show_popup("[color=000000]Remis![/color]")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.info_label.text = f"Tura gracza: [color={'ff0000' if self.current_player == 'X' else '0000ff'}]{self.current_player}[/color]"
        else:
            self.show_popup_warning("[color=ffff00]To pole jest już zajęte. Spróbuj ponownie.[/color]")

    def check_winner(self, board, player):
        for row in board:
            if all([cell == player for cell in row]):
                return True
        for col in range(3):
            if all([board[row][col] == player for row in range(3)]):
                return True
        if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
            return True
        return False

    def is_board_full(self, board):
        return all([cell != " " for row in board for cell in row])

    def show_popup(self, message):
        popup = Popup(title='Koniec gry', content=Label(text=message, markup=True), size_hint=(0.8, 0.4))
        popup.open()

    def show_popup_warning(self, message):
        popup = Popup(title='Uwaga!', content=Label(text=message, markup=True), size_hint=(0.8, 0.4))
        popup.open()

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].text = " "
                self.buttons[row][col].color = (0, 0, 0, 1)
        self.info_label.text = f"Tura gracza: [color=ff0000]{self.current_player}[/color]"

if __name__ == "__main__":
    TicTacToeApp().run()
