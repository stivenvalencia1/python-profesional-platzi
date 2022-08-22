def stringtorepit(string: str):
    assert type(string) == str, "solo puede ingresar cadenas"
    def repeater(number: int) -> str:
        return string * number
    return repeater

def run():
    repeatfacundo = stringtorepit("facundo")
    print(repeatfacundo(3))

if __name__=='__main__':
    run()
