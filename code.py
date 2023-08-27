import random
from PyQt5.QtWidgets import *
import base

app = QApplication([])
window = QWidget()
window.resize(500, 500)
mainLine = QVBoxLayout()
menuBtn = QPushButton("Меню")
restBtn = QPushButton("Відпочити")
timeSpn = QSpinBox()
timeLbl = QLabel("хвилин")
questLbl = QLabel("Питання")
answerBtn = QPushButton("Відповісти")
nextQuestBtn = QPushButton("Наступне питання")
nextQuestBtn.hide()
firstLine = QHBoxLayout()
firstLine.addWidget(menuBtn)
firstLine.addWidget(restBtn)
firstLine.addWidget(timeSpn)
firstLine.addWidget(timeLbl)
mainLine.addLayout(firstLine)
mainLine.addWidget(questLbl)
answersGroup = QGroupBox("Варіанти відповідей")
answer1 = QRadioButton("1")
answer2 = QRadioButton("2")
answer3 = QRadioButton("3")
answer4 = QRadioButton("4")
answers = [answer1, answer2, answer3, answer4]

answersLine = QVBoxLayout()
answersLine.addWidget(answer1)
answersLine.addWidget(answer2)
answersLine.addWidget(answer3)
answersLine.addWidget(answer4)

result = QLabel("Результат")
answersLine.addWidget(result)
result.hide()

answersGroup.setLayout(answersLine)

mainLine.addWidget(answersGroup)
mainLine.addWidget(answerBtn)
mainLine.addWidget(nextQuestBtn)

def setQuest():
    random.shuffle(answers)
    questLbl.setText(base.qeust[base.currentQuest]["питання"])
    answers[0].setText(base.qeust[base.currentQuest]["Правильна відповідь"])
    answers[1].setText(base.qeust[base.currentQuest]["не правильна1"])
    answers[2].setText(base.qeust[base.currentQuest]["не правильна2"])
    answers[3].setText(base.qeust[base.currentQuest]["не правильна3"])

setQuest()
def showResult():
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    result.show()
    nextQuestBtn.show()
    answerBtn.hide()
    if answers[0].isChecked():
        result.setText("Правильно")
    else:
        result.setText("не правильно")


def nextFunc():
    #показати кнопки
    #приховати результат
    base.currentQuest += 1
    setQuest()


answerBtn.clicked.connect(showResult)

window.setLayout(mainLine)
window.show()
app.exec()