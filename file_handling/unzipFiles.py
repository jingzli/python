def unzipFiles():
    zip_file_path = "C:\AA\BB"
    file_list = os.listdir(path)
    abs_path = []
    for a in file_list:
        x = zip_file_path+'\\'+a
        print x
        abs_path.append(x)
    for f in abs_path:
        zip=zipfile.ZipFile(f)
        zip.extractall(zip_file_path)
    pass
