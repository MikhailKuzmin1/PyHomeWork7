import os

def all_files():
   base_path = os.getcwd()
   res_files = []
   files = os.listdir()
   for i in files:
      path = os.path.join(base_path, i)
      if os.path.isfile(path):
        res_files.append(i)
   return res_files

def move_files():
    files = all_files()
    movi = ('mp4','avi')
    image = ('jpg','png')
    song = ('mp3', 'aud')
    for i in files:   
       if i.endswith(movi):
          os.replace(i, f'movi/{i}')
       elif i.endswith(image):
          os.replace(i, f'image/{i}')
       elif i.endswith(song):
          os.replace(i, f'song/{i}')
