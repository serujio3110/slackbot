# Slackbot developer guide

Thanks for your interest in developing Slackbot! These notes should help you produce pull requests that will get merged without any issues.

## Style guide

### Code style

There are places in the code that do not follow PEP 8 conventions. Do follow PEP 8 with new code, but do not fix formatting throughout the file you're editing. If your commit has a lot of unrelated reformatting in addition to your new/changed code, you may be asked to resubmit it with the extra changes removed.

### Commits

It's a good idea to use one branch per pull request. This will allow you to work on multiple changes at once.

Most pull requests should contain only a single commit. If you have to make corrections to a pull request, rebase and squash your branch, then do a forced push. Clean up the commit message so it's clear and as concise as needed.

## Developing

These steps will help you prepare your development environment to work on slackbot.

### Clone the repo

Begin by forking the repo. You will then clone your fork and add the central repo as another remote. This will help you incorporate changes as you develop.

```
$ git clone git@github.com:yourusername/slackbot.git
$ cd slackbot
$ git remote add upstream git@github.com:lins05/slackbot.git
```

Do not make commits to develop, even in your local copy. All commits should be on a branch. Start your branch:

```
$ git checkout develop -b name_of_feature
```

To incorporate upstream changes into your local copy and fork:

```
$ git checkout develop
$ git fetch upstream
$ git merge upstream/master
$ git push origin develop
```

See git documentation for info on merging, rebasing, and squashing commits.

### virtualenv/pyvenv

A virtualenv allows you to install the Python packages you need to develop and run slackbot without adding a bunch of unneeded junk to your system's Python installation. Once you create the virtualenv, you need to activate it any time you're developing or running slackbot. The steps are slightly different for Python 2 and Python 3. For Python 2, run:

```
$ virtualenv --no-site-packages .env
```

For Python 3, run:

```
$ pyvenv .env
```

Now that the virtualenv has been created, activate it and install the packages needed for development:

```
$ source .env/bin/activate
$ pip install -r requirements.txt
```

At this point, you should be able to run slackbot as described in the README.

### Configure tests

In order to run tests, you will need a slack instance. Create a free one at http://slack.com. Do not use an existing Slack for tests. The tests produce quite a bit of chat, and depending on how you set up Travis, it's possible for your API tokens to get leaked. Don't risk it. Use a slack created just for development and test.

#### setup bot and get tokens

** NOTE **
Slackbot depends on the RTM API, which is not available to new-style apps. The app it
uses must be a classic app.   

To create a classic app: <https://api.slack.com/apps?new_classic_app=1>
* Go to Features > App Home and add a legacy bot user
* Features > Oauth & Permissions. 
  * Add an OAuth Scope `bot`.
  * Install to workspace.  This will generate your bot's tokens.
(do NOT update to granular scopes as we need the rtm_connect functionality) 

Create a file named `slackbot_test_settings.py` and add the following settings:

```
# bot token
testbot_apitoken = 'xoxb-token'
testbot_username = 'testbot'
# user token
driver_apitoken = 'xoxp-token'  # note this is test user token NOT the bot user token - see note below
driver_username = 'your username'
test_channel = 'testchannel'
test_private_channel = 'testprivatechannel'
```

**Important note:** The bot token can be obtained by adding a custom bot integration (classic app) in Slack. User tokens can be obtained at https://api.slack.com/docs/oauth-test-tokens**. Slack tokens are like passwords! Don't commit them. If you're using them in some kind of Github or Travis automation, ensure they are for Slacks that are only for testing.

** **Note:** Test tokens for legacy custom integrations can no longer be issued for new
classic apps (although they can be re-issued for existing apps); this means the functional
tests will not work for a newly-created app.

At this point, you should be able to run tests:

```
$ pytest  # all tests
$ pytest test/unit  # just the unit tests
```

If you're signed into slack, you'll see your user account and bot account chatting with each other as the tests run.
