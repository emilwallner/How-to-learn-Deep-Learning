## Approach
A practical, top-down approach, starting with high-level frameworks with a focus on Deep Learning.

## Getting started [2 months]

There are three main goals to get up to speed with deep learning: 
1) Get familiar to the tools you will be working with, e.g. Python, the command line and Jupyter notebooks
2) Get used to the workflow, everything from finding the data to deploying a trained model
3) Building a deep learning mindset, an intuition for how deep learning models behave and how to improve them

- Spend a week on codecademy.com and learn the python syntax, command line and git. If you don't have any previous programming experience, it's good to spend a few months learning how to program. Otherwise, it's easy to become overwhelmed. 
- Spend one to two weeks using [Pandas](https://www.youtube.com/watch?v=yzIMircGU5I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y) and [Scikit-learn](http://scikit-learn.org/stable/) on [Kaggle problems](https://www.kaggle.com/competitions?sortBy=grouped&group=general&page=1&pageSize=20&category=gettingStarted) using [Jupyter Notebook](https://www.youtube.com/watch?v=HW29067qVWk&t=375s), e.g. [Titanic](https://www.kaggle.com/c/titanic), [House prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques), and [Iris](https://www.kaggle.com/uciml/iris). This gives you an overview of the machine learning mindset and workflow. 
- Spend one month implementing models on cloud GPUs. Start with [FastAI and PyTorch](http://course.fast.ai/). The FastAI community is the go-to place for people wanting to apply deep learning and share the state of the art techniques.

Once you have done this, you will know how to add value with ML. 


## Portfolio [3 - 12 months]

Your portfolio is a gateway to new opportunities, so focus on things you have an interest in. It's also an opportunity to explore different areas in machine learning. If you're not sure where to start, I'd start with a computer vision project and a language-related project (NLP). Here's a Twitter thread on [how to come up with portfolio ideas](https://twitter.com/EmilWallner/status/1184723538810413056), and here's another thread on how to [write about them](https://twitter.com/EmilWallner/status/1162289417140264960). 

A common mistake is to collect online course certificates instead of building projects. Employers tend to not value course certificates because they don't trust the rigor of mass accreditation. Instead, the internet-educated need tangible evidence of their knowledge:

- Publishing paper at good conferences
- Winning ML competitions
- Pull requests to established open source projects
- 50-100K readers on ML related topics
- ML tools with +100 weekly users
- ML gig/job
- ML art

If you are not sure of a good first project or where to begin, direct message people on Twitter. Find people on Twitter whos work inspire you, tell them what you have done so far and what you hope to achieve. Write a personal message to 50-100 people - you'll be surprised at how helpful people are. Just make sure you have done your homework and read up on best practices for cold outreach. 

## Theory 101 [1-3 months]

Learning how to read papers is a great source to improve your projects, and critical if you want to get into research. There are three key areas to feel comfortable reading papers:
1) Understanding the details of the most frequent algorithms, gradient descent, linear regression, and MLPs, etc
2) Learning how to translate the 50 most frequent math notations
3) Learn the basics of algebra, calculus, statistics, and machine learning

- Spend one month [recoding the core concepts](https://github.com/emilwallner/Deep-Learning-From-Scratch) in python numpy, including least squares, gradient descent, linear regression, and a vanilla neural network. Andrew Trask's [book](https://www.manning.com/books/grokking-deep-learning) and [blog](https://iamtrask.github.io/) are great for this. This will help you reduce a lot of cognitive load down the line. 
-  I believe the best deep learning theory curriculum is the [Deep Learning Book](http://www.deeplearningbook.org/) by Ian Goodfellow and Yoshua Bengio and Aaron Courville. I use it as a curriculum, and the use the internet to learn the details about each concept. Although, it's good to have six months of practical experience or a math/statistic background before you start with the theory. 
- Most of the value comes from memorizing the math notations on the first few pages. Learning that notations are compact logic and how to translate it into code will make you feel less anxious about the theory. If you have a week spare, I'd spend it on 3Blue1Brown's [Essence of linear algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab), [the Essence of Calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM&list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr), and StatQuests' [the Basics (of statistics)](https://www.youtube.com/watch?v=qBigTkBLU6g&list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9) and [Machine Learning](https://www.youtube.com/watch?v=Gv9_4yMHFhI&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF). Use a spaced repetition app like Anki and memorize all the key concepts. Use images as much as possible, they are easier to memorize. 
- If you have 2-3 months, spend it on part 1 of the Deep learning book. The MachineLearningGod shows a [great way to study the book.](https://www.youtube.com/watch?v=bzp5bQY7XmE&list=PLh6SAYydrIpc8uCGc_KxjLSDRV6tfT10u&index=2) Use lectures and videos to understand the concepts, and then use Anki and Khan academy exercises to learn them. 

## Your first paper [6 - 12 months]

![alt text](https://i.imgur.com/SMSyuhV.jpg)

[WIP]



## Forums
- [FastAI](http://forums.fast.ai/)
- [Keras Slack](https://keras-slack-autojoin.herokuapp.com/)
- [Distill Slack](https://join.slack.com/t/distillpub/shared_invite/enQtMzg1NzU3MzEzMTg3LWJkNmQ4Y2JlNjJkNDlhYTU2ZmQxMGFkM2NiMTI2NGVjNzJkOTdjNTFiOGZmNDBjNTEzZGUwM2U0Mzg4NDAyN2E)
- [Pytorch](https://discuss.pytorch.org/)
- Twitter


## Write-up of my process
- [Implementing Keras models (I started with TFlearn, but I'd highly recommend using Keras instead)](https://blog.floydhub.com/my-first-weekend-of-deep-learning/) (I mistakenly thought TFlearn was the official frontend. They have now made Keras the official front-end to Tensorflow.)
- [Recoding the core concepts in python](https://blog.floydhub.com/coding-the-history-of-deep-learning/)
- [My first paper using CNN](https://blog.floydhub.com/colorizing-b&w-photos-with-neural-networks/)
- [My first paper using LSTM](https://blog.floydhub.com/turning-design-mockups-into-code-with-deep-learning/)
- [My first paper using a GAN](http://www.aiartonline.com/design/emil-wallner/)
- [My first paper using RL/evolution](https://github.com/corewarai/open_project)
- [On going via my twitter feed](https://twitter.com/EmilWallner)

## Other good learning strategies:
- [S. Zayd Enam](http://ai.stanford.edu/~zayd/why-is-machine-learning-hard.html)
- [Catherine Olsson](https://80000hours.org/articles/ml-engineering-career-transition-guide/)
- [Greg Brockman V2](https://blog.gregbrockman.com/how-i-became-a-machine-learning-practitioner)
- [Greg Brockman V1](https://www.quora.com/What-are-the-best-ways-to-pick-up-Deep-Learning-skills-as-an-engineer)
- [Andrew Ng](https://www.youtube.com/watch?v=F1ka6a13S9I)
- [Amid Fish](http://amid.fish/reproducing-deep-rl)
- [Spinning Up by OpenAI](https://spinningup.openai.com/en/latest/spinningup/spinningup.html)
- [Confession as an AI researcher](https://www.reddit.com/r/MachineLearning/comments/73n9pm/d_confession_as_an_ai_researcher_seeking_advice/)
- YC Threads: [One](https://news.ycombinator.com/item?id=20765553) and [Two](https://news.ycombinator.com/item?id=18421422)

If you have suggestions/questions create an issue or [ping me on Twitter.](https://twitter.com/EmilWallner)
