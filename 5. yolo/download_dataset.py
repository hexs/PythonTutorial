from hexss import install_upgrade, github

install_upgrade('hexss')

api_url = "https://api.github.com/repos/hexs/Image-Dataset/contents/fine-a-red-hat"
github.download(api_url)
