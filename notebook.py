import datetime


class NoteBook:
    list_of_notes = []
    last_id = 0

    def __init__(self, name):
        self.name = name
        self.note_id = NoteBook.last_id + 1

    def add_note(self, Note):
        NoteBook.list_of_notes.append(Note)

    def modify_note(self):
        for note in NoteBook.list_of_notes:
            print(f"modifier la note {self.note_id}")

    def display_notes(self):
        print(f"il y a : {len(NoteBook.list_of_notes)} notes")
        print("----------------------------------------------")
        for notes in NoteBook.list_of_notes:
            print(f"note numero {self.note_id} est : {notes.memo} ")

    def search_note(self):
        pass


class Note:
    """represents a note in the notebook"""

    #last_id = 0

    def __init__(self, memo, tag):
        self.memo = memo
        self.tag = tag
        #self.note_id = Note.last_id + 1
        self.date_creation = self.set_date()

    @staticmethod
    def set_date():
        now = datetime.datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time


def main():
    while True:
        #print()
        print("*****************************************")
        print("Menu :                                  *")
        print("*****************************************")
        print("Enter 1 to create a note                *")
        print("Enter 2 to display the list of notes    *")
        print("Enter 3 to modify a note                *")
        print("Enter 4 to look for a note              *")
        print("Enter 5 to exit                         *")
        print("*****************************************")
        print("Votre choix :")
        user_choice = int(input())
        if user_choice is 1:
            nb = NoteBook('Notebook 1')
            print("Votre note :")
            text_input = str(input())
            note = Note(text_input, "test")
            nb.add_note(note)
            #date_creation = note.set_date()
            print("Memo : " + str(NoteBook.last_id) + " " + note.memo + " Date : " +
                  note.date_creation + " Tag : " + note.tag)
            #nb.display_notes()
            print("")
        elif user_choice is 2:
            nb.display_notes()
        elif user_choice is 3:
            print('Note number to modify ? : ')
            note_nb = int(input())
            nb.modify_note(note_nb)
        elif user_choice is 4:
            nb.search_note()
        elif user_choice is 5:
            print("**** Fin du programme ****")
            quit()


# Main
if __name__ == '__main__':
    # Runs the application
    main()
