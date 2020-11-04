

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ").lower()
    if shape.lower() =="pyramid":
     return shape
    elif shape.lower() == "square":
      return shape
    elif shape.lower() == "triangle":
        return shape
    elif shape.lower() == "rhombus":
        return shape
    elif shape.lower() == "rectangle":
        return shape
    elif shape.lower() == "reverse":
        return shape
    else:
        return get_shape()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    try:
     height = int(input("Height?: "))
     return height
    except:
        return get_height()
    

# TODO: Step 2
def draw_pyramid(height, outline):
        if (outline == False):
            for i in range(height):
                print(" "*(height-i-1), end="")
                print("*"*(2*i+1))
        if (outline == True):
            for i in range(0, height):
                for j in range(height - i - 1):
                    print(" ", end = "")
                for j in range(2 * i + 1):
                    if (j == 0 or j == 2 * i or i == (height - 1)):
                        print("*", end= '')
                    else:
                        print(" ", end= '')
                print("")    


# TODO: Step 3
def draw_square(height, outline):
        if (outline == False):
            for i in range(0, height):
                for j in range(0,height):
                    print("*", end="")
                print("")
        if (outline == True):
            for i in range(0, height):
                for j in range(0,height):
                    if(i == 0 or j == 0 or i == height - 1 or j == height - 1):
                        print("*", end='')
                    else:
                        print(" ", end='') 
                print("")
               


# TODO: Step 4
def draw_triangle(height, outline):
    if (outline == False):
        for i in range(0, height):
            for j in range(0,i + 1):
                print("*", end="")
            print("")
    if (outline == True):
        for i in range(0, height):
            for j in range(0, i + 1):
                if (j == 0 or i == height-1 or i == j):
                    print("*", end="")
                else:
                    print(end=" ")
            print("")


def draw_reverse_triangle(height, outline):
    if (outline == False):
        space = (height * 2 - 1)
        for i in range(0, height):
            for j in range(0, space):
                print(end=" ")
            space = space - 1
            for j in range(0,i + 1):
                print("*", end="")
            print("")

def draw_rectangle(height, outline):
    if (outline == True):
        n = height + 5
        for i in range(0, height):
            for j in range(0, n):
                if (i == 0 or i == height - 1 or j == 0 or j == n - 1):
                    print("*", end='')
                else:
                    print(" ", end="")
            print("")
    if (outline == False):
        n = height + 5
        for i in range(0, height):
            for j in range(0,n):
                    print("*", end="")
            print("")

    

def draw_rhombus(height, outline):
    if (outline == False):
        for i in range(0, height):
            for j in range (0,height - i ):
                print(end=" ")
            for j in range(0,height ):
                print("*", end="")
            print("")
        
    if (outline == True):
        for i in range(0, height):
            for j in range(0, height - i):
                print(end=" ")
            if (i == 0 or i == height-1):
                for j in range(0, height):
                    print("*", end='')
            else:
                for j in range(0, height):
                    if (j == 0 or j == height - 1):
                        print("*", end="")
                    else:
                        print(end=" ")
            print("")




# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if (shape == "pyramid"):
        draw_pyramid(height, outline)
    elif (shape == "square"):
        draw_square(height, outline)
    elif (shape == "triangle"):
        draw_triangle(height, outline)
    elif (shape == "rhombus"):
        draw_rhombus(height, outline)
    elif (shape == "rectangle"):
        draw_rectangle(height, outline)
    elif (shape == 'reverse'):
        draw_reverse_triangle(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (y/N): ")
    if (outline == "y" or outline == "Y"):
        return True
    elif (outline == "n" or outline == "N" or outline == ""):
        return False
    else:
        return get_outline()


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

