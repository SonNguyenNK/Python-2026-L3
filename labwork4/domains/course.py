class Course:
    """Lop dai dien cho Mon hoc"""
    def __init__(self, course_id="", name="", credits=0):
        self.__id = course_id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f"ID Mon: {self.__id:<8} | Ten Mon: {self.__name:<20} | Tin chi: {self.__credits}"