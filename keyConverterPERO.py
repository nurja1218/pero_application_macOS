import psutil
# import win32gui
# import win32process
from pynput import keyboard

# The key combination to check
COMBINATIONS = [{'comb1': [keyboard.Key.shift_l, keyboard.Key.enter]},
                {'comb2': [keyboard.Key.shift_r, keyboard.Key.enter]},
                {'comb3': [keyboard.Key.shift_l]},
                {'comb4': [keyboard.Key.shift_r]}]

# 현재 입력받은 키
currentValue = []

keyAction = keyboard.Controller()



#########################################
################# ppt ###################

def presentation_start():
    currentValue.clear()

    keyAction.press(keyboard.Key.f5)
    keyAction.release(keyboard.Key.f5)


def presentation_create():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press("n")
    keyAction.release("n")
    keyAction.release(keyboard.Key.ctrl_l)


def slide_add():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press("m")
    keyAction.release("m")
    keyAction.release(keyboard.Key.ctrl_l)


def save_as():
    currentValue.clear()

    keyAction.press(keyboard.Key.f12)
    keyAction.release(keyboard.Key.f12)


def file_home():
    currentValue.clear()

    keyAction.press(keyboard.Key.alt_l)
    keyAction.press("f")
    keyAction.release("f")
    keyAction.release(keyboard.Key.alt_l)


def open_file():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press("o")
    keyAction.release("o")
    keyAction.release(keyboard.Key.ctrl_l)


#########################################
################ excel ##################

def format_cell():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press('1')
    keyAction.release('1')
    keyAction.release(keyboard.Key.ctrl_l)


def column_zero():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press('9')
    keyAction.release('9')
    keyAction.release(keyboard.Key.ctrl_l)


def row_zero():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press('0')
    keyAction.release('0')
    keyAction.release(keyboard.Key.ctrl_l)


def function_wizard():
    currentValue.clear()

    keyAction.press(keyboard.Key.shift)
    keyAction.press(keyboard.Key.f3)
    keyAction.release(keyboard.Key.f3)
    keyAction.release(keyboard.Key.shift)


#########################################
############# macOS default #############

def mac_dashboard():
    currentValue.clear()

    keyAction.press(keyboard.Key.alt)
    keyAction.press(keyboard.Key.cmd)
    keyAction.press('d')
    keyAction.release('d')
    keyAction.release(keyboard.Key.cmd)
    keyAction.release(keyboard.Key.alt)


def desktop_left():
    currentValue.clear()

    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press(keyboard.Key.left)
    keyAction.release(keyboard.Key.left)
    keyAction.release(keyboard.Key.ctrl_l)


def help_menu():
    currentValue.clear()

    keyAction.press(keyboard.Key.shift)
    keyAction.press(keyboard.Key.cmd)
    keyAction.press('/')
    keyAction.release('/')
    keyAction.release(keyboard.Key.cmd)
    keyAction.release(keyboard.Key.shift)


def spotlight():
    currentValue.clear()

    keyAction.press(keyboard.Key.cmd)
    keyAction.press(keyboard.Key.space)
    keyAction.release(keyboard.Key.space)
    keyAction.release(keyboard.Key.cmd)


def desktop_right():
    currentValue.clear()


    keyAction.press(keyboard.Key.ctrl_l)
    keyAction.press(keyboard.Key.right)
    keyAction.release(keyboard.Key.right)
    keyAction.release(keyboard.Key.ctrl_l)


def full_screen_capture():
    currentValue.clear()

    keyAction.press(keyboard.Key.shift)
    keyAction.press(keyboard.Key.cmd)
    keyAction.press('3')
    keyAction.release('3')
    keyAction.release(keyboard.Key.cmd)
    keyAction.release(keyboard.Key.shift)


#########################################

func_mapping = {"mac_dashboard": mac_dashboard,
                "desktop_left": desktop_left,
                "help_menu": help_menu,
                "spotlight": spotlight,
                "desktop_right": desktop_right,
                "full_screen_capture": full_screen_capture,
                "presentation_start": presentation_start,
                "presentation_create": presentation_create,
                "slide_add": slide_add,
                "save_as": save_as,
                "file_home": file_home,
                "open_file": open_file,
                "format_cell": format_cell,
                "column_zero": column_zero,
                "row_zero": row_zero,
                "function_wizard": function_wizard}

#########################################

