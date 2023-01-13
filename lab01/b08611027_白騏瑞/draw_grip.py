def draw_grid(m, n):
    a = '+ - - ' * n + '+'
    b = '/     ' * n + '/'
    print('\n'.join([a, b, b] * m + [a]))
       
draw_grid(2, 3)