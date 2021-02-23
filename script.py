print("Hello World!")

my_salary = 12
my_yearly = my_salary * 12
print(my_yearly)


result = 4
result
len('the human bazooka')

def hello():
    name = 'Marcus'
    message = 'Hi'
    print(message, name)

hello()

mark = 0
while mark < 15:
    print('oh boy')
    mark = mark + 1

my_stuff = ['stuff', 'stuff', 'stuff']
for thing in my_stuff:
    print(thing)


def say_hi(name):
    if name == '':
        print('NO NAME')
    else:
        print ('WHATS UP DUDE')
        for letter in name:
            print(letter)

name = input()
say_hi(name)


name = 'test'
len(name)


class Car:
    speed = 0
    started = False

    def start(self):
        self.started = True
        print('Car started, let\'s start')

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('VROOOOOM!')
        else:
            print('You need to start the car first')

    def stop(self):
        self.speed = 0
        print('halting')

car = Car()

print(64**(1/3))
