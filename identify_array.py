def __read__(name):
    with open(name) as f:
        read_data = f.read()
    f.closed
    return read_data


def locate(read_str):
    num_upper = read_str.index('$Nodes')
    num_lower = read_str.index('$EndNodes')
    return num_lower, num_upper


def figure(figure_str):
    return figure_str.count('\n')


def sort(handle_str, sort_lower_, sort_upper_, fig):
    n = 0
    position_x = {}
    position_y = {}
    position_z = {}
    label = [0] * fig * 2
    start = handle_str.index('\n')
    temp = ''
    x = ''
    y = ''
    z = ''
    judge = 0
    for k in range(start+1, sort_upper_ - sort_lower_ - 7):
        if handle_str[k] == ' ':
            if judge == 0:
                label[n] = temp
            elif judge == 1:
                position_x[label[n]] = x
            else:
                position_y[label[n]] = y
            judge = judge+1
        elif handle_str[k] == '\n':
            position_z[label[n]] = z
            n = n + 1
            temp = ''
            x = ''
            y = ''
            z = ''
            judge = 0
        else:
            if judge == 0:
                temp = temp + handle_str[k]
            elif judge == 1:
                x = x + handle_str[k]
            elif judge == 2:
                y = y + handle_str[k]
            else:
                z = z + handle_str[k]
    return position_x, position_y, position_z


file_name = 'untitled.msh'
str_name = __read__(file_name)
print(locate(str_name))
upper, lower = locate(str_name)
fig = figure(str_name[lower+7: upper])
print(fig)
__x__, __y__, __z__ = sort(str_name[lower+7: upper], lower, upper,fig)
#print(__x__)
#print(__y__)
#print(__z__)
N = input('please input the label = ')
if N in __x__:
    print('the position is :')
    print(__x__[N],__y__[N],__z__[N])
else:
    print('the label does not exist, please input again')

