from .utils import LessonsPracticeView


class LessonsPracticeMinorView(LessonsPracticeView):
    lesson_type = 'minor'


class LessonsPracticeSeptView(LessonsPracticeView):
    lesson_type = 'sept'


class LessonsPracticeSusView(LessonsPracticeView):
    lesson_type = 'sus'


class LessonsPracticeMajView(LessonsPracticeView):
    lesson_type = 'maj'


class LessonsPracticeMinMajView(LessonsPracticeView):
    lesson_type = 'minmaj'
