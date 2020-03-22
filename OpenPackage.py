import os
import sublime
import sublime_plugin


class OpenPackageCommand(sublime_plugin.TextCommand):
    def run(self, edit, path):
        print('path')

    def input(self, args):
        return ListPackagesInputHandler()


class ListPackagesInputHandler(sublime_plugin.ListInputHandler):
    def name(self):
        return 'path'

    def list_items(self):
        packages_path = sublime.packages_path()
        print('packages_path', packages_path)
        plugin_folders = list(os.listdir(packages_path))

        items = []
        for folder in plugin_folders:
            items.append(
                (folder, os.path.join(packages_path, folder))
            )

        return items
