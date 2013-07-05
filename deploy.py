#!/usr/bin/python

import os
import shutil

def list_dotfiles_and_directories():

    def get_dotfiles_directory():
        return os.path.dirname(os.path.abspath(__file__))

    def list_dotfiles(directory):
        qualify = lambda filename: os.path.join(directory, filename)
        return [qualify(f) for f in os.listdir(directory) if f.startswith('.')]

    def split_files_from_directories(files):
        return (
            [f for f in files if os.path.isfile(f)],
            [f for f in files if os.path.isdir(f)])

    return split_files_from_directories(list_dotfiles(get_dotfiles_directory()))

def deploy_file(filepath):
    os.system('ln -sf %s ~' % filepath)

def deploy_directory(dirpath):

    def get_deployed_path():
        return os.path.abspath(os.path.join('~', os.path.basename(dirpath)))

    def get_backup_path():
        return get_deployed_path() + '.old'

    deployed = get_deployed_path()
    # if os.path.isdir(deployed):

        # backup = get_backup_path()
        # if os.path.isdir(backup):
            # shutil.rmtree(backup)
        # shutil.copytree(deployed, backup)

    os.system('ln -sf %s ~' % dirpath)

def main():

    files, directories = list_dotfiles_and_directories()
    map(deploy_file, files)
    map(deploy_directory, directories)

if __name__ == '__main__':
    main()
