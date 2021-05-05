from botControl import run_ActionGroup
import time


while True:
    key = input()
    if key == '1':
        run_ActionGroup('50',1)
    if key == '2':
        run_ActionGroup('51',1)
    if key == '3':
        run_ActionGroup('52',1)
    if key == '4':
        run_ActionGroup('53',1)
    if key == 'w':
        run_ActionGroup('1',1)
    if key == 's':
        run_ActionGroup('2',1)
    if key == 'a':
        run_ActionGroup('3',2)
    if key == 'd':
        run_ActionGroup('4',2)
        