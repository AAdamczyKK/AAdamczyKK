import random

lower_case_letter0 = chr(random.randint(65, 90))
lower_case_letter1 = chr(random.randint(65, 90))
upper_case_letter0 = chr(random.randint(65, 90))
upper_case_letter1 = chr(random.randint(65, 90))
digit0 = random.randint(0, 9)
digit1 = random.randint(0, 9)

Password = str(lower_case_letter1.lower()) + str(upper_case_letter0) + str(upper_case_letter1)+str(lower_case_letter0.lower()) + str(digit1) + str(digit0)
print(Password)
