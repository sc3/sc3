# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "sc3"

# Descriptive title of project
TITLE = "Supreme Chi-Town Coding Crew"

# Google spreadsheet key
SPREADSHEET_KEY = "0ArYYFwYApHDkdEZrMHBGVGlHZkdMblhKSFpvaG9lREE"

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
#S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    # "mytarget": "s3://mys3url.bucket.url/some/path"
#}

# Repository this project is based on (used for updates)
TEMPLATE_REPO_URL = "https://github.com/wilbertom/tarbell-template"

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'sc3',
    'title': 'Supreme Chi-Town Coding Crew'
}