# def funWin():
#     pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
#     # print(psutil.Process(pid[-1]).name())
#     return psutil.Process(pid[-1]).name()

#########################################
def execute1():
    # print("linear1")
    # new_window()
    pass


def execute2():
    # print("linear2")
    # previous_page()
    pass


def execute3():
    ############# linear3에 대한 함수 #############

    f = open("./setting/pero_setting_data/apply_app.txt", "r")
    apply_app = f.read()
    f = open("./setting/pero_setting_data/apply_gesture.txt", "r")
    apply_ges = f.read()
    apply_ges = apply_ges.split("\n")
    f.close()

    if apply_app == "default":
        ## default.txt를 읽어서 명령에 적용
        f = open("./setting/pero_setting_data/default.txt", "rt", encoding="UTF-8")
        default_list = f.read()
        default_list = default_list.split("\n")
        default_all = {}
        for i in range(len(default_list)):
            default_all.update({default_list[i].split(":")[0]: default_list[i].split(":")[1]})

        for item in list(default_all.keys()):
            if item == "linear3":
                func_mapping["mac_dashboard"]()
    elif apply_app == "mac_os":
        for i in range(len(apply_ges) - 1):
            if apply_ges[i] == "linear3":
                # 명령값에 대한 함수 실행
                f = open("./setting/pero_setting_data/linear3.txt", "r")
                linear3 = f.read()
                linear3 = linear3.split(":")[1]
                if linear3 == "대시보드 열기닫기(Default)":
                    func_mapping["mac_dashboard"]()
                elif linear3 == "화면 왼쪽 이동":
                    func_mapping["desktop_left"]()
                elif linear3 == "도움말 메뉴":
                    func_mapping["help_menu"]()


def execute4():
    f = open("./setting/pero_setting_data/apply_app.txt", "r")
    apply_app = f.read()
    f = open("./setting/pero_setting_data/apply_gesture.txt", "r")
    apply_ges = f.read()
    apply_ges = apply_ges.split("\n")
    f.close()

    if apply_app == "default":
        f = open("./setting/pero_setting_data/default.txt", "rt", encoding="UTF-8")
        default_list = f.read()
        default_list = default_list.split("\n")
        default_all = {}
        for i in range(len(default_list)):
            default_all.update({default_list[i].split(":")[0]: default_list[i].split(":")[1]})

        for item in list(default_all.keys()):
            if item == "linear4":
                func_mapping["spotlight"]()
    elif apply_app == "mac_os":
        for i in range(len(apply_ges) - 1):
            if apply_ges[i] == "linear4":
                f = open("./setting/pero_setting_data/linear4.txt", "r")
                linear4 = f.read()
                linear4 = linear4.split(":")[1]
                if linear4 == "스포트라이트(Default)":
                    func_mapping["spotlight"]()
                elif linear4 == "화면 오른쪽 이동":
                    func_mapping["desktop_right"]()
                elif linear4 == "전체화면 캡처":
                    func_mapping["full_screen_capture"]()


# 키보드 클릭시(press) 아래 함수 실행
def on_press(key):
    # 미리 설정한 단축키 dictionary값을 입력된 key값과 비교
    try:
        for i in COMBINATIONS:
            for j in i.values():
                for k in j:
                    # 단축키와 입력된key값이 같다면 currentValue에 추가
                    if key == k:
                        currentValue.append(key)
                        raise NotImplementedError
                    else:
                        pass
    except NotImplementedError:
        # currentValue.clear()
        # currentList.clear()
        pass

    # esc버튼 클릭하면 run stop
    # if key == keyboard.Key.esc:
    #     return False


def on_release(key):
    # press에서 확인한 currentValue값에 따라 실행될 함수 호출
    try:
        for m in COMBINATIONS:
            for n, l in m.items():
                if currentValue == l:
                    if n == 'comb1':
                        # execute1()
                        pass
                    elif n == 'comb2':
                        # execute2()
                        pass
                    elif n == 'comb3':
                        # 위로 제스처
                        execute3()
                    elif n == 'comb4':
                        # 아래로 제스처
                        execute4()
                    raise NotImplementedError
    except NotImplementedError:
        # currentValue.clear()
        # currentList.clear()
        pass

    try:
        currentValue.clear()
    except KeyError:
        pass



# 키보드 예외처리도 고려
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        print('keyboard interrupt = run stop')
