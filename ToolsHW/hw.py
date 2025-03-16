import webbrowser, sys, os  

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
B1 = False  
ERROR_COUNT = 0

def input_math():
    global B1, ERROR_COUNT, UndefinedVar
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == '1': 
                Open_Video()
                B1 = True
                UndefinedVar += 1  
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                ERROR_COUNT += 1 
    except NameError:
        ERROR_COUNT -= 1

def open_video():
    webbrowser.open(X1)
    os.system("echo 'Rickroll incoming...'")

input_math()
