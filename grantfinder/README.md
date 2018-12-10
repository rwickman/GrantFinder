# GrantFinder
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

### Verify installation

To verify that everything has been installed, do:

```sh
rails s -b 0.0.0.0
```

Then open up a web browser and go to `localhost:3000`

## Seed the Data

We are populating the database through a CSV and JSON data file for the Grant and GrantDescription model, respectively. So, you may need to run `rails db:seed` to perform this operation.
