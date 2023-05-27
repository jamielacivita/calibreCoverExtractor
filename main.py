import glob
from pdf2image import convert_from_path


def main():
    pass


def makeFirstPageJpeg(output_folder=r"D:\_Calibre\Unknown\Chemical Analysis and Interaction (13070)", filename="BOS.pdf"):
    """
    :param output_folder: The folder into which we are adding a cover file.
    :param filename: the name of the .PDF we want to turn the first page into a cover.
    :return: None - side effect is to add a cover.jpg file into the output_folder which is the first page of the .pdf file.
    """
    print("In makeFirstPageJpeg\n")
    output_folder = output_folder.split("\*")[0]
    print(f"folder : {output_folder}")
    print(f"file : {filename}")
    pages = convert_from_path(filename, dpi=500, first_page=1, last_page=1, output_folder=output_folder, output_file="cover", fmt="jpeg", single_file=True)
    #print(pages)

    #for count, page in enumerate(pages):
    #    page.save(f'out{count}.jpg', 'JPEG')
    pages[0].save("cover.jpg", "JPEG")

    return None

def getfilenames(path=r"D:\_Calibre\Unknown\Chemical Analysis and Interaction (13070)\*"):
    """
    :param path: a path to a directory
    :return: a list of filenames in that directory
    """
    filenames_lst = []
    for name in glob.glob(path):
        filenames_lst.append(name)
    return filenames_lst

def countpdfs(filenames_lst):
    """
    :param filenames_lst: a list of filenames with extentsions
    :return: the integer number of .pdf files in the given list.
    """
    count = 0
    for n in filenames_lst:
        if ".pdf" in n:
            count = count + 1
    return count

def getpdfpath(filenames_lst):
    for n in filenames_lst:
        if ".pdf" in n:
            return n
    return None




if __name__  == "__main__":
    #makeFirstPageJpeg("HTML.pdf")
    #set the directory to search in.
    path = r"D:\_Calibre\Unknown\The Coming of the Third Reich by R (13157)\*"
    path = r"D:\_Calibre\Unknown\Chemical Analysis and Interaction (13070)\*"
    path = r"D:\_Calibre\Unknown\Canals of Mars (1975) (13069)\*"
    path = r"D:\_Calibre\Unknown\Computer Simulations of Planetary (13066)\*"
    path = r"D:\_Calibre\Unknown\COSPAR Meetings in Prague (1969) (13062)\*"
    path = r"D:\_Calibre\Unknown\CQ Amateur Radio March 2021 (13112)\*"
    path = r"D:\_Calibre\Unknown\Dreams Are Maps (Planetary Report, (13060)\*"
    path = r"D:\_Calibre\Unknown\European Team Championship, Skara (13144)\*"
    path = input("Enter the path : ")
    path = path + "\*"
    #get a list of files in that directory
    names = getfilenames(path)
    #count the number of .pdf files.
    count = countpdfs(names)
    print(count)
    if count == 1:
        file = getpdfpath(names)
        print(f"path : {path}")
        print(f"file : {file}")
        #make the cover file
        print(makeFirstPageJpeg(path, file))

    print("Done.")


    #D:\_Calibre\Unknown\Chemical Analysis and Interaction (13070)