    import random

    class Citroen:
        color = 'black'
        price = 10 ** 6
        max_speed = 200
        current_speed = 0

    c3 = Citroen()
    c4 = Citroen()
    c5 = Citroen()

    c3.current_speed = random.randint(0, 200)
    c4.current_speed = random.randint(0, 200)
    c5.current_speed = random.randint(0, 200)

    print(c3.current_speed)
    print(c4.current_speed)
    print(c5.current_speed)