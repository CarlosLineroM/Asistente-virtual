import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el micrófono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 1

        # informar que comenzó la grabación
        print("Ya puedes hablar")

        # guarda lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-ES")

            #prueba de que puedo ingresar
            print("Dijistes: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no entienda el audio
        except sr.UnknownValueError:

           # prueba de que no comprendió el audio
           print("lo siento, no entendí")

           # devolver error
           return  "Sigo esperando"

        # en caso de no resolver
        except sr.RequestError:

            # prueba de que no comprendió el audio

            print("lo siento, no entendí")

            # devolver error
            return "Sigo esperando"

        # error insesperado
        except:

           # prueba de que no comprendió el audio
              print("Ups, algo salió mal")

           # devolver error
              return "Sigo esperando"

# Función para que el asistente pueda ser escuchado
def hablar(mensaje):

    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)

# Opciones de voz/idiomas

id1='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id2='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0'

# informar día de la semana
def pedir_cita():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de dias
    calendario ={0: 'Lunes',
                 1: 'Martes',
                 2: 'Miércoles',
                 3: 'Jueves',
                 4: 'Viernes',
                 5: 'Sábado',
                 6: 'Domingo'}

    # Decir el día de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

# informar que hora es
def pedir_hora():
    # Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

# función saludo inicial
def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour >20:
        momento = 'Buenas noches'
    elif hora.hour >=6 or hora.hour <13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'



    # decir el saludo
    hablar(f'{momento}, soy el Helena, tu asistente personal . Por favor, dime en que puedo ayudarte' )


# Función central del asistente
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if ' me puedes abrir youtube' in pedido:
            hablar('Perfecto, abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif ' me puedes abrir el navegador' in pedido:
            hablar('Claro, estoy en ello')
            webbrowser.open('https://www.google.com')
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences = 1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Dame un segundo')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
         elif 'cómo estás' in pedido:
            hablar('Estoy bien, gracias por preguntar')
            continue

        elif 'cuál es tu nombre' in pedido:
            hablar('Soy Helena, tu asistente virtual')
            continue

        elif 'te gusta la música' in pedido:
            hablar('Sí, me encanta la música. ¿Quieres que ponga una canción?')
            continue

        elif 'abre facebook' in pedido:
            hablar('Abriendo Facebook')
            webbrowser.open('https://www.facebook.com')
            continue

        elif 'abre twitter' in pedido:
            hablar('Abriendo Twitter')
            webbrowser.open('https://www.twitter.com')
            continue

        elif 'abre instagram' in pedido:
            hablar('Abriendo Instagram')
            webbrowser.open('https://www.instagram.com')
            continue

        elif 'abre spotify' in pedido:
            hablar('Abriendo Spotify')
            webbrowser.open('https://open.spotify.com')
            continue
    
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de'[-1].strip())
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón, no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa que necesites estoy aquí para ayudarte.")
            break


pedir_cosas()
