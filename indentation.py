# Correct:

# 类或者函数后空两格
# 每行的最大长度为79字符
# Add 4 spaces (an extra level of indentation) to distinguish arguments from
# the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)


# Aligned with opening delimiter.
# 参数换行缩进，左括号后有参数，则换行后参数与其垂直对齐。
var_one, var_two, var_three, var_four = 1, 2, 3, 4
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Hanging indents should add a level.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# 文件最后一行为空行
