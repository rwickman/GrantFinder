# GrantFinder
## Overview
GrantFinder is a Web App built with Ruby on Rails. Its purpose is to allow researchers to easily find grants from the National Institutes of Health (NIH) website by using our Search Engine. Initially I scrapped descriptions of each grant from the website to populate the database. Next, I applied Latent Semantic Analysis (LSA) on the dataset as a preprocessing step. Finally, when a user enters in a query, it will compute the cosine similarity to find related grants.

## Installation

If you are cloning this repo from scratch, you will need to run the following commands:

```sh
gem install bundler
bundle install
rails db:migrate
rails db:seed
sudo apt-get remove --purge -y nodejs
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

source ~/.bashrc
nvm install --lts
```
Make sure you have python3.x installed as well.
Furthermore, we are using the gensim library for LSA computations, so you will need to install it with pip3. If you do not have pip3 installed please run:

```sh
sudo apt-get install python3-pip python-dev build-essential 
```

Then to install gensim, do:
```
sudo pip3 install gensim
```

### Verify installation

To verify that everything has been installed, do:

```sh
rails s -b 0.0.0.0
```

Then open up a web browser and go to `localhost:3000`


## How To Login
 * When you load The GrantFinder Web App you will be prompted to login
 * Ther are two user names reserved for testing: user1@email.com and user2@email.com
 * Both have password: dddddd(that's 6 lowercase d's)
 * Use either of the usernames to do an initial login
 * Alternatively, you can sign up using an email that is not the same as either of the usernames reserved for testing
 
## Seed the Data

We are populating the database through a CSV and JSON data file for the Grant and GrantDescription model, respectively. So, you may need to run `rails db:seed` to perform this operation.
