#!/usr/bin/python
# vim: set fileencoding=utf-8 :

# For Local Testing
LOCAL_TEST	= True
LOCAL_PORT	= '8100'
LOCAL_URL	= 'http://localhost:%s' % LOCAL_PORT

# OAuth
oauth_settings = {
		'client_id'		: '37b8c0cb93f5dbae87db',						# Client ID
		'client_secret' : '9e033e9718e8ffdcc88eb32dab8889926b5927d6',	# Client Secret
		'base_url'		: 'https://github.com/login/oauth/authorize',	# Github OAuth URL
		'redirect_url'	: 'http://localhost:8080/oauth_redirect',		# Local host test URL
		#'redirect_url'	: 'http://dev-stats.appspot.com/oauth_redirect',# GAE URL
		'scope'			: 'user,repo'									# Scopes to request
		}

# Date Range
date_range_by = {
		'dr_day' : 1,
		'dr_wek' : 7,	# +++++++++++++++++++++++ 以日起整周算还是从当天到上周
		'dr_mon' : 30	# +++++++++++++++++++++++ 月有不同天数
		}

# Data Type
DATA_TYPE = {
		'GC' : 11,	# Github Commit
		'GCL': 12,	# Github Commit Change Line
		'LT' : 21,	# Lighthouse Ticket
		'LTC': 22	# Lighthouse Ticket Comment
		}

# URL for Github data fetching
URL_GITHUB_HEADER = 'https://api.github.com/'
URL_GITHUB = {
		'OAuth_request'			: "https://github.com/login/oauth/authorize?client_id=%s&redirect_uri=%s&scope=%s",
		'OAuth_authorization'	: "https://github.com/login/oauth/access_token?client_id=%s&redirect_uri=%s&client_secret=%s&code=%s",
		'User'					: URL_GITHUB_HEADER + "user?access_token=%s",
		'User_Orgs'				: URL_GITHUB_HEADER + "user/orgs?access_token=%s",
		'Org_Repos'				: URL_GITHUB_HEADER + "orgs/%s/repos?access_token=%s",
		'Org_Repo_Collaborators': URL_GITHUB_HEADER + "repos/%s/%s/collaborators?access_token=%s",
		'Org_Members'			: URL_GITHUB_HEADER + "orgs/%s/members?access_token=%s",
		'Commits'				: URL_GITHUB_HEADER + "repos/%s/%s/commits?access_token=%s"
		}

# --------------------------------------------------------------------------
