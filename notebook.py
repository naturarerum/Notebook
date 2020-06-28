import datetime

class NoteBook:

    list_of_notes = []

    def __init__(self, name):
        self.name = name

    def add_note(self, Note):
        NoteBook.list_of_notes.append(Note)

    def modify_note(self,note_id):
        note_to_modify = note_id
        for note in NoteBook.list_of_notes:
            print(note_to_modify)
        

    def display_notes(self):
        for notes in NoteBook.list_of_notes:
            print(notes)

    def search_note(self):
        pass


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

def main():
    while True:
        print("Enter 1 to create a note")
        print("Enter 2 to display the list of notes")
        print("Enter 3 to modify a note")
        print("Enter 4 to look for a note")
        print("Enter 5 to exit")
        user_choice = (int(input()))
        if user_choice is 1:
            nb = NoteBook('Notebook 1')
            note = Note("ceci est mon premier essai de mémo", "test")
            nb.add_note(note)
            date_creation = note.set_date()
            print("Memo : " + str(Note.last_id) + note.memo + " Date : " +
                  date_creation + " Tag : " + note.tag )
            nb.display_notes()
            print("Menu : ")
        elif user_choice is 2:
            nb.display_notes()
        elif user_choice is 3:
            print('Note number to modify ? : ')
            note_nb = int(input())
            nb.modify_note(note_nb)
        elif user_choice is 4:
            nb.search_note()
        elif user_choice is 5:
            quit()


# Main
if __name__ == '__main__':
        # Runs the application
    main()
