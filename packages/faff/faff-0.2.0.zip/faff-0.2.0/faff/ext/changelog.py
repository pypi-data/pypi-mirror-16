#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import collections
from datetime import datetime
import jinja2
import faff


class ChangeLog(object):
    """Change log generation using Git version control commit messages.

    `path`
        Absolute path to git repository.
    `name`
        File name of output, defaults to `CHANGELOG.md`.

    By default the following commit message format is supported::

        <category>(<audience>): <subject>

        <body>
    """
    # TODO: Command line options.
    # TODO: Use message format string for configuration.
    # "{CATEGORY}({AUDIENCE}): {SUBJECT}\n\n{BODY}"
    # TODO: Configurable categories, audiences.
    CATEGORIES = ("added", "changed", "removed", "fixed")
    ALL = "all"
    AUDIENCES = ("user", "developer", ALL)

    def __init__(self, path, name="CHANGELOG.md"):
        # Path to git repository, change log file.
        self._path = os.path.abspath(str(path))
        self._file = os.path.join(self._path, name)

        # Jinja2 environment.
        root = os.path.abspath(os.path.dirname(__file__))
        templates = os.path.join(root, "templates")
        self._env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(templates),
        )

        # Check that git is available.
        if faff.Run.is_installed("git --version"):
            # Get tags, commits data from repository.
            self._tags = self._get_tags()
            self._commits = self._get_commits()

            # Process tags, commits into internal data.
            self._data = self._get_data()

            # Render and write change log to file.
            with open(self._file, "w") as f:
                self._render_changelog(f)

        # TODO: Raise exception or write error if not installed.

    # Private methods.

    def _get_tags(self):
        tags = collections.OrderedDict()

        # Get git repository tags.
        gittags = faff.Run("git tag", self._path, hide=True)
        gittags = gittags.get_output().split("\n")

        # For each tag get commit hash.
        for tag in gittags:
            cmd = "git rev-list -n 1 {}".format(tag)
            chash = faff.Run(cmd, self._path, hide=True)

            # Add tag/hash to ordered dictionary.
            tags[tag] = chash.get_output()

        return tags

    def _get_commits(self):
        # Load git repository commits into index.
        # Git commit format for processing.
        fmt = (
            "commit=%H",
            "author=%an",
            "date=%aI",
            "subject=%s",
            "body=%b",
        )
        cmd = 'git log --format="{}'.format("%n".join(fmt))
        cmd += '%n%n%n"'

        # Git log command output.
        # TODO: Exception handling.
        gitlog = faff.Run(cmd, self._path, hide=True)
        gitlog = gitlog.get_output()
        # Git log split into commits.
        gitlog = gitlog.split("\n\n\n\n")

        commits = collections.OrderedDict()
        for commit in gitlog:
            data = {}

            # Extract commit hash.
            chash = commit.split("author=", 1)[0]
            chash = chash.strip("\n").split("=")
            if len(chash) < 2:
                continue

            # Extract commit author.
            cauthor = commit.split("author=", 1)[1]
            cauthor = cauthor.split("date=", 1)[0]
            data["author"] = cauthor.strip("\n")

            # Extract commit date.
            cdate = commit.split("date=", 1)[1]
            cdate = cdate.split("subject=", 1)[0]
            # Remove timezone information for parsing.
            cdate = cdate.strip("\n").split("+", 1)[0]
            data["date"] = datetime.strptime(cdate, "%Y-%m-%dT%H:%M:%S")

            # Extract commit subject.
            csubject = commit.split("subject=", 1)[1]
            csubject = csubject.split("body=", 1)[0]
            data["subject"] = csubject.strip("\n")

            # Extract commit body.
            cbody = commit.split("body=", 1)[1]
            data["body"] = cbody.strip("\n")

            # Add commit data to index.
            commits[chash[1]] = data

        return commits

    def _get_data(self):
        data = collections.OrderedDict()

        for tag, thash in self._tags.items():
            data[tag] = {
                # Date for tag acquired from commits.
                "date": self._commits[thash]["date"],
                # Commits associated with tag.
                "commits": [],
            }

            # Compare commit dates to tag, pop and append to commit list where
            # dates are less than or equal.
            pop_list = []
            for commit, cdata in self._commits.items():
                if cdata["date"] <= data[tag]["date"]:
                    pop_list.append(commit)

            for commit in pop_list:
                data[tag]["commits"].append(self._commits.pop(commit))

        # Add unreleased tag and pop any remaining commits.
        data["unreleased"] = {
            "date": None,
            "commits": [],
        }

        commits = list(self._commits.keys())
        for commit in commits:
            data["unreleased"]["commits"].append(self._commits.pop(commit))

        # Extract categories, audiences from commit subjects.
        for tag, tdata in data.items():
            commits = []

            for commit in tdata["commits"]:
                # Split subject into prefix.
                parts = commit["subject"].split(":", 1)
                if len(parts) < 2:
                    continue

                # Split prefix into category.
                prefix_parts = parts[0].split("(", 1)
                category = prefix_parts[0].strip()

                # Split prefix into audience if available, default to all.
                audience = self.ALL
                if len(prefix_parts) > 1:
                    audience = prefix_parts[1].rstrip(")")

                # Check category and audience.
                if category not in self.CATEGORIES:
                    continue
                if audience not in self.AUDIENCES:
                    continue

                # Create new commit data.
                cdata = {
                    "author": commit["author"],
                    "category": category,
                    "audience": audience,
                    "subject": parts[1].strip(),
                }
                commits.append(cdata)

            # Overwrite commits list with parsed data.
            tdata["commits"] = commits

        return data

    def _render_changelog(self, f):
        # TODO: Different change log formats.
        template = self._env.get_template("CHANGELOG.md")
        context = {"audiences": []}

        # Add each audience to context, excluding all.
        for audience in self.AUDIENCES[:-1]:
            adata = {
                "name": audience.capitalize(),
                "tags": [],
            }

            # Add tags to audiences.
            for tag, tdata in reversed(self._data.items()):
                tdata2 = {
                    "name": tag,
                    "categories": [],
                }
                filt_commits = []

                # Add date if available.
                if tdata["date"] is not None:
                    tdata2["date"] = tdata["date"].strftime("%Y-%m-%d")

                # Filter commits based on audience.
                for commit in tdata["commits"]:
                    ca = commit["audience"]
                    if (ca == audience) or (ca == self.ALL):
                        filt_commits.append(commit)

                # Sort commits for each category.
                for category in self.CATEGORIES:
                    cdata = {
                        "name": category.capitalize(),
                        "commits": [],
                    }

                    # Filter commits based on category.
                    for commit in filt_commits:
                        if commit["category"] == category:
                            cdata["commits"].append(commit)

                    # Category data.
                    if len(cdata["commits"]) > 0:
                        tdata2["categories"].append(cdata)

                # Tags data.
                if len(tdata2["categories"]) > 0:
                    adata["tags"].append(tdata2)

            # Audience data.
            if len(adata["tags"]) > 0:
                context["audiences"].append(adata)

        # Render and write template to file.
        f.write(template.render(context))
