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
    """represents a notebook"""

    note_list = []

    def search_note(self):
        pass
    
    

def main():
    note1 = Note("ceci est mon premier essai de mémo", "test")
    date_creation = note1.set_date()
    print("Memo : " + note1.memo)
    print("tag : " + note1.tag)
    print("date de création :", date_creation)
    print(note1.last_id)
    note2 = Note("ceci est mon deuxieme essai de mémo", "test2")
    print(note2.last_id)

# Main
if __name__ == '__main__':
        # Runs the application
    main()
