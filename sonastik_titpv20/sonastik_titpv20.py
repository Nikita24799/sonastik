rus_list=[]
est_list=[]


def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())      
    return mas
def tolkimine(mas1, mas2 ): 
    sona=input("Введи слово, кoторое хочешь перевести ")
    signal = 0
    if sona in mas1:
        tolk=mas2[mas1.index(sona)]
    elif sona in mas2:
        tolk=mas1[mas2.index(sona)]
    else:
        signal = 1
        tolk=""
        print("Такого слова в словаре нет, но вы можете его добавить:")
    return tolk, signal
def correct(mas1, mas2, f1, f2):
    sona = input("Введите слово: ")
    muutus = input("Какое слово изменить?: ")
    if sona.isascii():        
        if sona in mas2:
            index = mas2.index(sona)        
            mas1[index] = muutus    
    else:
        if sona in mas1:
            index = mas1.index(sona) 
            mas2[index] = muutus


    fail=open(f1,'w',encoding="utf-8-sig")
    text = ""
    for s in mas1:
        text += s + "\n"
    fail.write(text)  
    fail=open(f2, 'w', encoding="utf-8-sig")
    text = ""
    for s in mas2:
        text += s + "\n"
    fail.write(text)
    fail.close()

def tolkimine(mas1, mas2 ): 
    sona=input("Введи слово, кoторое надо перевести ")
    signal = 0
    if sona in mas1:
        tolk=mas2[mas1.index(sona)]
    elif sona in mas2:
        tolk=mas1[mas2.index(sona)]
    else:
        signal = 1
        tolk=""
        print("Такого слова в словаре нет, но вы можете его добавить:")
    return tolk, signal



def uus_sona(mas1,mas2,f1,f2):
    sona_rus=input("Введите слово на русском:")
    sona_est=input("Введите слово на эстонском: ")
    mas1.append(sona_rus)
    mas2.append(sona_est)
    fail=open(f2,'a',encoding="utf-8-sig")
    fail.write(sona_est+"\n")
    fail.close()
    fail=open(f1,'a',encoding="utf-8-sig")
    fail.write(sona_rus+"\n")
    fail.close()
    return mas1, mas2
    return mas1, mas2

rus_list=loe_failist("rus.txt")
est_list=loe_failist("est.txt")
print(est_list)
while True:      
    print(rus_list)
    print(est_list)
    tolkimine(rus_list,est_list)