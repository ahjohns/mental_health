# mental_health
Use this code to explore your own personal writing. I think it's useful to explore perspective from multiple angles. Figuring out the frequency through use of a word cloud tells a lot about what you're thinking when you are writing something that is based on experience and human emotions.

##Prerequisites
Use pip to install the matplotlib module package.
If you are using an OSX environment, I'd recommend installing Homebrew first, follow instructions for that here: http://brew.sh
```
brew install python
sudo pip install matplotlib
sudo pip install pillow
```
To get the word cloud package up and running, follow the command line instructions here: https://github.com/amueller/word_cloud
Beware to take note of special note about file-names for non-ubuntu environments.

##Get your repository set up
```
git clone https://github.com/ahjohns/mental_health
cd mental_health
```
Whatever personal writing you want to explore, it needs to be in a txt file. You need to edit the .py files where appropriate.

##Begin by running the first program
Ya'll need to run all three .py scripts to get the right data.

```
python experience.py
```

If you run into problems with required modules when you making the cloud, for instance, the PIL module, check the path relative to the wordcloud package. They must be in the same site-package folder. Example of how to check the path:
```
import wordcloud
wordcloud.__path__
```
