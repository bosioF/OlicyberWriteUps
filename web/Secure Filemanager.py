import nc

bannedwords = ['flag', 'secret', 'password', 'key']

def cleanup(filename):
  for word in bannedwords:
    filename = filename.replace(word, '')
  return filename

