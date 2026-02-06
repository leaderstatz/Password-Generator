import string
import secrets
import random

configuration = {
    "Uppercase": string.ascii_uppercase,
    "Lowercase": string.ascii_lowercase,
    "Numbers": string.digits,
    "Symbols": string.punctuation
}

class Generate():
    def __init__(self, window):
        """
        this functions generates a random password and ensures that all the characters you checked are used
        args:
            self
            window
        returns:
            technically returns the var password but is displayed on the GUI
        """

        chars = ""
        password_chars = []

        for option, instance in window.cached_options.items():
            if not configuration[option]:
                window.result.setText("Error generating password (not a valid option)")
                return
            
            if instance.isChecked():
                chars += configuration[option] or string.ascii_uppercase
                password_chars.append(secrets.choice(configuration[option]))

        if not chars:
            window.result.setText("You must select at least one option")
            return
        
        length = window.length_box.value()

        for _ in range(length - len(password_chars)):
            password_chars.append(secrets.choice(chars))

        random.shuffle(password_chars)

        password = "".join(password_chars)

        window.result.setText(password)

    def validate(self):
        pass