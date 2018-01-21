def drawStars(list):
    for val in list:
        if type(val) == int:
            print "*" * val
        else: 
            print val[0].lower() * len(val)
drawStars([50, 20, "hi", 5, "Goodbye", 1])
