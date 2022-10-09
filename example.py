class Building:
    def __init__(self, number_of_apartments: int, number_of_floors: int, first_floor_area: float, number_of_residents: dict):
        """
        Создание и подготовка к работе объекта "Здание"

        :param number_of_apartments: Количество квартир
        :param number_of_floors: Количество этажей
        :param first_floor_area: Площадь первого этажа
        :param number_of_residents: Количество жителей в квартирах
        
        """
        self.number_of_apartments = number_of_apartments
        self.number_of_floors = number_of_floors
        self.first_floor_area = first_floor_area
        self.number_of_residents = first_floor_area

    def heiht_of_building(self) -> float:
        """
        Функция которая считает высоту здания

        :return: Высоту здания
        """
        ...

    def mean_apartment_area(self) -> float:
        """
        Рассчитывает среднюю площадь квартиры в здании.

        :return: Средняя площадь квартиры
        """
        ...

    def settlement(self, number_of_empty_apartments) -> dict:
        """
        Заполнить пустые квартиры в доме жителями, возвращает количество новых жителей поквартирно

        Если в доме нет пустых квартир вызывает ошибку с сообщением "дом уже заполнен"

        :param number_of_empty_apartments: Количество пустых квартир
        :return: количество новых жителей поквартирно
        """
        ...


if __name__ == "__main__":
    Building_1 = Building(48, 3, 1000, {apt1:1, apt2:6, apt3:0...} )  # инициализация экземпляра класса
