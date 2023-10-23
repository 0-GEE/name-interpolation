import numpy as np
import matplotlib.pyplot as plt


CHARS = 6 # number of characters in the nickname
IMNAME = "nickname_scanned.jpg" # filename of the handwritten nickname image

def main():
    '''
    This script handles the creation of points
    on each nickname character which will act
    as input to the interpolation functions.
    The points wil be serialized in text files
    corresponding to the character whose points
    they contain (char1.txt, char2.txt, ...).
    Within each file, the x- and y- coords are
    listed separately.

    An image of the nickname (scan preferred)
    in JPEG format (.jpg) is required for this
    to work.

    Left click in the gui to create a point,
    right click to delete the most recent point.
    
    Hit 'Enter' key to move on to next character.
    '''

    for i in range(CHARS):
        f = plt.imread(IMNAME)

        plt.figure(figsize=(9,5))
        plt.imshow(f)

        points = plt.ginput(n=-1, show_clicks=True, timeout=0)

        with open("char{0}.txt".format(i+1), 'w') as out_file:  
        
            out_file.write("CHARACTER {0}:\n\n".format(i+1))
            out_file.write("X coords:\n[")

            for pt in points:
                out_file.write(str(pt[0])+', ')
        
            out_file.write("]\nY coords:\n[")

            for pt in points:
                out_file.write(str(pt[1])+', ')
            out_file.write("]")

        print("points written:\n{0}".format(points))

    print("Done.")


if __name__ == "__main__":
    main()
