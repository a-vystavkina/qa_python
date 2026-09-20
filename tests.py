from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_does_not_add_empty_name(self):
        collector = BooksCollector()
    
        collector.add_new_book('')
    
        assert collector.get_books_genre() == {}

    def test_add_new_book_does_not_add_name_longer_than_40_characters(self):
        collector = BooksCollector()
        book_name = 'a' * 41
    
        collector.add_new_book(book_name)
    
        assert collector.get_books_genre() == {}
    
    def test_add_new_book_adds_name_with_40_characters(self):
        collector = BooksCollector()
        book_name = 'a' * 40
    
        collector.add_new_book(book_name)
    
        assert collector.get_books_genre() == {book_name: ''}
    
    def test_set_book_genre_sets_valid_genre_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
    
        collector.set_book_genre('Марсианин', 'Фантастика')
    
        assert collector.get_book_genre('Марсианин') == 'Фантастика'
    
    def test_set_book_genre_does_not_set_unknown_book_or_genre(self):
        collector = BooksCollector()
        collector.set_book_genre('Неизвестная книга', 'Фантастика')
    
        collector.add_new_book('Марсианин')
        collector.set_book_genre('Марсианин', 'Неизвестный жанр')
    
        assert 'Неизвестная книга' not in collector.get_books_genre()
        assert collector.get_book_genre('Марсианин') == ''
    
    def test_get_book_genre_returns_none_for_unknown_book(self):
        collector = BooksCollector()
    
        assert collector.get_book_genre('Неизвестная книга') is None
    
    def test_get_books_with_specific_genre_returns_matching_books(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.add_new_book('Оно')
        collector.set_book_genre('Марсианин', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
    
        assert collector.get_books_with_specific_genre('Фантастика') == ['Марсианин']
    
    def test_get_books_with_specific_genre_returns_empty_list_without_matches(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.set_book_genre('Марсианин', 'Фантастика')
    
        assert collector.get_books_with_specific_genre('Комедии') == []
    
    def test_get_books_genre_returns_all_books_and_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.set_book_genre('Марсианин', 'Фантастика')
    
        assert collector.get_books_genre() == {'Марсианин': 'Фантастика'}
    
    def test_get_books_for_children_excludes_age_restricted_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.add_new_book('Оно')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Марсианин', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шрек', 'Мультфильмы')
    
        assert collector.get_books_for_children() == ['Марсианин', 'Шрек']
    
    def test_add_book_in_favorites_adds_existing_book_once(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
    
        collector.add_book_in_favorites('Марсианин')
        collector.add_book_in_favorites('Марсианин')
    
        assert collector.get_list_of_favorites_books() == ['Марсианин']
    
    def test_add_book_in_favorites_does_not_add_unknown_book(self):
        collector = BooksCollector()
    
        collector.add_book_in_favorites('Неизвестная книга')
    
        assert collector.get_list_of_favorites_books() == []
    
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.add_book_in_favorites('Марсианин')
    
        collector.delete_book_from_favorites('Марсианин')
    
        assert collector.get_list_of_favorites_books() == []
    
    def test_delete_book_from_favorites_does_nothing_for_unknown_book(self):
        collector = BooksCollector()
    
        collector.delete_book_from_favorites('Неизвестная книга')
    
        assert collector.get_list_of_favorites_books() == []
    
    def test_get_list_of_favorites_books_returns_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.add_book_in_favorites('Марсианин')
    
        assert collector.get_list_of_favorites_books() == ['Марсианин']