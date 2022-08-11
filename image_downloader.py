import urllib.request
from image_link_fetcher import *
def download_images(images,file_path='./images/'):
     """
    Give input as a dictionary with keywords and their respective url's,
    you get the output dictionary with keywords and their relative location as corresponding values.    
    The image will be downloaded in the /images directory within the current working directory
    
    Parameters:
    dictionary: Dictionary with image title as key and image URL as the value associated with the key
    
    Returns:
    dictionary: Dictionary with image title as key and image location on the local device the value associated with the key
  
    """
    image_loc = {}
    for key in images:
        full_path = file_path + key + '.jpg'
        image_loc[key] = full_path
        urllib.request.urlretrieve(images[key], full_path)
    return image_loc
#Here is an example, Uncomment it to test it.
#download_images(get_img_links(["Transistors","capacitors","moores law"]))
