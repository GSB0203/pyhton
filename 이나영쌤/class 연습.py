class Bssm():
    def __init__(self, task, age, name):
        self.team = "부소마"
        self.task = task
        self.age = age
        self.name = name

    def intro(self):
        print("안녕하세요, %s 에서 %s를 담당하고 있는 %d살 %s입니다." % (self.team, self.task, self.age, self.name))


gsb = Bssm("학생", 17, "김승빈")
gsb.intro()
