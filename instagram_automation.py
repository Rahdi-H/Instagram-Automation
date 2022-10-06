from instabot import Bot
bot = Bot()
bot.login(username='rahdinhussain', password='123456')

# ----- to follow someone

bot.follow('myfavperson')

# ------ to upload photo

bot.upload_photo('photo.jpg', caption='this is captin')

# ------- to unfollow someone

bot.unfollow('hatedperson')

# --------- to send message

bot.send_message('hello sir', ['myfavperson', 'mayfavperson2'])

#----- to get followers info --------

followers=bot.get_user_followers('rahdinhussain')
for follower in followers:
    print(bot.get_user_info(follower))

#------to get following info

followings = bot.get_user_following('rahdinhussain')
for following in followings:
    print(bot.get_user_info(following))
