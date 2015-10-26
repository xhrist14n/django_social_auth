clear
rm ./home/*.pyc
rm ./socialapp/*.pyc
rm ./django_social_auth/*.pyc
git add . -f
git commit -am "django social auth app"
git push origin master
