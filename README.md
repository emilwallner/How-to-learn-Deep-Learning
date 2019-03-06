## Approach
A practical, top-down approach, starting with high-level frameworks with a focus on Deep Learning. It will enable you to create your own projects and land jobs at start-ups. To invent [new deep learning algorithms](https://www.reddit.com/r/MachineLearning/comments/73n9pm/d_confession_as_an_ai_researcher_seeking_advice/), also check the theory section. 

## Practical
**Note:** You don't need a math background (I only know high school math), but a lot of determination. I found learning deep learning as hard as learning to program in C (my first programming language).
- Spend a week on codecademy.com and learn the python syntax, command line and git. 
- Spend one to two weeks using [Pandas](https://www.youtube.com/watch?v=yzIMircGU5I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y) and [Scikit-learn](http://scikit-learn.org/stable/) on [Kaggle problems](https://www.kaggle.com/competitions?sortBy=grouped&group=general&page=1&pageSize=20&category=gettingStarted) using [Jupyter Notebook](https://www.youtube.com/watch?v=HW29067qVWk&t=375s), e.g. [Titanic](https://www.kaggle.com/c/titanic), [House prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques), and [Iris](https://www.kaggle.com/uciml/iris). This gives you an overview of the machine learning mindset and workflow. 
- Spend one month implementing models on cloud GPUs. Most beginners tend to start with Keras with a Tenorflow-backend or Pytorch using the FastAI library. Start with [these Keras models](https://github.com/keras-team/keras/tree/master/examples) or the [official Pytorch tutorials](https://pytorch.org/tutorials/). Also, check [the resources from FastAI.](http://course.fast.ai/) The FastAI community if becoming the go-to place for people wanting to apply deep learning and share the state of the art techniques.
- Spend one month [recoding the core concepts](https://github.com/emilwallner/Deep-Learning-From-Scratch) in python numpy, including a The Method of Least Squares, Gradient Descent, Linear Regression, The Perceptron and a vanilla neural network. Andrew Trask's [book](https://www.manning.com/books/grokking-deep-learning) and [blog](https://iamtrask.github.io/) are great for this. This will help you reduce a lot of cognitive load down the line. 

## Reproducing Papers
By reproducing papers you get a feel for doing actual work in deep learning. I'd recommend reproducing a paper or building a project in the following four areas: CNN, LSTM, GAN, and reinforcement learning.  For the first two areas, I'd recommend reimplementing [student papers.](http://cs231n.stanford.edu/reports.html) I'd recommend using Keras or Pytorch and reimplementing it from scratch.

**Tips for reproducing papers:**
- It takes 1-2 months to reproduce a student paper if you work full-time. It takes about 3 weeks to get clarity of the core concepts in each paper.
- Find github reimplementations, but avoid looking at repos using the same framework as you, since the temptation to copy-paste will be too high. Read all the repo issues, since the language is easier and you have a high chance of struggling with the same things.
- I often build the network in four steps. Start with one data example and make anything that runs. At this stage, it's okay if you only understood 20% of the paper and your network is buggy. Once you have something to experiment, it makes it a lot easier to add the remaining 80% of the knowledge. For the second stage, I start automating the training flow and try to overfit the network. Once you can overfit the model, I build a structure to create a network that can generalize. For the final part, I implement multiprocessing and optimize the CPU and GPU utilization. 
- Discussions online are in general a good way to understand a paper better. Google is a good starting point, but also check reviewing sites such as [openreview](openreview.net), [Arxiv-sanity](http://www.arxiv-sanity.com/) or [Twitter search](https://twitter.com/search-advanced).
- After reproducing 2-3 papers you will be able to reproduce a paper in a few days or weeks.  
- Spend the first week reimplementing the core algorithm in python numpy, say an RNN, neural network or CNN.
- Don't follow a step by step tutorial or MOOC. Instead, spend a few days scanning every MOOC and tutorial on the topic. This gives you an index of resources you can later dig deeper in. If you follow a step by step guide, you end up copy-pasting instead of learning anything.
- It's very cognitive demanding to learn deep learning. To feel a sense of progress, I'd recommend [scheduling everything you do.](https://twitter.com/EmilWallner/status/955684571202359297) Also, have a Pomodoro timer and [block all news/notifications/social media.](https://twitter.com/EmilWallner/status/948200877680201729)
- Most Q&A/forums will offer little help in solving your bugs. The best option is to document the problem you are facing in detail, then research all the unknowns. It often helps if you refactor your code and make small tests to try different assumptions about your model. I'd also suggest reaching out to the author of the paper you are reproducing. Again, if you reproduce student papers they are often happy to answer clarifying questions.

## Forums
- [FastAI](http://forums.fast.ai/)
- [Keras Slack](https://keras-slack-autojoin.herokuapp.com/)
- [Distill Slack](https://join.slack.com/t/distillpub/shared_invite/enQtMzg1NzU3MzEzMTg3LWJkNmQ4Y2JlNjJkNDlhYTU2ZmQxMGFkM2NiMTI2NGVjNzJkOTdjNTFiOGZmNDBjNTEzZGUwM2U0Mzg4NDAyN2E)
- [Pytorch](https://discuss.pytorch.org/)

The best way to get a feel for the most interesting ideas in Machine Learning is Twitter and [Arxiv-sanity](http://www.arxiv-sanity.com/). Here is my full list of people I [follow on Twitter](https://twitter.com/following). These are my favorites: [hardmaru](https://twitter.com/hardmaru), [ilyasut](https://twitter.com/ilyasut), [josephreisinger](https://twitter.com/josephreisinger), [math_rachel](https://twitter.com/math_rachel), [mustafasuleymn](https://twitter.com/mustafasuleymn), [catherineols](https://twitter.com/catherineols), [dennybritz](https://twitter.com/dennybritz), [ylecun](https://twitter.com/ylecun), [jtoy](https://twitter.com/jtoy), [_brohrer_](https://twitter.com/_brohrer_), [tkasasagi](https://twitter.com/tkasasagi), [jeremyjkun](https://twitter.com/jeremyjkun), [jeffclune](https://twitter.com/jeffclune), [danielgross](https://twitter.com/danielgross), [karoly_zsolnai](https://twitter.com/karoly_zsolnai), [mortendahlcs](https://twitter.com/mortendahlcs), [Reza_Zadeh](https://twitter.com/Reza_Zadeh), [goodfellow_ian](https://twitter.com/goodfellow_ian), [fchollet](https://twitter.com/fchollet), [michael_nielsen](https://twitter.com/michael_nielsen), [iamtrask](https://twitter.com/iamtrask), [jeremyphoward](https://twitter.com/jeremyphoward), [jackclarkSF](https://twitter.com/jackclarkSF), [ch402](https://twitter.com/ch402), [distillpub](https://twitter.com/distillpub)

## Theory
I'd recommend starting with the practical approach, then you'll be familiar with many of the concepts when you start adding theoretical knowledge. I had 18 months of practical experience before I started digging into the theory. I'm using the [Deep Learning Book](http://www.deeplearningbook.org/) by Ian Goodfellow and Yoshua Bengio and Aaron Courville. 

I'm using Michael Nielsen's [Anki method](http://augmentingcognition.com/ltm.html) to process the material. 
- I normally spend 6 hours reading 5 - 20 pages and finding YouTube tutorials to understand every concept. This includes doing exercises on Khan Academy and redoing derivations from lectures on Youtube.
- Then I spend 2 - 3 hours creating Anki cards. I have one deck for questions I can rehearse on the go, and another for exercises I need a pen and paper for. 
- I spend another hour reviewing previous Anki cards and exercises.

I set aside three months to study the Deep Learning Book fulltime. The book is 700 pages, so aim to ankify 10 - 15 pages per day. The first few chapters are denser, so I began with 5 pages a day and gradually got closer to 15 pages. 

Once you have a broad theoretical knowledge of deep learning, I'd recommend Ankifying ~100 papers in the field you want to build an edge in. I'm using [OpenAI's curriculum and paper recommendations](https://spinningup.openai.com/en/latest/) to get up to speed with the research in deep reinforcement learning. 

## GPU access
GPU access is key. If you want a fully configured development environment, Floydhub is perfect. If you have a GPU budget that is less than 100$/month I'd recommend colab.research.google.com. The offer free TPU instances for ~6h. Kaggle.com also offers free ~6h training sessions on Tesla K80s. If you have a low budget, yet need a lot of compute, I'd recommend paying 100$ for producthunt.com's subscription, which gives you $7.5K in AWS cloud credit. 

But the best option is to create a deep learning startup and apply for cloud credit. You don't need more than a [landing page](https://readymag.com/) and a [company email](https://www.zoho.eu/) to get $5K-100K in cloud credit. You can apply on [Google's startup program](https://cloud.google.com/developers/startups/) or through one of [their partners](https://docs.google.com/spreadsheets/d/15nQTTOoi9yoeRvsRXGNZeY46FA1pKPb0fq3_qNpzz3w/edit?usp=sharing). AWS, Digital Ocean, Azure, and Alibaba also have cloud credit programs for startups.

If you have +$3K budget, building [your own rig is a great option.](https://medium.com/the-mission/why-building-your-own-deep-learning-computer-is-10x-cheaper-than-aws-b1c91b55ce8c) 


## Write-up of my process
- [Implementing Keras models (I started with TFlearn, but I'd highly recommend using Keras instead)](https://blog.floydhub.com/my-first-weekend-of-deep-learning/) (I mistakenly thought TFlearn was the official frontend. They have now made Keras the official front-end to Tensorflow.)
- [Recoding the core concepts in python](https://blog.floydhub.com/coding-the-history-of-deep-learning/)
- [My first paper using CNN](https://blog.floydhub.com/colorizing-b&w-photos-with-neural-networks/)
- [My first paper using LSTM](https://blog.floydhub.com/turning-design-mockups-into-code-with-deep-learning/)
- [My first paper using a GAN](http://www.aiartonline.com/design/emil-wallner/)
- [My first paper using RL/evolution](https://github.com/corewarai/open_project)
- [On going via my twitter feed](https://twitter.com/EmilWallner)

## Other good learning strategies:
- [Per Harald Borgen](https://medium.com/learning-new-stuff/machine-learning-in-a-year-cdb0b0ebd29c)
- [Greg Brockman](https://www.quora.com/What-are-the-best-ways-to-pick-up-Deep-Learning-skills-as-an-engineer)
- [Andrew Ng](https://www.youtube.com/watch?v=F1ka6a13S9I)
- [Amid Fish](http://amid.fish/reproducing-deep-rl)
- [Spinning Up by OpenAI](https://spinningup.openai.com/en/latest/spinningup/spinningup.html)
- [Confession as an AI researcher](https://www.reddit.com/r/MachineLearning/comments/73n9pm/d_confession_as_an_ai_researcher_seeking_advice/)

If you have suggestions/questions create an issue or [ping me on Twitter.](https://twitter.com/EmilWallner)
