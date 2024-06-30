import os
from dotenv import load_dotenv,find_dotenv
import instaloader

_=load_dotenv(find_dotenv())

ig_loader = instaloader.Instaloader()

ig_loader.login(os.getenv("IG_USR"), os.getenv("IG_PWD"))
profile = instaloader.Profile.from_username(ig_loader.context, "")


print()