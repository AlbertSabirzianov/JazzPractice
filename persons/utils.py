class DataMixin:
    """
    Базовый класс для PersonalMap
    содержит data для методов:
    get_stady_level()
    get_stady_course()
    """
    data_stady_level: dict[int, str] = {
        0: 'Не выбранно',
        1: 'Нет музыкального образования',
        2: 'Музыкальная школа',
        3: 'Среднее музыкальное образование',
        4: 'Бакалавриат',
        5: 'Магистратура',
        6: 'Аспирантура',
    }
    data_course: dict[int, str] = {
        0: 'Не выбранно',
        1: '1й',
        2: '2й',
        3: '3й',
        4: '4й',
        5: '5й',
    }

    def get_full_name(self):
        return f'{self.user.last_name} {self.user.first_name}'
