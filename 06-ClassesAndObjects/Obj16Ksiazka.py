class Book:
    __current_page = 1
    __is_open = False

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def open_book(self):
        self.__is_open = True
        print("Otwierasz książke", self.title)

    def close_book(self):
        self.__is_open = False

    def next_page(self):
        if self.__current_page + 1 < self.pages:
            if self.__is_open == True:
                self.__current_page += 1
                print("Jesteś teraz na stronie:", self.__current_page)
            else:
                print("Książka jest zamknięta.Nie możesz zmienić strony")
        else:
            print("Koniec książki")

    def status(self):
        print(self.title, self.author, self.pages, self.__current_page)



