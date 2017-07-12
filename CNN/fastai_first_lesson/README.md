## Introduction

I belive the http://course.fast.ai/ is the best course to learn deep learning on the web and that Floydhub is the easiest and cheapest way to run your deep learning models. 

This was orignally made by: https://github.com/YuelongGuo/floydhub.fast.ai . I've just added clarity on the sections I struggled with. 

## Prerequisites
* Python syntax: https://www.codecademy.com/learn/python [Takes 1-2 days]
* Command line: https://www.codecademy.com/learn/learn-the-command-line [Play around with it for a day]
* Git: https://www.codecademy.com/learn/learn-git [1-2 hours]
* Jupyter Notebook: https://www.youtube.com/watch?v=HW29067qVWk [Watch it play with it for 30 min]

## Set up floydhub account and working directory [1 - 10 min]

First, you'll need a floydhub account and have the floyd CLI installed. Follow their online instruction at https://www.floydhub.com/welcome. 

## Running your first Deep learning model
<pre><code>
git clone https://github.com/emilwallner/How-to-learn-AI.git
cd fastai_first_lesson/
</code></pre>

## Start a floydnet instance

We will use Floyd CLI to initiate a cloud instance. Use floyd init followed by a name for your experiment:

<pre><code>
floyd init dogscats
floyd run --mode jupyter --data yz3A8G5vX5ZQxv5VVyD3GH --env theano:py2 --gpu
</code></pre>

To start a GPU instance with Jupyter notebook that is compatable to lesson 1 scripts, you need to specify the following parameters:

<pre><code>
floyd run --mode jupyter --env theano:py2 --gpu
</code></pre>

Wait for a few minutes, then you should get a website address in your console for the running Jupyter notebook.

#### One more thing before running lesson 1 code

You need to configure the keras.json file . YuelongGuo has prepared a simple shell script. Just start a console session in jupyter notebook, then run:

<pre><code>
bash setup.sh
</code></pre>

Please note the home directory on Floydhub instance is actually /root/ directory.

Now lesson 1 should run with the sample dataset.

####

Now, we are ready to create the actual floydnet workspace to start learning fast.ai!
Assuming you have cloned this repo following the method running sample dataset.
<pre><code>
floyd init dogscats
floyd run \
  --mode jupyter \
  --data yz3A8G5vX5ZQxv5VVyD3GH \
  --env theano:py2 \
  --gpu
</code></pre>

Again, the data ID should be consistent with your unzipped data ID.

The data is available in the /input directory. So make sure you change the path to "/input/dogscats/"

Thanks to Sai for helping me out and pointing me to the right direction.
Now, start enjoy your 100 hours free GPU computing resources provided by floydhub.

One epoch took around 677s for me when I tried it out. Not bad at all!

---

## Appendix


#### scripts

The fast.ai github repository (https://github.com/fastai/courses/tree/master/deeplearning1/nbs) includes files for all the phase I lessons. For the purpose of this example, and to keep it simple, I copied only the bare minimul necessary files to the working directory. This includes:
* lesson1.ipynb
* utils.py
* vgg16.py
* vgg16bn.py

#### data

Instead of uploading data, we'll use Floydhub's hosted version of the dataset. [Check the original link if you want to learn how to upload data on Floydhub.](https://github.com/YuelongGuo/floydhub.fast.ai)

#### dependencies

Floydnet theano:py2 environment is missing one package - bcolz. For this, you need to add it to file "floyd_requirements.txt". This is the floydnet default for installing dependencies. It's already done, so you don't have to worry about it.
