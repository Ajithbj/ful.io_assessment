import re

def is_valid_phone_number(phone_number):
  patterns = [
    r'^\+?[1-9]\d{1,14}$', # E.164 format
    r'^\+\d{1,3}\s?\d{1,3}\s?\d{4,10}$', # +XX XXX XXXXXXX
    r'^\(\d{1,3}\)\s?\d{3}\s?\d{4}$', # (XXX) XXX XXXX
    r'^\d{3}\-\d{3}\-\d{4}$', # XXX-XXX-XXXX 
    r'\d{3}\.\d{3}\.\d{4}', # XXX.XXX.XXXX
    r'^\d{3}\s\d{3}\s\d{4}$', # XXX XXX XXXX
    r'^\+?\d{1,3}\-\d{1,3}\-\d{4,10}$', # [+]XX-XXX-XXXXXXXX
    r'^1\-\d{3}\-\d{3}\-\d{4}' # 1-XXX-XXX-XXXX
  ]

  for pattern in patterns:
    if re.match(pattern, phone_number):
      return True
  
  return False

contact_numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

for number in contact_numbers:
    if is_valid_phone_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")
