def stam():
    def lets_do_it(a=0):
        print('lets do it')
        return a*10
    return lets_do_it

aa = stam( )
print(aa("@a@a"))