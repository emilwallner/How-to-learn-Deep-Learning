## The Basics
A practical, top-down approach, starting with high-level frameworks with a focus on Deep Learning.
- Spend a week on codecademy.com and learn the python syntax, command line and git. 
- Spend 1-2 weeks using Pandas and Scikit-learn on Kaggle problems using Jupyter Notebook. This gives you an overview of the machine learning mindset and workflow. 
- Spend 1-month implementing Keras models on cloud GPUs. This gives you a sense of the deep learning mindset and workflow. Start with [keras' examples.](https://github.com/keras-team/keras/tree/master/examples)
- Spend 1 month recoding the core concepts in python numpy, including a The Method of Least Squares, Gradient Descent, Linear Regression, The Perceptron and a vanilla neural network.

## Reproduce papers
By reproducing papers you get a feel for doing actual work in deep learning. I'd recommend reproducing a paper or building a project in the following four areas: CNN, LSTM, GAN, and reinforcement learning(or neuroevolution or neural programming).  For the first two areas reimplement [student papers.](http://cs231n.stanford.edu/reports.html) I'd recommend using Keras and reimplementing it from scratch.

The best way to get a feel for the most interesting ideas in Machine Learning is Twitter and [Arxiv-sanity](http://www.arxiv-sanity.com/). Here is my full list of people I [follow on Twitter](https://twitter.com/following). These are my favorites: [ilyasut](https://twitter.com/ilyasut), [josephreisinger](https://twitter.com/josephreisinger), [math_rachel](https://twitter.com/math_rachel), [mustafasuleymn](https://twitter.com/mustafasuleymn), [catherineols](https://twitter.com/catherineols), [dennybritz](https://twitter.com/dennybritz), [ylecun](https://twitter.com/ylecun), [jtoy](https://twitter.com/jtoy), [_brohrer_](https://twitter.com/_brohrer_), [tkasasagi](https://twitter.com/tkasasagi), [jeremyjkun](https://twitter.com/jeremyjkun), [jeffclune](https://twitter.com/jeffclune), [danielgross](https://twitter.com/danielgross), [karoly_zsolnai](https://twitter.com/karoly_zsolnai), [mortendahlcs](https://twitter.com/mortendahlcs), [Reza_Zadeh](https://twitter.com/Reza_Zadeh), [goodfellow_ian](https://twitter.com/goodfellow_ian), [fchollet](https://twitter.com/fchollet), [michael_nielsen](https://twitter.com/michael_nielsen), [iamtrask](https://twitter.com/iamtrask), [jeremyphoward](https://twitter.com/jeremyphoward), [jackclarkSF](https://twitter.com/jackclarkSF), [ch402](https://twitter.com/ch402), [distillpub](https://twitter.com/distillpub)

## Forums
- [FastAI](http://forums.fast.ai/)
- [Keras Slack](https://keras-slack-autojoin.herokuapp.com/)

Tips for reproducing papers:
- It takes 1-2 months to reproduce a student paper if you work full-time. It takes about 3 weeks to get clarity of the core concepts in each paper. 
- Spend the first week reimplementing the core algorithm in python numpy, say an RNN, neural network or CNN.
- Don't follow a step by step tutorial or MOOC. Instead, spend a few days scanning every MOOC and tutorial on the topic. This gives you an index of resources you can later dig deeper in. If you follow a step by step guide, you end up copy-pasting instead of learning anything.
- GPU access is key. My favorite GPU cloud provider is Floydhub. It's hands down the best option. If you have a GPU budget that is less than 100$/month I'd recommend colab.research.google.com. If you have a low budget, yet need a lot of compute, I'd recommend paying 100$ for producthunt.com's subscription, which gives you $7.5K in AWS cloud credit. Another good bet is Google's startup program through one of [their partners](https://docs.google.com/spreadsheets/d/15nQTTOoi9yoeRvsRXGNZeY46FA1pKPb0fq3_qNpzz3w/edit?usp=sharing) or apply via AIgrant.
- It's very cognitive demanding to learn deep learning. To feel a sense of progress, I'd recommend [scheduling everything you do.](https://twitter.com/EmilWallner/status/955684571202359297) Also, have a Pomodoro timer and [block all news/notifications/social media.](https://twitter.com/EmilWallner/status/948200877680201729)
- You don't need mentors. Having gone through a teaching-heavy education system, we often underestimate our capacity to learn by ourselves. Most Q&A/forums will offer little help in solving your bugs. The best option is to document the problem you are facing in detail, then research all the unknowns. I'd also suggest reaching out to the author of the paper you are reproducing. Again, if you reproduce student papers they are often happy to answer clarifying questions.

## Write-up of my process
- [Implementing Keras models (I started with TFlearn, but I'd highly recommend using Keras instead)](https://blog.floydhub.com/my-first-weekend-of-deep-learning/)
- [Recoding the core concepts in python](https://blog.floydhub.com/coding-the-history-of-deep-learning/)
- [My first paper using CNN](https://blog.floydhub.com/colorizing-b&w-photos-with-neural-networks/)
- [My first paper using LSTM](https://blog.floydhub.com/turning-design-mockups-into-code-with-deep-learning/)
- My first paper using GAN(in progress)
- My first paper using RL/evolution(in progress)
- [On going via my twitter feed](https://twitter.com/EmilWallner)

## Other good learning strategies:
- [Per Harald Borgen](https://medium.com/learning-new-stuff/machine-learning-in-a-year-cdb0b0ebd29c)
- [Greg Brockman](https://www.quora.com/What-are-the-best-ways-to-pick-up-Deep-Learning-skills-as-an-engineer)
- [Andrew Ng](https://www.youtube.com/watch?v=F1ka6a13S9I)
- [Amid Fish](http://amid.fish/reproducing-deep-rl)

If you have suggestions/questions create an issue or [ping me on Twitter.](https://twitter.com/EmilWallner)
