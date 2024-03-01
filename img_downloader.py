import requests 
from rembg import remove

url = 'https://media.geeksforgeeks.org/wp-content/uploads/'
image_urls = ['20240302025345/black_rook.png', '20240302025325/white_knight.png', '20240302025943/white_king.png', '20240302025944/white_bishop.png', '20240302025945/black_pawn.png', '20240302025946/black_queen.png', '20240302025947/black_knight.png', '20240302025948/black_king.png', '20240302025949/white_rook.png', '20240302025951/black_bishop.png', '20240302025952/white_queen.png', '20240302025953/white_pawn.png']

for i in image_urls:
    new_url = url + i
    data = requests.get(new_url).content
    
    # Remove the background using rembg
    removed_bg = remove(data)
    
    # Save the image with the background removed
    with open('./images/'+i[i.index("/"):], 'wb') as f:   
        f.write(removed_bg)
