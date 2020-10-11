import os
import zipfile


"""
# import os, zipfile
# #打包目录为zip文件（未压缩）
# def make_zip(source_dir, output_filename):
#   zipf = zipfile.ZipFile(output_filename, 'w')
#   pre_len = len(os.path.dirname(source_dir))
#   for parent, dirnames, filenames in os.walk(source_dir):
#     for filename in filenames:
#       pathfile = os.path.join(parent, filename)
#       arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
#       zipf.write(pathfile, arcname)
#   zipf.close()


# import os, tarfile
# #一次性打包整个根目录。空子目录会被打包。
# #如果只打包不压缩，将"w:gz"参数改为"w:"或"w"即可。
# def make_targz(output_filename, source_dir):
#   with tarfile.open(output_filename, "w:gz") as tar:
#     tar.add(source_dir, arcname=os.path.basename(source_dir))
# #逐个添加文件打包，未打包空子目录。可过滤文件。
# #如果只打包不压缩，将"w:gz"参数改为"w:"或"w"即可。
# def make_targz_one_by_one(output_filename, source_dir):
#   tar = tarfile.open(output_filename,"w:gz")
#   for root,dir,files in os.walk(source_dir):
#     for file in files:
#       pathfile = os.path.join(root, file)
#       tar.add(pathfile)
#   tar.close()
"""


def make_dirs_to_zip(source_dir, zip_name):
    """将文件打包成zip压缩包"""
    print("******************zip start******************")
    with zipfile.ZipFile(zip_name, "w") as z:
        # 出去要压缩的文件的路径长度(最右边不带斜杠)
        base_path_len = len(os.path.dirname(source_dir))
        for parent, dir_names, file_names in os.walk(source_dir):
            for file_name in file_names:
                file_path = os.path.join(parent, file_name)
                # 在zip包中的归档路径（用相对路径表示）
                archive_name = file_path[base_path_len:].strip(os.path.sep)
                z.write(file_path, archive_name)
    print("******************zip end******************")


if __name__ == "__main__":
    base_path = r"D:\PrivateProject\Python-Tags"
    source_dir_cur = os.path.join(base_path, r"NiceLib")
    # 最好用绝对路径，且生成zip的路径不能包含在要压缩的文件夹内部，否则会一直递归压缩，生成的zip包会越来越大
    # 如果运行生成zip的程序在需要压缩的文件夹内，则如果不用绝对路径设置压缩路径在要压缩的文件夹外部，则会产生递归压缩
    zip_name_cur = os.path.join(base_path, "NiceLib.zip")
    make_dirs_to_zip(source_dir_cur, zip_name_cur)
