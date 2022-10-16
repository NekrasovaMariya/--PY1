src = not False and True or False and not True

result = True and True or False and True #упростили отрицание
result = True or False #упростили логическое "и"
result = True #упростили логическое "или"
print(src == result)
