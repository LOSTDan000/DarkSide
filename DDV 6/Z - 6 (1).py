st=''
def add(st):
    st = str(input(''))
    print('Количество удаленных символов',len(st)-len(st.replace('.','')))
    print(st.replace('.',''))
add(st)