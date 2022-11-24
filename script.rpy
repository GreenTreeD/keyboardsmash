
define mc = Character('Эйлин', color="#c8ffc8")




label start:

    scene bg room
    "???" "А что происходит?)"
    show eileen happy
    

    mc "Вы создали новую игру Ren'Py."

    mc "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    hide eileen happy 

    menu:
        "Выбор 1":
            jump scene1
        "Выбор 2":
            jump scene2


    return

label scene1:
    "Сцена 1"

    return

label scene2:
    "Cцена 2"

    return