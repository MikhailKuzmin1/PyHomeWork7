import os

def files_in_folder(extension):
   base_path = os.getcwd()
   res_files = []
   files = os.listdir()
   for i in files:
      path = os.path.join(base_path, i)
      if os.path.isfile(path):
         if i.endswith(extension):
            res_files.append(i)
   return res_files


def rename_files(end_name:str, count_number:int, extension_file:str, end_extens:str, range_list:list = [0,0] ):
    files = files_in_folder(extension_file)
    count = 1
    len_files = len(files)
    first_num = ''
    count_zero = len(str(len_files))
    for _ in range(count_number - count_zero):
        first_num += '0'
    for i in files:
        first_name = i[range_list[0]-1:range_list[1]]
        end_names = f'{first_name}{end_name}{first_num}{count}.{end_extens}'
        os.rename(i,end_names)
        count += 1
