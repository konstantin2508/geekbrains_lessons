# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

bit_and = 5 & 6
print(f'Результат побитового "И": {bit_and}')

bit_or = 5 | 6
print(f'Результат побитового "ИЛИ": {bit_or}')

bit_xor = 5 ^ 6
print(f'Результат побитового "исключающее ИЛИ": {bit_xor}')

bit_right = 5 >> 2
print(f'Результат побитового сдвига вправо на два знака над числом "5": {bit_right}')

bit_left = 5 << 2
print(f'Результат побитового сдвига влево на два знака над числом "5": {bit_left}')