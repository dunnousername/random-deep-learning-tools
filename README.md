# random-deep-learning-tools
Random machine learning scripts I wrote, mainly for dataset formatting and collection, provided as-is.
## One of your programs doesn't work!
All of these programs are provided as-is. I try my best to make them usable.
I upload these programs to hopefully save people time, since I would otherwise just discard them.
However, if I screwed something up and just wasted an hour debugging it, I'm sorry!
You can submit a pull request or upload a fixed file in issues, and I'll try my best to merge it into master if it appears to work.
I can't promise it'll be accepted, and unless it's an easy fix I don't have the time to rewrite each of these programs.
That said, I'll try my best.
# Tools
## redditdl.py
Finds all/most images from a subreddit, for dataset use, using pushshift.io.
Some of these links may not be image files - make sure to remove .html and index files!
## verifier.py
a GUI program for [TrainYourOwnYOLO](https://github.com/AntonMu/TrainYourOwnYOLO) outputs to allow you to cherrypick outputs to feed back in.
## via2csv.py
a program that converts unlabeled [VIA](http://www.robots.ox.ac.uk/~vgg/software/via/via.html) JSON exports to standard csv format, like the one vott exports.
That is, `file,x1,y1,x2,y2,class`.
