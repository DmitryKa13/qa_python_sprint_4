# ФИНАЛЬНЫЙ ПРОЕКТ 4ого спринта курса QA_PYTHON

## Задача
Покрыть класс BooksCollector тестами.
Покрывать все сценарии не нужно: написать 9-10 тестов — минимум по одному на каждый метод.

## Решение
	# ===========================================================================================================================#
	# 1. метод __init__()
	#----------------------------------------------------------------------------------------------------------------------------#
	# 1.a проверка значений по умолчанию для полей обьекта BooksCollector
		def test_check_default_fields_books_collector()
	# ===========================================================================================================================#
	# 2. метод add_new_book()
	#----------------------------------------------------------------------------------------------------------------------------#
	# 2.a добавление двух книг
		def test_add_new_book_add_two_books_show_two_books()
	#----------------------------------------------------------------------------------------------------------------------------#
	# 2.b параметрический негативный тест для добавления книги с пустым названием и с названием больше 40 символов
		def test_add_new_book_invalid_name()
	# ===========================================================================================================================#
	# 3. метод set_book_genre()
	#----------------------------------------------------------------------------------------------------------------------------#
	# 3.a устанавливаем книге жанр из списка допустимых жанров
		def test_set_book_genre_exist_genre_set_genre()
	#----------------------------------------------------------------------------------------------------------------------------#
	# 3.b устанавливаем книге жанр, которого нет в списке допустимых жанров
		def test_set_book_genre_non_exist_genre_not_set_genre()
	# ===========================================================================================================================#
	# 4. метод get_book_genre()
	#----------------------------------------------------------------------------------------------------------------------------#
	# 4.a параметрический негативный тест для получения жанра книги с пустым названием и с названием, которого нет в списке книг
		def test_get_book_genre_invalid_name()
	# ===========================================================================================================================#
	# 5. метод get_books_with_specific_genre()
	#----------------------------------------------------------------------------------------------------------------------------#
	# 5.a проверяем список книг с жанром из словаря, одна книга с таким жанром существует в коллекции
		def test_get_books_with_specific_genre_exist_genre_show_one_book()
	#----------------------------------------------------------------------------------------------------------------------------#
	# 5.b проверяем список книг с жанром не из словаря, книга с таким жанром не существует в коллекции
		def test_get_books_with_specific_genre_non_exist_genre_do_not_show_book()
	#----------------------------------------------------------------------------------------------------------------------------#
	# 5.c проверяем список книг с жанром не из словаря, книга с таким жанром существует в коллекции
		def test_get_books_with_specific_genre_exist_book_do_not_show_book()
	#============================================================================================================================#
	# 6. метод get_books_genre()
	#----------------------------------------------------------------------------------------------------------------------------#	
	# 6.a проверяем словарь books_genre, если словарь books_genre заполнен
		def test_get_books_genre_show_books()
	#----------------------------------------------------------------------------------------------------------------------------#
	# 6.b проверяем словарь books_genre, если словарь книг пустой
		def test_get_books_genre_empty_books_collection()
	#============================================================================================================================#
	# 7. метод get_books_for_children()
	#----------------------------------------------------------------------------------------------------------------------------#
	# 7.a возвращаем книги, подходящие детям
		def test_get_books_for_children_show_books()
	#----------------------------------------------------------------------------------------------------------------------------#
	# 7.b проверяем книги, подходящие детям, если словарь книг пустой
		def test_get_books_for_children_empty_books_collection()
	# ===========================================================================================================================#
	# 8. метод get_list_of_favorites_books()
	# ---------------------------------------------------------------------------------------------------------------------------#
	# 8.a возвращаем книги из списка избранных
		def test_get_list_of_favorites_books_show_favorites()
	# ---------------------------------------------------------------------------------------------------------------------------#
	# 8.b возвращаем книги из пустого списка избранных
		def test_get_list_of_favorites_books_show_empty_favorites()
	# ===========================================================================================================================#
	# 9. метод delete_book_from_favorites()
	# ---------------------------------------------------------------------------------------------------------------------------#
	# 9.a удаляем книгу, которая присутствует в списке избранных
		def test_delete_book_from_favorites_exist_book_show_new_favorites()
	# ---------------------------------------------------------------------------------------------------------------------------#
	# 9.b удаляем книгу, которая отсутствует в списке избранных
		def test_delete_book_from_favorites_non_exist_book_show_old_favorites()
	# ===========================================================================================================================#
	# 10. метод add_book_in_favorites()
	# ---------------------------------------------------------------------------------------------------------------------------#
	# 10.a добавляем книгу в избранное, которая присутствует в списке книг
		def test_add_book_in_favorites_exist_book_show_new_favorites()
	# ---------------------------------------------------------------------------------------------------------------------------#
	# 10.b добавляем книгу в избранное, которая отсутствует в списке книг
		def test_add_book_in_favorites_non_exist_book_show_old_favorites()
	# ---------------------------------------------------------------------------------------------------------------------------#

## Результат
============================ test session starts =============================
platform win32 -- Python 3.12.4, pytest-8.3.4, pluggy-1.5.0 -- C:\Users\dkaprenin\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: D:\Study\qa_python
plugins: cov-6.0.0
collecting ... collected 21 items

tests.py::TestBooksCollector::test_check_default_fields_books_collector PASSED [  4%]
tests.py::TestBooksCollector::test_add_new_book_add_two_books_show_two_books PASSED [  9%]
tests.py::TestBooksCollector::test_add_new_book_invalid_name[] PASSED    [ 14%]
tests.py::TestBooksCollector::test_add_new_book_invalid_name[12345678901234567890123456789012345678901] PASSED [ 19%]
tests.py::TestBooksCollector::test_set_book_genre_exist_genre_set_genre PASSED [ 23%]
tests.py::TestBooksCollector::test_set_book_genre_non_exist_genre_not_set_genre PASSED [ 28%]
tests.py::TestBooksCollector::test_get_book_genre_invalid_name[] PASSED  [ 33%]
tests.py::TestBooksCollector::test_get_book_genre_invalid_name[12345678901234567890123456789012345678901] PASSED [ 38%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_exist_genre_show_one_book PASSED [ 42%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_non_exist_genre_do_not_show_book PASSED [ 47%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_exist_book_do_not_show_book PASSED [ 52%]
tests.py::TestBooksCollector::test_get_books_genre_show_books PASSED     [ 57%]
tests.py::TestBooksCollector::test_get_books_genre_empty_books_collection PASSED [ 61%]
tests.py::TestBooksCollector::test_get_books_for_children_show_books PASSED [ 66%]
tests.py::TestBooksCollector::test_get_books_for_children_empty_books_collection PASSED [ 71%]
tests.py::TestBooksCollector::test_get_list_of_favorites_books_show_favorites PASSED [ 76%]
tests.py::TestBooksCollector::test_get_list_of_favorites_books_show_empty_favorites PASSED [ 80%]
tests.py::TestBooksCollector::test_delete_book_from_favorites_exist_book_show_new_favorites PASSED [ 85%]
tests.py::TestBooksCollector::test_delete_book_from_favorites_non_exist_book_show_old_favorites PASSED [ 90%]
tests.py::TestBooksCollector::test_add_book_in_favorites_exist_book_show_new_favorites PASSED [ 95%]
tests.py::TestBooksCollector::test_add_book_in_favorites_non_exist_book_show_old_favorites PASSED [100%]

============================= 21 passed in 0.03s ==============================