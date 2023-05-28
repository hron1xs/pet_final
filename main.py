import play #імпорт бібліотеки

play.set_backdrop("white")#встановлення кольору фона



@play.when_program_starts #декоратор
#Декоратор - це функція, яка дозволяє обернути іншу функцію для розширення її функціональності без безпосередньої зміни коду

def start():#функція для старту програми

    global player,speach,text2
    text1 = play.new_text(words='С - стріляти, В - вчити, Р - рятувати',x=0,y=250,font_size=40,)#команда для створення тексту
    text2 = play.new_text(words='Ї - їсти, А - розказати анекдот, З - підняти трубку',x=0,y=225,font_size=40)#команда для створення тексту
    player = play.new_image(image='pruvit.jpg',x=0,y=0,size=100)#командва для додавання зображення
    speach = play.new_text(words='Привіт, я щойно прийшов зі школи, потрібно зробити уроки',x= 0,y = -250,font_size= 30 )


@play.repeat_forever #декоратор2

async def do():#ігровий цикл
    if play.key_is_pressed('В') or play.key_is_pressed('в'):
        player.size = 50
        player.image = 'yrock.jpg'
        speach.words = 'я так довго робив уроки що уже настав вечір'
        await play.timer(2)
        speach.words = 'тепер хочеться їсти'
    elif play.key_is_pressed('ї') or play.key_is_pressed('Ї'):
        player.size = 150
        player.image = 'eat.jpg'
        speach.words = 'тут нічого не має'
        await play.timer(2)
        speach.words = 'піду рятувати світ'
    elif play.key_is_pressed('р') or play.key_is_pressed('Р'):
        player.size = 75
        player.image = 'spidermen.jpg'
        speach.words = '"на фоні грає музика Destroy Lonely"'
        await play.timer(5)
        player.size = 150
        player.image = 'geniys.jpg'
        speach.words = 'я навіть не втомився'
        await play.timer(2)
        speach.words = '"у вас зазвонив телефон"'
    elif play.key_is_pressed('з') or play.key_is_pressed('З'):
        player.image = 'tilifon.jpg'
        speach.words = 'Ало'
        await play.timer(1)
        speach.words = '"Доброго дня, це Дім Дімич?"'
        await play.timer(2)
        speach.words = 'так'
        await play.timer(3)
        speach.words = '"Вам повістка на Бахмут"'
        await play.timer(3)
        player.size = 50
        player.image = 'bahmyt.jpg'
        speach.words = 'Нарешті, я цього ждав'
        await play.timer(3)
        player.size = 150
        player.image = 'chohesh.jpg'
        speach.words = 'Кінець'
        await play.timer(3)
        speach.words = 'Якщо хочете можете послушати анекдот'
    elif play.key_is_pressed('А') or play.key_is_pressed('а'):
        player.size = 50
        player.image = 'shop.jpg'
        speach.words = 'Випадок в магазині'
        await play.timer(2)
        player.image = 'fonera.jpg'
        speach.words = '-Доброго дня, у вас є фонера?'
        await play.timer(2)
        player.size = 75
        player.image = 'dom.jpg'
        speach.words = '-Вам для господарства?'
        await play.timer(2)
        player.size = 8
        player.image = 'PARIZH.jpg'
        speach.words = '-Ні, буду над Парижем літати'
   
play.start_program()#запуск програми