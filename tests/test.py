import instaloader

url = "https://www.instagram.com/p/Da3WVDbAGDR/"

shortcode = url.split("/p/")[1].split("/")[0]

loader = instaloader.Instaloader()

post = instaloader.Post.from_shortcode(
    loader.context,
    shortcode
)

print("Автор:", post.owner_username)
print("Тип:", post.typename)
print("Видео:", post.is_video)
print("Подпись:", post.caption[:100] if post.caption else "")