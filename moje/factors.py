def factors (number):
  lista = []
  dzielnik = 2

  while dzielnik <= number:
    if number % dzielnik == 0:
      lista = lista + [dzielnik]  # trzeba wstawić starą zmienna i zrobić tą zmienną + element
      # lista.append(dzielnik)
      number = number // dzielnik  # / zwraca liczbę fload a // liczbę całkowitą
    else:
      dzielnik = dzielnik +1
      # dzielnik += 1
  return lista



# Rekurencja funkcji (wywołanie samej siebie w kółko)
def factors2 (number, dzielnik = 2):
  if dzielnik > number:   # warunek stopu dajemy na początku rekurencji
    return[]
  if number % dzielnik == 0:  # wywołujemy funkcje  w kółko, zastępuje pętle while
    return [dzielnik] + factors2 (number // dzielnik, dzielnik) # nie mogę dać number= bo wtedy drugi argument musze nazwać też dzielnik= 
  return factors2 (number, dzielnik + 1)


# z użyciem generatora 
def factors3 (number):
  dzielnik = 2

  while dzielnik <= number:
    if number % dzielnik == 0:
      yield dzielnik
      # lista = lista + [dzielnik]
      # list.append(dzielnik)
      number //= dzielnik
      # number = number // dzielnik
    else:
      dzielnik += 1
# w terminalu wpisujemy: list(factors3(liczba jaką chcemy iterować)) np list(factors3(60)) | next() | for...
# to jest tylko generator, yield działa leniwie, dopiero jak wywoła się konkretną liczbę


