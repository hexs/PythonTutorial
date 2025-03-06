from hexss import install_upgrade, github

install_upgrade('hexss')

api_url = "https://api.github.com/repos/hexs/Image-Dataset/contents/flower_photos"
github.download(api_url, 50)

api_url = "https://api.github.com/repos/hexs/Image-Dataset/contents/pet_photos"
github.download(api_url, 50)
