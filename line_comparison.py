import logging
import math

logging.basicConfig(filename="line_comparison.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class LineComparison:
    def __init__(self, para):

        self.x1 = para.get('x1')
        self.x2 = para.get('x2')
        self.y1 = para.get('y1')
        self.y2 = para.get('y2')
        self.x3 = para.get('x3')
        self.x4 = para.get('x4')
        self.y3 = para.get('y3')
        self.y4 = para.get('y4')

    def length_calculation(self):
        """
        Function to calculate the length of the line by taking user input
        """
        try:
            line1 = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
            line2 = math.sqrt((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2)
            if line1 == line2:
                print("Length of line1 and line2 are equal")
            elif line1 > line2:
                print("Length of line1 is greater than length of line2")
            else:
                print("Length of line2 is greater than length of line1")
        except Exception as e:
            logging.error(e)


def length_of_line():
    """
    Function for taking user input and to call length_calculation function
    :return: return user input and call the length_calculation function
    """
    try:
        x1 = int(input("Enter value of X1 : "))
        x2 = int(input("Enter value of X2 : "))
        y1 = int(input("Enter value of Y1 : "))
        y2 = int(input("Enter value of Y2 : "))
        x3 = int(input("Enter value of X3 : "))
        x4 = int(input("Enter value of X4 : "))
        y3 = int(input("Enter value of Y3 : "))
        y4 = int(input("Enter value of Y4 : "))

        l1 = LineComparison({'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2, 'x3': x3, 'x4': x4, 'y3': y3, 'y4': y4})

        l1.length_calculation()

    except ValueError:
        logging.error("Enter number only")
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    object = length_of_line()
    print(object)
