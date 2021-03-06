import sublime
import sublime_plugin
import os

import subprocess
import re

import threading
import json

from urllib.request import Request, urlopen


DEBUG = False


def debug(*args):
    if DEBUG:
        print('GithubPR -> ', *args)


def is_git_repo():
    root = sublime.active_window().extract_variables()['folder']
    # TODO: maybe for WINDOWS use join path ??
    return os.path.exists("{}/.git".format(root))


class Command:
    ''' Responsible for running git comands throught `subprocess`
    and returning it's output. '''

    def __init__(self):
        self.window = sublime.active_window()
        self.project_root = self.window.extract_variables()['folder']

    def git_remote_v(self):
        cmd = ['git remote -v']
        return self.run(cmd)

    def git_fetch(self, pr, remote):
        cmd = "git fetch {} pull/{}/head:{}/{}".format(
            remote["name"],
            pr["number"],
            pr["user"]["login"],
            pr["head"]["ref"]
        )

        return self.run(cmd)

    def git_checkout(self, branch_name):
        cmd = "git checkout {}".format(branch_name)
        return self.run(cmd)

    def git_remote_add(self, remote_name, repository_url):
        cmd = " git remote add {} {}".format(remote_name, repository_url)
        return self.run(cmd)

    def git_fetch_upstream(self):
        cmd = "git fetch upstream"
        return self.run(cmd)

    def git_merge(self, branch_name):
        cmd = "git merge {}".format(branch_name)
        return self.run(cmd)

    def run(self, cmd):
        p = subprocess.Popen(cmd,
                             bufsize=-1,
                             cwd=self.project_root,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True)
        output, stderr = p.communicate()
        if (stderr):
            return stderr.decode('utf-8')
            debug('😱 Error with Command: {}\n{}'.format(cmd, stderr))
        return output.decode('utf-8')


class GithubListPullRequestCommand(sublime_plugin.WindowCommand):
    def is_visible(self):
        return is_git_repo()

    def run(self):
        self.remotes = get_remotes()

        if len(self.remotes) == 0:
            debug('⛅ List of remotes is 0')
            return

        titles = list(map(lambda remote: remote["name"], self.remotes))
        if len(self.remotes) > 1:
            self.window.show_quick_panel(titles, self.on_select_remote)
        else:
            list_pull_requests(self.remotes[0])

    def on_select_remote(self, index):
        if index > -1:
            list_pull_requests(self.remotes[index])


def get_remotes():
    if not is_git_repo():
        return []

    command = Command()
    output = command.git_remote_v()

    remotes = output.splitlines()
    unique_remotes = []
    for remote in remotes:
        name, url_and_method = re.split(r'\t+', remote)

        # parse username and repo from url_and_method
        # url_and_method >> 'https://github.com/predragnikolic/sublime-git-diff-view.git (push)
        url, _method = url_and_method.split()
        # url >> 'https://github.com/predragnikolic/sublime-git-diff-view.git

        # stript github and .git
        username_and_repo = url.replace("https://github.com/", "")
        username_and_repo = username_and_repo.replace(".git", "")
        # url >> predragnikolic/sublime-git-diff-view

        username, repo = username_and_repo.split("/")

        rem = {
            "name": name,
            "username": username,
            "repo": repo
        }

        if rem not in unique_remotes:
            unique_remotes.append(rem)

    return unique_remotes


def list_pull_requests(remote):
    sublime.status_message('Fetching Pull Requests from "{}"'.format(remote["name"]))

    t = threading.Thread(target=fetch_pull_request, args=(remote,))
    t.start()


def fetch_pull_request(remote):
    url = "https://api.github.com/repos/{}/{}/pulls".format(
        remote["username"],
        remote["repo"]
    )
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        # see how the response looks at
        # https://developer.github.com/v3/pulls/#list-pull-requests
        pull_requests = json.loads(urlopen(req).read().decode('utf-8'))
        if len(pull_requests) < 1:
            sublime.status_message('No Pull Requests')
            return
        select_pull_requsest(pull_requests, remote)
    except:
        debug('👻 fetching pull request gone wrong')


def select_pull_requsest(pull_requests, remote):
    window = sublime.active_window()

    def on_select_pr(index):
        if index > -1:
            checkout_pull_request(pull_requests[index], remote)

    titles = list(map(lambda pr: ["#{} {}".format(pr["number"], pr["title"]), "{}:{}".format(pr["user"]["login"], pr["head"]["ref"])], pull_requests))

    if len(pull_requests) > 0:
        window.show_quick_panel(titles, on_select_pr)


def checkout_pull_request(pr, remote):
    window = sublime.active_window()
    command = Command()
    branch_name = "{}/{}".format(pr["user"]["login"], pr["head"]["ref"])
    sublime.status_message("Fetching {}:{}".format(pr["user"]["login"], branch_name))
    command.git_fetch(pr, remote)

    output = command.git_checkout(branch_name)

    window.run_command('update_github_output_panel', {
        "output": output
    })


class UpdateGithubOutputPanel(sublime_plugin.TextCommand):
    def run(self, edit, output):
        window = self.view.window()
        panel = get_output_panel()

        panel.replace(edit, sublime.Region(0, panel.size()), output)
        window.run_command("show_panel", {"panel": "output.github_pr"})


def get_output_panel():
    window = sublime.active_window()

    panel = window.find_output_panel('github_pr')
    if panel is None:
        panel = window.create_output_panel('github_pr')

    panel.set_syntax_file('Packages/Text/Plain text.tmLanguage')
    return panel


class RemoteNameInputHandler(sublime_plugin.ListInputHandler):
    def name(self):
        return "remote_name"

    def placeholder(self):
        return 'remote_name'

    def validate(self, name):
        return len(name) > 0

    def list_items(self):
        return ['origin', 'upstream']

    def next_input(self, _args):
        return RemoteUrlInputHandler()


class RemoteUrlInputHandler(sublime_plugin.TextInputHandler):
    def name(self):
        return "remote_url"

    def placeholder(self):
        return 'https://github.com/owner/repo.git'

    def validate(self, name):
        return len(name) > 0


class GithubAddRemoteCommand(sublime_plugin.WindowCommand):
    def input(self, args):
        return RemoteNameInputHandler()

    def run(self, remote_name, remote_url):
        taken_names = list(map(lambda remote: remote['name'], get_remotes()))

        if remote_name in taken_names:
            sublime.status_message('⚠ {} remote name is already taken!'.format(remote_name))
            return

        command = Command()
        command.git_remote_add(remote_name, remote_url)

        self.window.run_command('update_github_output_panel', {
            "output": "Added remote {} for {}".format(remote_name, remote_url)
        })


def sync_fork():
    command = Command()

    # Fetch the branches and their respective commits from the upstream repository
    output = command.git_fetch_upstream()

    # Check out your fork's local master branch
    output += command.git_checkout('master')

    # Merge the changes from upstream/master into your local master branch.
    output += command.git_merge('upstream/master')

    window = sublime.active_window()
    window.run_command('update_github_output_panel', {
        "output": output
    })


class GithubSyncForkCommand(sublime_plugin.WindowCommand):
    def is_visible(self):
        if len(get_remotes()) > 1:
            return True
        return False

    def run(self):
        t = threading.Thread(target=sync_fork)
        t.start()


        