"""Exemplos aula 09."""

frase = '  Curso em Vídeo Python  '
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[::2])
print("""Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(), upper(),
lower(), capitalize(), title(), strip(), junção com join().""")
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
frase = frase.replace('Python', 'Android')
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido[2][3])
