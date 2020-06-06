## Approach
A practical, top-down approach, starting with high-level frameworks with a focus on Deep Learning.

---

Language versions: [Korean](https://github.com/emilwallner/How-to-learn-Deep-Learning/blob/master/README_kr.md) | [English](https://github.com/emilwallner/How-to-learn-Deep-Learning/blob/master/README.md)

## Getting started [2 months]

There are three main goals to get up to speed with deep learning: 
1) Get familiar to the tools you will be working with, e.g. Python, the command line and Jupyter notebooks
2) Get used to the workflow, everything from finding the data to deploying a trained model
3) Building a deep learning mindset, an intuition for how deep learning models behave and how to improve them

- Spend a week on codecademy.com and learn the python syntax, command line and git. If you don't have any previous programming experience, it's good to spend a few months learning how to program. Otherwise, it's easy to become overwhelmed. 
- Spend one to two weeks using [Pandas](https://www.youtube.com/watch?v=yzIMircGU5I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y) and [Scikit-learn](http://scikit-learn.org/stable/) on [Kaggle problems](https://www.kaggle.com/competitions?sortBy=grouped&group=general&page=1&pageSize=20&category=gettingStarted) using [Jupyter Notebook on Colab](https://colab.research.google.com/notebooks/welcome.ipynb), e.g. [Titanic](https://www.kaggle.com/c/titanic), [House prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques), and [Iris](https://www.kaggle.com/uciml/iris). This gives you an overview of the machine learning mindset and workflow. 
- Spend one month implementing models on cloud GPUs. Start with [FastAI and PyTorch](http://course.fast.ai/). The FastAI community is the go-to place for people wanting to apply deep learning and share the state of the art techniques.

Once you have done this, you will know how to add value with ML. 


## Portfolio [3 - 12 months]

Think of your portfolio as evidence to a potential employer that you can provide value for them.

When you are looking for your first job, there are four main roles you can apply for 
1. Machine Learning Engineering, 
1. Applied Machine Learning Researcher / Residencies, 
1. Machine Learning Research Scientist, and 
1. Software Engineering. 

A lot of the work related to machine learning is pure software engineering roles (category 4), e.g. scaling infrastructure, but that's out of scope for this article. 

It's easiest to get a foot in the door if you aim for Machine Learning Engineering roles. There are a magnitude more ML engineering roles compared to category 2 & 3 roles, they require little to no theory, and they are less competitive. Most employers prefer scaling and leveraging stable implementations, often ~1 year old, instead of allocating scarce resources to implement SOTA papers, which are often time-consuming and seldom work well in practice.  

Once you can cover your bills and have a few years of experience, you are in a better position to learn theory and advance to category 2 & 3 roles. This is especially true if you are self-taught, you often have an edge against an average university graduate. In general, graduates have weak practical skills and strong theory skills. 

### Context

You'll have a mix of  3 - 10 technical and non-technical people looking at your portfolio, regardless of their background, you want to spark the following reactions: 
* the applicant has experience tackling our type of problems,
* the applicant's work is easy to understand and well organized, and
* the work was without a doubt 100% made by the applicant.

Most ML learners end up with the same portfolio as everyone else. Portfolio items include things as MOOC participation, dog/cat classifiers, and implementations on toy datasets such as the titanic and iris datasets. They often indicate that you actively avoid real-world problem-solving, and prefer being in your comfort zone by copy-pasting from tutorials. These portfolio items often signal negative value instead of signaling that you are a high-quality candidate.

A unique portfolio item implies that you have tackled a unique problem without a solution, and thus have to engage in the type of problem-solving an employee does daily. A good starting point is to look for portfolio ideas on [active Kaggle competitions](https://www.kaggle.com/competitions), and [machine learning consulting projects](https://www.upwork.com/freelance-jobs/machine-learning/), and demo versions of [common production pipelines](https://github.com/chiphuyen/machine-learning-systems-design/blob/master/build/build1/consolidated.pdf). Here's a Twitter thread on [how to come up with portfolio ideas](https://twitter.com/EmilWallner/status/1184723538810413056).

Here are rough guidelines to self-assess the strength of your portfolio:

#### Machine learning engineering:

Even though ML engineering roles are the most strategic entry point, they are still highly competitive. In general, there are ~50 software engineering roles for every ML role. From the self-learners I know, 2/3 fail to get a foot in the door and end up taking software engineering roles instead. You are ready to look for a job when you have two high-quality projects that are well-documented, have unique datasets, and are relevant to a [specific industry](https://towardsdatascience.com/the-cold-start-problem-how-to-build-your-machine-learning-portfolio-6718b4ae83e9), say banking or insurance. 

Project Type | Base score | 
-------------| -----------|
Common project | -1 p ||
Unique project | 10 p |

Multiplier Type | Factor
-----------------|-----------------
Strong documentation | 5x
5000-word article | 5x
Kaggle Medal | 10x
Employer relevancy | 20x
 
* __Hireable:__ 5,250 p
* __Competative:__ 15,000 p



#### Applied research / research assistant/ residencies:

For most companies, the risk of pursuing cutting edge research is often too high, thus only the biggest companies tend to need this skillset. There are smaller research organizations that hire for these positions, but these positions tend to be poorly advertised and have a bias for people in their existing community. 

Many of these roles don't require a Ph.D., which makes them available to most people with a Bachelor's or Master's degrees, or self-learners with one year of focussed study. 

Given the status, scarcity, and requirements for these positions, they are the most competitive ML positions. Positions at well-known companies tend to get more than a thousand applicants per position.

Daily, these roles require that you understand and can implement SOTA papers, thus that's what they will be looking for in your portfolio. 


Projects type | Base score
--------------| -----------
Common project | -10 p
Unique project | 1 p
SOTA paper implementation | 20 p

Multiplier type | Factor
----------------| --------------- 
Strong documentation | 5x
5000-word article | 5x
SOTA performance | 5x
Employer relevancy | 20x

* __Hireable:__  52,500 p
* __Competitive:__ 150,000 p


#### Research Scientist:

Research scientist roles require a Ph.D. or equivalent experience. While the former category requires the ability to implement SOTA papers, this category requires you to come up with research ideas. The mainstream research community measure the quality of research ideas by their impact, [here is a list of the venues and their impact](https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng_artificialintelligence). To have a competitive portfolio, you need two published papers in the top venues in an area that's relevant to your potential employer.

Project type | Base score
-------------| ----------------
Common project | -100 p
An unpublished paper | 5 p
ICML/ICLR/NeurIPS publication | 500p
All other publications | 50 p

Multiplier type | Factor
------------------| ------------------
First author paper | 10x
Employer relevancy | 20x

* __Hireable:__ 20,000 p
* __Competitive roles and elite PhD positions:__ 200,000 p

__Examples:__
* My first portfolio item (after 2 months of learning): [Code](https://github.com/emilwallner/Coloring-greyscale-images) | [Write-up](https://blog.floydhub.com/colorizing-b-w-photos-with-neural-networks/)
* My second portfolio item (after 4 months of learning): [Code](https://github.com/emilwallner/Screenshot-to-code) | [Write-up](https://blog.floydhub.com/turning-design-mockups-into-code-with-deep-learning/)
* [Dylan Djian's](https://github.com/dylandjian) first portfolio item: [Code](https://github.com/dylandjian/retro-contest-sonic) | [Write-up](https://dylandjian.github.io/world-models/)
* [Dylan Djian's](https://github.com/dylandjian) second portfolio item: [Code](https://github.com/dylandjian/SuperGo) | [Write-up](https://dylandjian.github.io/alphago-zero/)
* [Reiichiro Nakano's](https://github.com/reiinakano) first portfolio item: [Code](https://github.com/reiinakano/arbitrary-image-stylization-tfjs) | [Write-up](https://magenta.tensorflow.org/blog/2018/12/20/style-transfer-js/)
* [Reiichiro Nakano's](https://github.com/reiinakano) second portfolio item: [Write-up](https://reiinakano.com/2019/01/27/world-painters.html)

Most recruiters will spend 10-20 seconds on each of your portfolio items. Unless they can understand the value in that time frame, the value of the project is close to zero. Thus, writing and documentation are key. Here's another thread on how to [write about portfolio items](https://twitter.com/EmilWallner/status/1162289417140264960). 

The last key point is relevancy. It's more fun to make a wide range of projects, but if you want to optimize for breaking into the industry, you want to do all projects in one niche, thus making your skillset **super** relevant for a specific pool of employers.

__Further Inspiration:__
* [FastAI student projects](https://forums.fast.ai/t/share-you-work-here-highlights/57140)
* [Stanford NLP student projects](https://nlp.stanford.edu/courses/cs224n/)
* [Stanford CNN student projects](http://cs231n.stanford.edu/index.html)


## Theory 101 [4 months]

Learning how to read papers is critical if you want to get into research, and a brilliant asset as an ML engineer. There are three key areas to feel comfortable reading papers:
1) Understanding the details of the most frequent algorithms, gradient descent, linear regression, and MLPs, etc
2) Learning how to translate the most frequent math notations into code
3) Learn the basics of algebra, calculus, statistics, and machine learning

- For the first week, spend it on 3Blue1Brown's [Essence of linear algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab), [the Essence of Calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM&list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr), and StatQuests' [the Basics (of statistics)](https://www.youtube.com/watch?v=qBigTkBLU6g&list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9) and [Machine Learning](https://www.youtube.com/watch?v=Gv9_4yMHFhI&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF). Use a spaced repetition app like Anki and memorize all the key concepts. Use images as much as possible, they are easier to memorize. 
- Spend one month [recoding the core concepts](https://github.com/eriklindernoren/ML-From-Scratch) in python numpy, including least squares, gradient descent, linear regression, and a vanilla neural network. This will help you reduce a lot of cognitive load down the line. Learning that notations are compact logic and how to translate it into code will make you feel less anxious about the theory.
-  I believe the best deep learning theory curriculum is the [Deep Learning Book](http://www.deeplearningbook.org/) by Ian Goodfellow and Yoshua Bengio and Aaron Courville. I use it as a curriculum, and the use online courses and internet resources to learn the details about each concept. Spend three months on part 1 of the Deep learning book. The MachineLearningGod shows a [great way to study the book.](https://www.youtube.com/watch?v=bzp5bQY7XmE&list=PLh6SAYydrIpc8uCGc_KxjLSDRV6tfT10u&index=2) Use lectures and videos to understand the concepts, Khan academy type exercises to master each concept, and Anki flashcards to remember them long-term. 

**Key Books:**
- [Deep Learning Book](http://www.deeplearningbook.org/) by Ian Goodfellow and Yoshua Bengio and Aaron Courville.
- [Deep Learning for Coders with fastai and PyTorch: AI Applications Without a PhD](https://www.amazon.com/gp/product/1492045527/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1) by Jeremy Howard and Sylvain.
Gugger.
- [Deep Learning with Python](https://www.manning.com/books/deep-learning-with-python) by François Chollet.
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) by Michael Nielsen.
- [Grokking Deep Learning](https://www.manning.com/books/grokking-deep-learning) by Andrew W. Trask.


## Forums
- [FastAI](http://forums.fast.ai/)
- [Keras Slack](https://keras-slack-autojoin.herokuapp.com/)
- [Distill Slack](https://join.slack.com/t/distillpub/shared_invite/enQtMzg1NzU3MzEzMTg3LWJkNmQ4Y2JlNjJkNDlhYTU2ZmQxMGFkM2NiMTI2NGVjNzJkOTdjNTFiOGZmNDBjNTEzZGUwM2U0Mzg4NDAyN2E)
- [Pytorch](https://discuss.pytorch.org/)
- Twitter

## Other good learning strategies:
- [Emil Wallner](https://blog.floydhub.com/emils-story-as-a-self-taught-ai-researcher/)
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
