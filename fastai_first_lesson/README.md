## Introduction
This is an examle of how to setup instance on floydhub to run lesson 1 of the awesome deep learning course available at http://course.fast.ai/. This document was revised March 5th 2017 and now works with the full dogscats dataset.

## Set up floydhub account and working directory
First, you'll need a floydhub account and have the floyd CLI installed. Follow their online instruction at https://www.floydhub.com/welcome.

Next, you'll want to create a working directory in your local computer. All files in this directory will be uploaded to the floydhub cloud instance when you do <code> floyd run </code> (explained in detail later). 

<pre><code>
mkdir ~/Projects/
cd ~/Projects/
</code></pre>

## Set up necessary files for lesson one

If you would like to skip all the details and just to get things going, you may choose to clone all files in this repo.

<pre><code>
git clone https://github.com/YuelongGuo/floydhub.fast.ai.git
cd floydhub.fast.ai/
</code></pre>

You may skip to the next section "Start a floydnet instance" if you choose to skip reading the details.

Well, a bit more details:

#### scripts

The fast.ai github repository (https://github.com/fastai/courses/tree/master/deeplearning1/nbs) includes files for all the phase I lessons. For the purpose of this example, and to keep it simple, I copied only the bare minimul necessary files to the working directory. This includes:
* lesson1.ipynb
* utils.py
* vgg16.py
* vgg16bn.py
* some sample data to work with

#### data

I copied the dogscats sample dataset (dogscats/sample if you unzip the dogscats.zip at http://www.platform.ai/files/dogscats.zip). However, this is considered very bad practice, because I am creating a copy of the data every time I start a new cloud instance. Please refer to the bottom section "Run for the full dogs and cats dataset" for data preperation best practice.

#### dependencies

The scripts written in lesson 1 runs with python 2 + Keras + Theano, so you need to specify <code> --env theano:py2 </code> when you start the cloud instance (more details below). However, Floydnet theano:py2 environment is still missing one package - bcolz. For this, you need to add it to file "floyd_requirements.txt". This is the floydnet default for installing dependencies.

<pre><code>
echo "bcolz" > floyd_requirements.txt
</code></pre>

## Start a floydnet instance

We will use Floyd CLI to initiate a cloud instance. Initiation:

<pre><code>
floyd init your_favorate_task_name_e.g._neural_networks
</code></pre>

To start a GPU instance with Jupyter notebook that is compatable to lesson 1 scripts, you need to specify the following parameters:

<pre><code>
floyd run \
  --mode jupyter \
  --env theano:py2 \
  --gpu
</code></pre>

Wait for a few minutes, then you should get a website address in your console for the running Jupyter notebook.

#### One more thing before running lesson 1 code

We are almost there, but there is one more thing we need to configure - the keras.json file

Start a console session in jupyter notebook, then 

<pre><code>
mkdir ~/.keras
echo '{
    "image_dim_ordering": "th",
    "epsilon": 1e-07,
    "floatx": "float32",
    "backend": "theano"
}' > ~/.keras/keras.json
</code></pre>

Please note the home directory on Floydhub instance is actually /root/ directory.

Now lesson 1 should run with the sample dataset.

## Run for the full dogs and cats dataset

For the full dataset, it is recommended that you build a data object in the floydnet. 

First, download the dogs and cats dataset to an empty folder: 

<pre><code>
cd ~/Projects/
mkdir floydhub.fast.ai.data.zipped
cd floydhub.fast.ai.data.zipped
wget http://www.platform.ai/files/dogscats.zip
</code></pre>

Next, upload the zipped dataset to floydnet, and create a floydnet dataset

<pre><code>
floyd data init dogscats.zipped
floyd data upload
</code></pre>

After the data finished upload, you should see something like this:

<pre><code>
Creating data source. Uploading files ...
DATA ID                 NAME                        VERSION
----------------------  ------------------------  ---------
UMSaLZVseGPSsPCbYkZFZA  userID/dogscats.zipped:1          1
</code></pre>

Now, we are ready to unzip the data on floydnet.
Again, start with an empty directory.

<pre><code>
cd ~/Projects/
mkdir floydhub.fast.ai.data.unzip
cd floydhub.fast.ai.data.unzip
floyd init dogscats.unzip
floyd run --gpu --data UMSaLZVseGPSsPCbYkZFZA "unzip /input/dogscats.zip -d /output"
</code></pre>

Please note:
1. the data ID should be the one you see from the above step
2. the mounted data is available in /input/ directory, and you need to direct the unzipped files to /output/ directory

After this finishes, which took about 20 mins for me, you'll see in your floydhub UI interface, under "Data" section, a dataset userID/dogscats.unzip:1/output. On the right side, click View -> Advanced -> under Id, keep a record of your data Id. Mine is yz3A8G5vX5ZQxv5VVyD3GH

Now, we are ready to create the actual floydnet workspace to start learning fast.ai!
Assuming you have cloned this repo following the method running sample dataset.
<pre><code>
cd ~/Projects/floydhub.fast.ai/
rm -r data
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
