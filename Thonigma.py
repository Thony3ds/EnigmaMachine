class EnigmaMachine:
    def __init__(self, rotor1_pos, rotor2_pos, rotor3_pos):
        self.rotor1 = Rotor(start_pos=rotor1_pos, engine_pos=0)
        self.rotor2 = Rotor(start_pos=rotor2_pos, engine_pos=1)
        self.rotor3 = Rotor(start_pos=rotor3_pos, engine_pos=2)

    def change_pos(self):
        self.rotor1.change_pos()
        if self.rotor1.actual_pos > 25:  # Correction: ASCII offset of 65 + 26 letters _
            self.rotor1.actual_pos -= 26
            self.rotor2.change_pos()
        if self.rotor2.actual_pos > 25:
            self.rotor2.actual_pos -= 26
            self.rotor3.change_pos()
        if self.rotor3.actual_pos > 25:
            self.rotor3.actual_pos -= 26

    def reset_rotors(self):
        self.rotor1 = Rotor(start_pos=0, engine_pos=0)
        self.rotor2 = Rotor(start_pos=1, engine_pos=1)
        self.rotor3 = Rotor(start_pos=2, engine_pos=2)

    def process_letter(self, letter: str, reverse: bool = False) -> str:
        letter_idx = ord(letter) - 65
        if reverse:
            # Reverse cryptographic process (simulate decryption)
            letter_idx = self.rotor3.process_letter(letter_idx, reverse=True)
            letter_idx = self.rotor2.process_letter(letter_idx, reverse=True)
            letter_idx = self.rotor1.process_letter(letter_idx, reverse=True)
        else:
            # Forward cryptographic process (simulate encryption)
            letter_idx = self.rotor1.process_letter(letter_idx)
            letter_idx = self.rotor2.process_letter(letter_idx)
            letter_idx = self.rotor3.process_letter(letter_idx)

        self.change_pos()
        return chr(letter_idx + 65)

    def run_emulator(self, sentence:str, cmd:str) -> str:
        command = cmd.strip().lower()
        if command in ("crypt", "decrypt"):
            final_result = ""
            self.reset_rotors()
            reverse = command == "decrypt"
            for i in sentence:
                letter = i.strip().upper()
                if len(letter) == 1 and 'A' <= letter <= 'Z':
                    result = self.process_letter(letter, reverse=reverse)
                    final_result += result
            return final_result

class Rotor:
    def __init__(self, start_pos, engine_pos):
        self.start_pos = start_pos
        self.engine_pos = engine_pos
        self.actual_pos = self.start_pos  # Position relative de 0 à 25

    def change_pos(self):
        self.actual_pos = (self.actual_pos + 1) % 26

    def process_letter(self, letter: int, reverse: bool = False) -> int:
        if reverse:
            # Reverse the letter through the rotor
            return (letter - self.actual_pos + 26) % 26
        else:
            # Forward the letter through the rotor
            return (letter + self.actual_pos) % 26

#enigma_machine = EnigmaMachine()
#enigma_machine.run_emulator(sentence="ANTHONY", cmd="crypt")