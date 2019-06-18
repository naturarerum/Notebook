import datetime

class Note:

    """represents a note in the notebook"""

    def __init__(self, memo, tag):
        self.memo = memo
        self.tag = tag

    def set_date(self):
        now = datetime.datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time


def main():
    note1 = Note("ceci est mon premier essai de mémo", "test")
    date_creation = note1.set_date()
    print("Memo : " + note1.memo)
    print("tag : " + note1.tag)
    print("date de création :", date_creation)


# Main
if __name__ == '__main__':
        # Runs the application
    main()
