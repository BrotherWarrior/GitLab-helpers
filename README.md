# GitLab-helpers

## Introduction

[GitLab](https://www.gitlab.com) provides API for scripting usage but sometimes it does not complete. This 
set of scripts helps to do some things easy or provide functionality that not released
in GitLab

## Scipts

### gitlab-get-release-attachements.py

#### Description

Python extension script for GitLab API to provide fetching release attachemnts
through parsing Markdown description and extract links. GitLab
provides Releases as extensions for Tags. Description of release
may contain files. Inside GitLab attachments released with next steps:

* Uploading file. As a result of call upload method is link to uploaded
file. Name of link is short filename and link is relative link to
file ends with filename.

* Adding Markdown link to description of Release

For using this script you should make rules of filenaming for yourself.

#### Usage

```
$ gitlab-get-release-link.py [-h] --baseurl BASEURL --token TOKEN
                                  --release RELEASE --project PROJECT
                                  --filename FILENAME [--loglevel LOGLEVEL]
```
Arguments description:

`-h, --help`: 
show help message and exit

`--baseurl BASEURL, -b BASEURL`: 
GitLab api base url, f.e. `https://gitlab.example.com/`

`--token TOKEN, -t TOKEN`: 
Security token

`--release RELEASE, -r RELEASE`:
Release name to fetch file

`--project PROJECT, -p PROJECT`:
`Project name` or `id`, f.e. `-p MyProjectGroup/MyProject` or `-p 10`.
If you are using `Project name` you can double quote it (i.e. `"`) (*Warning*, only double quoting works on all platforms)

`--filename FILENAME, -f FILENAME`:
Release attachment filename

`--loglevel LOGLEVEL`:   Loggin level (Optional, default `WARNING`)

#### Known TODO's

* Support mask (like file-release-v*.bin) for release filenaming
* Markdown parsing is not strictly, use Python's Markdow for extracting links
