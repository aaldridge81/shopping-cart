## shopping-cart
Shopping Cart Project to print receipt for customers at your grocery store

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Clone the repo from (https://github.com/aaldridge81/shopping-cart), then navigate into the project repo

```sh
cd shopping-cart
```


## Environment Setup

Use Anaconda to create and activate a new virtual environment, called "shopping-env": 
```sh
conda create -n shopping-env python=3.8
conda activate shopping-env 
```

from inside virtual environment, install package dependencies:
```sh
pip install -r requirements.text
```

> NOTE: If installation causes an error message, make sure you are navigating within the repository's root directiory, where the requirements.txt file exists 

## Setup

In the root directory of your local repository, create a new file called ".env" and update the contents of the ".env" file to comply with your states tax rate:
        TAX_RATE = .07

## Usage
To run the program, in the command line:

```py
python shopping.cart.py
```

## adapted from the "my-first-python-app" README file

