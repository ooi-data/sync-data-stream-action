import os
import time
import subprocess
import datetime
import yaml
import sys

from github import GitHub

IGNORE_REPOS = [
    'ooi-harvester',
    'staged-harvest',
    'helm-charts',
    'docker-images',
    'discrete-sample',
    'specification',
    'qaqc',
    'read-history-status-action',
    'PyGithub',
    'stream_template',
    'status',
]

def  main():
    GH_PAT = os.environ.get("GH_PAT", None)
    GH_ORG = os.environ.get("INPUT_GH_ORG", None)
    GH_MAIN_BRANCH = os.environ.get("INPUT_GH_MAIN_BRANCH", "main")
    DEBUG = os.environ.get("INPUT_DEBUG", "false").upper()
    if GH_PAT:
        try:
            gh = Github(GH_PAT)
            if GH_ORG is None:
                print("Github organization not provided! Exiting action.")
                args = ["echo", "::set-output", f"name=sync_status::failed"]
                subprocess.call(args)
                sys.exit(0)
            org = gh.get_organization(GH_ORG)
            for repo in org.get_repos():
                if repo.name not in IGNORE_REPOS:
                    try:
                        print(f"Syncing {repo.full_name} with template ...")
                        update_template = repo.get_workflow('update-template.yaml')
                        print(update_template)
                        if DEBUG == "FALSE":
                            update_template.create_dispatch(GH_MAIN_BRANCH)
                    except Exception:
                        print(
                            f"{repo.full_name} doesn't have template update workflow .. skipping .."
                        )
                        continue
            print(f"Syncing Finished.")
            args = ["echo", "::set-output", f"name=sync_status::success"]
            subprocess.call(args)
        except Exception as e:
            print(f"Error found: {e}")
            args = ["echo", "::set-output", f"name=sync_status::failed"]
            subprocess.call(args)
            sys.exit(0)
    else:
        print("Please provide github personal access token as environment variable!")


if __name__ == "__main__":
    main()
