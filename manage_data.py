from utils import *
from constants import *


def manage_data(subjects=[], lectures={}, rooms=[], timetable={}):
    global _subjects
    global _lectures
    global _rooms
    global _timetable
    _subjects = subjects
    _lectures = lectures
    _rooms = rooms
    _timetable = timetable

    value = 0
    while value != 5:
        print_menu()
        value = input_number('> ', '1 ~ 3 사이의 수를 입력해주세요.')
        if value == 1:
            save()
        elif value == 2:
            load()
        elif value == 3:
            break
        else:
            print('1 ~ 3 사이의 수를 입력해주세요.')


def print_menu():
    print()
    print('**********************************************************************')
    print('1. 저장하기')
    print('2. 불러오기')
    print('3. 나가기')
    print('**********************************************************************')


def save():
    print()
    print('모든 데이터를 저장합니다')
    save_data(_subjects, SUBJECT_PATH)
    save_data(_lectures, LECTURE_PATH)
    save_data(_rooms, ROOM_PATH)
    save_data(_timetable, TIMETABLE_PATH)
    print('데이터를 모두 저장했습니다')


def load():
    print()
    print('모든 데이터를 불러옵니다')

    _subjects.clear()
    _subjects.extend(load_data(SUBJECT_PATH))

    _lectures.clear()
    _lectures.update(load_data(LECTURE_PATH))

    _rooms.clear()
    _rooms.extend(load_data(ROOM_PATH))

    _timetable.clear()
    _timetable.update(load_data(TIMETABLE_PATH))

    print('데이터를 모두 불러왔습니다')
