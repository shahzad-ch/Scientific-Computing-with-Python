import copy
import random

class Hat:
    def __init__(self,**args):
        print(args)
        self.contents = []
        for i in args:
            for j in range(args[i]):
                self.contents.append(i)
    
    def draw(self, n):
        drawn_balls = []
        r = random
        if n > len(self.contents):
            drawn_balls.extend(self.contents)
            print('drawn balls are')
            print(drawn_balls)
            self.contents = []
        else:
            for i in range(n):
                choice = r.choice(self.contents)
                drawn_balls.append(choice)
                self.contents.pop(self.contents.index(choice))
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    exp_balls = []
    balls_drawn = []
    for i in expected_balls:
        for j in range(expected_balls[i]):
            exp_balls.append(i)

    for i in range(num_experiments):
        copied_hat = copy.deepcopy(hat)
        balls_drawn = copied_hat.draw(num_balls_drawn)

        pop_count = 0
        for j in exp_balls:
            if j in balls_drawn:
                balls_drawn.pop(balls_drawn.index(j))
                pop_count += 1
            if pop_count == len(exp_balls):
                count += 1
    
    probability = count/num_experiments
    print(probability)
    return probability


  
hat1 = Hat(black=6, red=4, green=3)
    
experiment(hat1, {'red': 2, 'green': 1}, 4, 100)
