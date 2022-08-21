Now that you have created the virtual environment, you will need to activate it before you can use it in your project.

```bash
sudo apt-get install python-dev libffi-dev libssl-dev

# Riak suggests using python2.7
virtualenv -p /usr/bin/python2.7 venv

source venv/bin/activate

pip install riak

pip install -r requirements.txt

# if you install new packages
# pip freeze > requirements.txt

deactivate
```

This will activate your virtual environment. Immediately, you will notice that your terminal path includes env, signifying an activated virtual environment.
