# generate_graph.py

import matplotlib.pyplot as plt
import sys

def generate_graph(x, y, output_path):
    plt.scatter(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.plot(x,   y, marker = 'o')
    plt.title('Plotted Graph')
    plt.savefig('media/Graph/'+output_path)
    plt.close()
    print(output_path)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_graph.py <x1> <y1> <output_path>")
        sys.exit(1)



    a1 = sys.argv[1]
    b1 = sys.argv[2]

    a = a1.split(',')
    b = b1.split(',')
    ar1 = []
    ar2 = []
    for i in a:
        ar1.append(int(i))

    for i in b:
        ar2.append(int(i))

    x_values = ar1
    y_values = ar2

    # print(x_values,y_values)


    output_path = sys.argv[3]

    generate_graph(x_values, y_values, output_path)
    