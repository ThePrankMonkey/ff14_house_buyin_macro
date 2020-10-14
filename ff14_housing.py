import pyautogui
import time
import random

random.seed(time.time())
COMMANDS_PERSONAL = ["num0", "num0", "num0", "num0", "num4", "num0"]
COMMANDS_FREECOMPANY = ["num0", "num0", "num0",
                        "num2", "num0", "num4", "num0"]  # Untested?
GLOBAL_WAIT = 0.35
RAND_WAIT = 0.5


def try_to_buy(commands):
    # print("\t Waiting")
    # time.sleep(RAND_WAIT*random.random() + GLOBAL_WAIT)
    print("\t Going")
    for command in commands:
        try:
            pyautogui.press(command)
            time.sleep(RAND_WAIT*random.random() + GLOBAL_WAIT)
        except KeyboardInterrupt:
            print("Quitting...")
            return False
    return True


def clicking_job(housing_type="personal"):
    if housing_type == "freecompany":
        commands = COMMANDS_FREECOMPANY
    else:
        commands = COMMANDS_PERSONAL
    start = time.time()
    print("Get over to FF14 and select the house placard ASAP!")
    time.sleep(5)
    count = 1
    loop = True
    while loop:
        print(f"Trying to buy, count {count}")
        loop = try_to_buy(commands)
        count += 1
    end = time.time()
    print(f"Ran for {end-start} seconds!")


clicking_job()
