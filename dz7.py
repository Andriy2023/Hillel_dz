"""Convert a non-negative integer num toits English words representation."""


# Function to receive numbers and convert to words
def number_to_words(num):
    if 100 <= num <= 999:
        # Списки слов для единиц, десятков и сотен
        ones = ['', 'One', 'Two', 'Three', 'Four',
                'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty',
                'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        # Разделение числа на сотни, десятки и единицы
        hundreds_digit = num // 100
        tens_digit = (num % 100) // 10
        ones_digit = num % 10

        # Формирование строки с английским представлением числа
        repres = ''
        if hundreds_digit > 0:
            repres += ones[hundreds_digit] + ' Hundred'
            if tens_digit > 0 or ones_digit > 0:
                repres += ' '

        if tens_digit == 1:
            repres += teens[ones_digit]
        else:
            repres += tens[tens_digit]
            if ones_digit > 0:
                repres += ' ' + ones[ones_digit]

        return repres
    else:
        return 'Enter the correct number'


# Пример использования функции
num = int(input('Enter a non-negative num >= 100 and <= 999 : '))
output = number_to_words(num)
print(output)
