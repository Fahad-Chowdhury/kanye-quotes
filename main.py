from tkinter import *
import os
import requests


class KanyeQuotes():

    def __init__(self):
        self.window = None
        self.canvas = None
        self.quote_text = None
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.setup_ui()

    def setup_ui(self):
        """ Setup the User Interface. """
        self._setup_window()
        self._setup_canvas()
        self._setup_button()

    def _setup_window(self):
        """ Setup the window. """
        self.window = Tk()
        self.window.title("Kanye Says...")
        self.window.config(padx=50, pady=50)

    def _setup_canvas(self):
        """ Setup Canvas with background image. """
        self.canvas = Canvas(width=300, height=414)
        background_img_path = os.path.join(self.current_dir, "background.png")
        self.background_img = PhotoImage(file=background_img_path)
        self.canvas.create_image(150, 207, image=self.background_img)
        self.quote_text = self.canvas.create_text(150, 207, text="Click button for Kanye Quotes",
                                                  width=250, font=("Arial", 20, "bold"), fill="white")
        self.canvas.grid(row=0, column=0)

    def _setup_button(self):
        """ Setup Button with Kanye West Image. """
        kanye_img_path = os.path.join(self.current_dir, "kanye.png")
        self.kanye_img = PhotoImage(file=kanye_img_path)
        kanye_button = Button(image=self.kanye_img, highlightthickness=0, command=self.update_quote)
        kanye_button.grid(row=1, column=0)

    def update_quote(self):
        ''' Update Kanye West quote in the canvas. '''
        response = requests.get(url="https://api.kanye.rest")
        # Raise exeception for response code other than 200
        response.raise_for_status()
        quote = response.json()["quote"]
        self.canvas.itemconfig(self.quote_text, text=quote)


def main():
    """ Main method to execute Kanye-quotes app. """
    kanye = KanyeQuotes()
    kanye.window.mainloop()


if __name__ == "__main__":
    main()
