
import random


class GameGuess():
    def __init__(self) -> None:
        self.reboot()
    
    def begin_g(self) -> int:
        self.num = random.randint(1, self.border)
        
    def reboot(self):
        self.count: int = 0
        self.textLabel: str = 'Укажите в каком интервале загадать число\n (от 1 до скольки, но не больше 1000?)'
        self.gg_progress: bool = True
        self.border: int = 1000
        self.one_num: int = 100
        self.game_over: bool = False
    
    def is_valid(self, s: str) -> bool:
        if self.game_over and s.lower() in ("yes","да","y","д"):
            self.game_over = False
            return False
        elif self.game_over:
            return False
        elif s.isdigit() and 0 < int(s) < self.border +1:
            return True
        self.game_over =True
        return True
    
    def check_n(self):
        if self.n == self.num:
            self.count += 1
            self.textLabel = f'Вы угадали c {self.count} попыток, поздравляю!\n Желаете перезапустить игру?'
            self.game_over = True
            
           
            
        elif self.n < self.num:
            self.count += 1
            self.textLabel = f'Вы ввели {self.n}\n Это слишком мало, попробуйте еще раз!'
            
            
        else:
            self.count += 1
            self.textLabel = f'Вы ввели {self.n}.\n Это слишком много, попробуйте еще раз!'           
    
    def play(self, n:str) -> bool:
        self.valid: bool = self.is_valid(n)
        if self.valid and not self.game_over:
            self.n = int(n)
            if self.gg_progress:
                self.border=self.n
                self.begin_g()
                
                self.textLabel="Введите загаданное число:"
                self.gg_progress = False
                self.one_num = 1
                return True
            else:
                self.check_n()
                return True
        elif self.game_over and not self.valid:
            return False
        elif not self.game_over and not self.valid:
            self.reboot()
            return True
        else:
            self.textLabel: str = f'А может быть все-таки введем целое число \n от {self.one_num} до {self.border}?'
            self.game_over = False
            return True

if __name__=='__main__':
    gg = GameGuess()
    play = True
    while play:
        play = gg.play(input(gg.textLabel))
        
        
            
       
       
        