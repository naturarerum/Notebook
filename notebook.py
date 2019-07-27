import datetime


class Note:
    """represents a note in the notebook"""

    last_id = 0

    def __init__(self, memo, tag):
        self.memo = memo
        self.tag = tag
        Note.last_id += 1

    def set_date(self):
        now = datetime.datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time

    def modify_note(self):
        pass


class NoteBook:

    list_of_notes = []

    def add_note(self, Note):
        NoteBook.list_of_notes.append(Note)

    def modify_note(self):
        pass

    def display_note(self):
        for notes in NoteBook.list_of_notes:
            print(notes)

    def search_note(self):
        pass


def main():
    while True:
        print("Enter 1 to create a note")
        print("Enter 2 to display the list of notes")
        print("Enter 3 to exit")
        user_choice = (int(input()))
        if user_choice is 1:
            note = Note("ceci est mon premier essai de mémo", "test")
            date_creation = note.set_date()
            nb = NoteBook()
            nb.add_note(note)
            print("Memo : " + " Memo : " + note.memo + " Date : " +
                  date_creation + " Tag : " + note.tag + " id : " + str(Note.last_id))
            nb.display_note()
            print("Menu : ")
        elif user_choice is 2:
            nb.display_note()
        elif user_choice is 3:
            quit()


# Main
if __name__ == '__main__':
        # Runs the application
    main()
