def division_by(div: int):
    def divided(x: int) -> int:
        return x/div
    return divided

def run():
    division_by_3=division_by(3)
    print(division_by_3(18))

if __name__=='__main__':
    run()
