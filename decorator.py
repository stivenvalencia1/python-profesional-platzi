def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensajes(nombre):
    return f'{nombre}, recibiste un mensaje'

def run():
    print(mensajes('Cesar'))

if __name__=='__main__':
    run()
