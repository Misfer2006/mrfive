if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Misfer2006/mrfive.git /mrfive
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /mrfive
fi
cd /mrfive
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
