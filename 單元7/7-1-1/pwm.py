import PWMServo,time

PWMServo.setServo(1, 1500, 500)
PWMServo.setServo(2, 1500, 500)
time.sleep(0.5)
PWMServo.setServo(1, 1200, 500)
PWMServo.setServo(2, 1500, 500)
time.sleep(0.5)
PWMServo.setServo(1, 1500, 500)
PWMServo.setServo(2, 1500, 500)