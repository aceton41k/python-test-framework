# reading
with open('D:/drive/work/rostelecom_testing.txt', 'r', encoding='utf-8') as file:
    # Код внутри блока контекста
    contents = file.read()
    print(contents)


# writing
def test_writing():
    with open('D:/drive/work/python_file_to_write.txt', 'w', encoding='utf-8') as pup:
        # Код внутри блока контекста
        listing = 'gggg, cow, slumby'.strip(' ')
        for i in listing.split(','):
            pup.write(f'line {i}\n')
        # print(contents)
