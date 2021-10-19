from typing import Callable, TextIO
import requests
import sys,os

def download_file(url:str,save_path:str,chunk_size:int=1024,progress_callback:Callable[[int,int],None]=None)->str:
    """Downloads the file from the given URL string

    Args:
        url (str): URL to download the file from
        save_path (str): Local path to save the file to. Defaults to . (the current directory)
        chunk_size (int): Chunk size (in bytes) to pass to requests. Defaults to 1024
        progress_callback (Callable): Function to call on every progress update. Defaults to None
        Will be passed two integers, the first being the total bytes of the file, the second being the current number of bytes downloaded.

    Returns:
        str: The location of the downloaded file on the system.
        (Should be the same as save_path)
    """
    try:
        req=requests.get(url,stream=True)
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f'Couldn\'t download file "{url}"')
    
    with open(save_path,'wb') as file:
        total_length = int(req.headers.get('content-length'))
        for i,chunk in enumerate(req.iter_content(chunk_size=chunk_size)):
            file.write(chunk)
            if progress_callback is not None:
                progress_callback(total_length,i*chunk_size+len(chunk))
    
    return save_path
    
def local_path(*args):
    """Gets the path to a local file/folder.
        "Local" means the same directory as the .py/.exe file, unless the application is "frozen"/onefile, where it is sys._MEIPASS.
        All args are passed to os.path.join

    Returns:
        str: The absolute path to the file/folder
    """
    local=''
    if getattr(sys,'frozen',False) and hasattr(sys,'_MEIPASS'):
        local= sys._MEIPASS
    else:
        local= os.path.split(sys.argv[0])[0]
    return os.path.join(local,*args)



class ConsoleColorToHTMLStream(TextIO):
    """Custom TextIO stream class to convert console ASCII escape colors to HTML colors.
        For use with QT/PySide's "text browser" or other HTML outputs.

    """
    colors={
        "\033[00;32m":"LawnGreen",  # GREEN
         "\033[00;36m":"DeepSkyBlue",  # CYAN
        "\033[01;33m":"Orange",  # BOLD YELLOW
        "\033[01;31m":"Crimson",  # BOLD RED
         "\033[01;31m":"Crimson",  # BOLD RED
         "\x1b[00;32m":"LawnGreen",  # GREEN
         "\x1b[00;36m":"DeepSkyBlue",  # CYAN
        "\x1b[01;33m":"Orange",  # BOLD YELLOW
        "\x1b[01;31m":"Crimson",  # BOLD RED
         "\x1b[01;31m":"Crimson",  # BOLD RED
        }
    def __init__(self,callback):
        super(ConsoleColorToHTMLStream,self).__init__()
        self.callback=callback
    def isatty(self):return True
    def write(self,text:str):
        text=text.strip()
        text='<p style="margin:0;">'+text
        for key,val in self.colors.items():
            if key in text:
                text=text.replace(key,f'<span style="font-weight:bold;color:{val};">')
        text=(text.replace('\x1b[0m','</span>')+'</p>').replace('\n','<br>').replace('\r','')
        self.callback(text)