# mental_health
Use this code to explore your own personal writing. I think it's useful to explore perspective from multiple angles. Figuring out the frequency through use of a word cloud tells a lot about what you're thinking when you are writing something that is based on experience and human emotions. Good mental health soul searching.

##Prerequisites
Use pip to install the matplotlib + pillow (PIL) module packages.
If you are using an OSX environment, I'd recommend installing Homebrew first, follow instructions for that here: http://brew.sh
```
brew install python
sudo pip install matplotlib
sudo pip install pillow
```
To get the word cloud package up and running, follow the command line instructions here: https://github.com/amueller/word_cloud
Beware to take note of necessary FONT-PATH changes for non-ubuntu environments.

##Get your repository set up
```
git clone https://github.com/ahjohns/mental_health
cd mental_health
cd files
```
Whatever personal writing you want to explore, it needs to be in a txt file. Easy way would be to edit experience.txt. You need to edit the .py files where appropriate.

##Begin by running the first program
Ya'll need to run all three .py scripts to get the right data.

```
python experience.py
python mentalhealth.py
python mentalhealthcloud.py
```

If you run into problems with required modules when you're making the cloud, check the path relative to the wordcloud package. They must be in the same site-package folder. Example of how to check the path in your system:
```
import wordcloud
wordcloud.__path__
```
