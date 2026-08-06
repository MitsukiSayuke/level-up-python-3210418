def palindrome (zdanie):
  
  zdanie = zdanie.lower()
  oryginal = []
  
  for znak in zdanie:
    if znak.isalpha():
      oryginal.append(znak)

  palindrom = oryginal[:: -1]

  return oryginal == palindrom  # krótsza wersja

  # if oryginal == palindrom:
  #   return True
  # else:
  #   return False
