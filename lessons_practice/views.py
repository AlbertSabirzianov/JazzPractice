from .utils import LessonsPracticeView


class LessonsPracticeMinorView(LessonsPracticeView):
    """Страница практики минорных аккордов."""

    lesson_type = 'minor'


class LessonsPracticeSeptView(LessonsPracticeView):
    """Страници практики септ аккордов."""

    lesson_type = 'sept'


class LessonsPracticeSusView(LessonsPracticeView):
    """Страница практики sus аккордов."""

    lesson_type = 'sus'


class LessonsPracticeMajView(LessonsPracticeView):
    """Страница пракитики больших мажорнах аккордов."""

    lesson_type = 'maj'


class LessonsPracticeMinMajView(LessonsPracticeView):
    """Страница практики больших минорных аккордов."""

    lesson_type = 'minmaj'
