# =======================================================================
# communal functions
# =======================================================================
import numpy as np


def triangle_square(__vector_1__, __vector_2__):
    x1 = float(__vector_1__[0, 0])
    y1 = float(__vector_1__[0, 1])
    z1 = float(__vector_1__[0, 2])
    x2 = float(__vector_2__[0, 0])
    y2 = float(__vector_2__[0, 1])
    z2 = float(__vector_2__[0, 2])
    __square__ = 0.5 * ((y2 * z1 - y1 * z2) ** 2 + (x2 * z1 - x1 * z2) ** 2 + (y2 * x1 - y1 * x2) ** 2) ** 0.5
    return __square__


def get_num(__line__):
    n = len(__line__)
    for i in range(0, n):
        if line[-1 * i] == ' ':
            return int(__line__[n - i: n])
        else:
            pass


# =======================================================================
#  communal functions end
# =======================================================================
# =======================================================================
#  nodes functions
# =======================================================================


def handle_nodes(position_x, position_y, position_z, line_nodes, node_number):
    label = ''
    x = ''
    y = ''
    z = ''
    space_number = 0
    n = len(line_nodes)
    for i in range(0, n):
        if line_nodes[i] == ' ':
            space_number = space_number + 1
        elif line_nodes[i] == '\n':
            position_z[int(label)] = float(z)
        else:
            if space_number == 0:
                label = label + line_nodes[i]
            elif space_number == 1:
                x = x + line_nodes[i]
            elif space_number == 2:
                y = y + line_nodes[i]
                position_x[int(label)] = float(x)
            elif space_number == 3:
                z = z + line_nodes[i]
                position_y[int(label)] = float(y)
            else:
                pass
    return position_x, position_y, position_z


def identify_nodes(x, y, z, num, node_number):
    for k in range(num):
        line_nodes = f.readline()
        position_x, position_y, position_z = handle_nodes(x, y, z, line_nodes, node_number)
    line_nodes = f.readline()
    if line_nodes == '$EndNodes\n':
        judge_nodes = 0
        loop_nodes = 0
    else:
        judge_nodes = 1
        loop_nodes = get_num(line_nodes)
    return position_x, position_y, position_z, judge_nodes, loop_nodes


# =======================================================================
#  nodes functions end
# =======================================================================
# =======================================================================
#  elements functions
# =======================================================================


def handle_elements(_element_A, _element_B, _element_C, line_elements, elemente_number):
    label = ''
    A = ''
    B = ''
    C = ''
    space_number = 0
    n = len(line_elements)
    for i in range(0, n):
        if line_elements[i] == ' ':
            space_number = space_number + 1
        elif line_elements[i] == '\n' and C == '' and B == '' and A != '':
            _element_A[int(label)] = int(A)
        elif line_elements[i] == '\n' and C == '' and B != '' and A != '':
            _element_A[int(label)] = int(A)
            _element_B[int(label)] = int(B)
        elif line_elements[i] == '\n' and C != '' and B != '' and A != '':
            _element_C[int(label)] = int(C)
            _element_A[int(label)] = int(A)
            _element_B[int(label)] = int(B)
        else:
            if space_number == 0:
                label = label + line_elements[i]
            elif space_number == 1:
                A = A + line_elements[i]
            elif space_number == 2:
                B = B + line_elements[i]
            elif space_number == 3:
                C = C + line_elements[i]
            else:
                pass
    return _element_A, _element_B, _element_C


def identify_elements(_element_A, _element_B, _element_C, num, element_number):
    for k in range(num):
        line_elements = f.readline()
        _element_A, _element_B, _element_C = handle_elements(_element_A, _element_B, _element_C, line_elements, element_number)
    line_elements = f.readline()
    if line_elements == '$EndElements\n':
        judge_elements = 0
        loop_elements = 0
    else:
        judge_elements = 1
        loop_elements = get_num(line_elements)
    return _element_A, _element_B, _element_C, judge_elements, loop_elements


# =======================================================================
#   elements functions end
# =======================================================================


if __name__ == '__main__':
    f = open('untitled.msh', 'r')
    line = f.readline()
    for line in open('untitled.msh'):
        line = f.readline()
        if line == '$Nodes\n':
            line = f.readline()
            nodes_num = get_num(line)
            line = f.readline()
            loop_num = get_num(line)
            judge_nodes = 1
            nodes_x = {}
            nodes_y = {}
            nodes_z = {}
            while(judge_nodes > 0):
                nodes_x, nodes_y, nodes_z, judge_nodes, loop_num = identify_nodes(nodes_x, nodes_y, nodes_z, loop_num, nodes_num)
        elif line == '$Elements\n':
            line = f.readline()
            elements_num = get_num(line)
            line = f.readline()
            loop_num = get_num(line)
            judge_elements = 1
            element_A = {}
            element_B = {}
            element_C = {}
            while (judge_elements > 0):
                element_A, element_B, element_C, judge_elements, loop_num = identify_elements(element_A, element_B,element_C, loop_num, elements_num)
                #print(loop_num)
        else:
            pass

    n = int(input('please input the label of node = '))
    if n in nodes_x:
        print('the #%d node in the .msh file is (%f, %f, %f)' % (n, nodes_x[n], nodes_y[n], nodes_z[n]))
    else:
        print('label #%d is not in nodes dict, please input again' % n)

    N = int(input('please input the label of element = '))
    if N in element_A and N in element_B and N in element_C:
        print('the #%d element in the .msh file is a 2D element , include nodes %d, %d, %d' % (N, element_A[N], element_B[N], element_C[N]))
    elif N in element_A and N in element_B and N not in element_C:
        print('the #%d element in the .msh file is a 1D element , include nodes %d, %d' % (N, element_A[N], element_B[N]))
    elif N in element_A and N not in element_B and N not in element_C:
        print('the #%d element in the .msh file is a 0D element , include nodes %d' % (N, element_A[N]))
    else:
        print('label #%d is not in elements dict, please input again' % N)

    square = [0] * (elements_num+1)
    for i in range(1, elements_num+1):
        if i in element_A and i in element_B and i in element_C:
            label_A = element_A[i]
            label_B = element_B[i]
            label_C = element_C[i]
            vector_1 = np.mat('0 0 0')
            vector_2 = np.mat('0 0 0')
            vector_1[0, 0] = float(nodes_x[element_A[i]] - nodes_x[element_B[i]])
            vector_1[0, 1] = float(nodes_y[element_A[i]] - nodes_y[element_B[i]])
            vector_1[0, 2] = float(nodes_z[element_A[i]] - nodes_z[element_B[i]])
            vector_2[0, 0] = float(nodes_x[element_C[i]] - nodes_x[element_B[i]])
            vector_2[0, 1] = float(nodes_y[element_C[i]] - nodes_y[element_B[i]])
            vector_2[0, 2] = float(nodes_z[element_C[i]] - nodes_z[element_B[i]])
            square[i] = triangle_square(vector_1, vector_2)
        else:
            pass

    sum = 0
    for i in range(0, elements_num):
        sum = sum + square[i]

    #print(element_A)
    #print(element_B)
    #print(element_C)
    #print(square)
    #print(sum)
    f.close()

