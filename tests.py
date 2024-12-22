import pytest
from main import BooksCollector

class TestBooksCollector:

    # словарь тестовых данных книга-жанр
    books_dictionary = {
            'Война и мир' : 'Роман',
            'Чужой' : 'Ужасы',
            'С новым годом 1!': 'Комедии',
            'Золушка' : 'Мультфильмы',
            'С новым годом 2!' : 'Комедии'
    }

    # фикстура, которая создаёт объект BooksCollector и заполняет словарь books_genre валидными данными
    @pytest.fixture
    def books_collection(self):
        books = BooksCollector()
        books.books_genre = self.books_dictionary
        return books

    # фикстура, которая использует books_collection и заполняет спискок избранного favorites валидными данными
    @pytest.fixture
    def favorites_list(self, books_collection):
        books_collection.favorites = ['С новым годом 1!', 'Чужой']
        return books_collection

    # ======================================================================#
    # 1. метод __init__()
    #-----------------------------------------------------------------------#
    # 1.a проверка значений по умолчанию для полей обьекта BooksCollector
    def test_check_default_fields_books_collector(self):
        collector = BooksCollector()
        assert (collector.books_genre == {} and
                collector.favorites == [] and
                collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'] and
                collector.genre_age_rating == ['Ужасы', 'Детективы'])

    # ======================================================================#
    # 2. метод add_new_book()
    #-----------------------------------------------------------------------#
    # 2.a добавление двух книг
    def test_add_new_book_add_two_books_show_two_books(self):
        collector = BooksCollector()

        books = [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить'
        ]

        books_genre = {}
        for book in books:
            books_genre[book] = ''

        for book in books:
            collector.add_new_book(book)

        assert (len(collector.get_books_genre()) == 2 and
                collector.get_books_genre() == books_genre)
    #-----------------------------------------------------------------------#
    # 2.b параметрический негативный тест для добавления книги с пустым названием и с названием больше 40 символов
    @pytest.mark.parametrize('name', ['', '12345678901234567890123456789012345678901'])
    def test_add_new_book_invalid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert collector.get_books_genre() == {}

    # ======================================================================#
    # 3. метод set_book_genre()
    #-----------------------------------------------------------------------#
    # 3.a устанавливаем книге жанр из списка допустимых жанров
    def test_set_book_genre_exist_genre_set_genre(self):
        collector = BooksCollector()

        book_name = 'Книга1'
        book_genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre
    #-----------------------------------------------------------------------#
    # 3.b устанавливаем книге жанр, которого нет в списке допустимых жанров
    def test_set_book_genre_non_exist_genre_not_set_genre(self):
        collector = BooksCollector()

        book_name = 'Книга1'
        book_genre = 'Жанр1'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == ''

    # ======================================================================#
    # 4. метод get_book_genre()
    #-----------------------------------------------------------------------#
    # 4.a параметрический негативный тест для получения жанра книги с пустым названием и с названием, которого нет в списке книг
    @pytest.mark.parametrize('name', ['', '12345678901234567890123456789012345678901'])
    def test_get_book_genre_invalid_name(self, name, books_collection):
        assert books_collection.get_book_genre(name) == None

    # ======================================================================#
    # 5. метод get_books_with_specific_genre()
    #-----------------------------------------------------------------------#
    # 5.a проверяем список книг с жанром из словаря, одна книга с таким жанром существует в коллекции
    def test_get_books_with_specific_genre_exist_genre_show_one_book(self, books_collection):
        assert books_collection.get_books_with_specific_genre('Мультфильмы') == ['Золушка']
    #-----------------------------------------------------------------------#
    # 5.b проверяем список книг с жанром не из словаря, книга с таким жанром не существует в коллекции
    def test_get_books_with_specific_genre_non_exist_genre_do_not_show_book(self, books_collection):
        assert books_collection.get_books_with_specific_genre('Новости') == []
    #-----------------------------------------------------------------------#
    # 5.c проверяем список книг с жанром не из словаря, книга с таким жанром существует в коллекции
    def test_get_books_with_specific_genre_exist_book_do_not_show_book(self, books_collection):
        assert books_collection.get_books_with_specific_genre('Роман') == []

    #=======================================================================#
    # 6. метод get_books_genre()
    #-----------------------------------------------------------------------#
    # 6.a проверяем словарь books_genre, если словарь books_genre заполнен
    def test_get_books_genre_show_books(self, books_collection):
        assert books_collection.get_books_genre() == self.books_dictionary
    #-----------------------------------------------------------------------#
    # 6.b проверяем словарь books_genre, если словарь книг пустой
    def test_get_books_genre_empty_books_collection(self):
        assert BooksCollector().get_books_genre() == {}

    #=======================================================================#
    # 7. метод get_books_for_children()
    #-----------------------------------------------------------------------#
    # 7.a возвращаем книги, подходящие детям
    def test_get_books_for_children_show_books(self, books_collection):
        assert books_collection.get_books_for_children() == ['С новым годом 1!', 'Золушка', 'С новым годом 2!']
    #-----------------------------------------------------------------------#
    # 7.b проверяем книги, подходящие детям, если словарь книг пустой
    def test_get_books_for_children_empty_books_collection(self):
        assert BooksCollector().get_books_for_children() == []

    # =======================================================================#
    # 8. метод get_list_of_favorites_books()
    # -----------------------------------------------------------------------#
    # 8.a возвращаем книги из списка избранных
    def test_get_list_of_favorites_books_show_favorites(self, favorites_list):
        assert favorites_list.get_list_of_favorites_books() == ['С новым годом 1!', 'Чужой']
    # -----------------------------------------------------------------------#
    # 8.b возвращаем книги из пустого списка избранных
    def test_get_list_of_favorites_books_show_empty_favorites(self):
        assert BooksCollector().get_list_of_favorites_books() == []

    # =======================================================================#
    # 9. метод delete_book_from_favorites()
    # -----------------------------------------------------------------------#
    # 9.a удаляем книгу, которая присутствует в списке избранных
    def test_delete_book_from_favorites_exist_book_show_new_favorites(self, favorites_list):
        favorites_list.delete_book_from_favorites('С новым годом 1!')
        assert favorites_list.get_list_of_favorites_books() == ['Чужой']
    # -----------------------------------------------------------------------#
    # 9.b удаляем книгу, которая отсутствует в списке избранных
    def test_delete_book_from_favorites_non_exist_book_show_old_favorites(self, favorites_list):
        favorites_list.delete_book_from_favorites('Книга 1')
        assert favorites_list.get_list_of_favorites_books() == ['С новым годом 1!', 'Чужой']

    # =======================================================================#
    # 10. метод add_book_in_favorites()
    # -----------------------------------------------------------------------#
    # 10.a добавляем книгу в избранное, которая присутствует в списке книг
    def test_add_book_in_favorites_exist_book_show_new_favorites(self, books_collection):
        books_collection.add_book_in_favorites('С новым годом 1!')
        assert books_collection.get_list_of_favorites_books() == ['С новым годом 1!']
    # -----------------------------------------------------------------------#
    # 10.b добавляем книгу в избранное, которая отсутствует в списке книг
    def test_add_book_in_favorites_non_exist_book_show_old_favorites(self, books_collection):
        books_collection.add_book_in_favorites('Книга 1')
        assert books_collection.get_list_of_favorites_books() == []

