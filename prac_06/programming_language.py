class ProgrammingLanguage:
    def __init__(self, name="", typing="", year="", reflection=False):
        self.name = name
        self.typing = typing
        self.year = year
        self.reflection = reflection

    def is_dynamic(self):
        return self.typing == "dynamic"

    def __str__(self):
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name, self.typing, self.year, self.reflection)

    def run_test():
        ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
        python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
        visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

        languages = [ruby, python, visual_basic]
        print(python)

        print("The dynamically typed languages are:")
        for language in languages:
            if language.is_dynamic():
                print(language.name)

    run_test()
