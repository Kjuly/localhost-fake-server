import sys, os

TOKEN		= 'a336c3224230a4b0671d83eb8247491714e5fdf9'

URL_HEADER	= 'https://api.github.com/'
URL_TAIL	= '?access_token=%s' % TOKEN

# ---------------------------------------------------
# USER
# user
if sys.argv[1] == '10' :
	BODY = 'user'

# user/orgs
elif sys.argv[1] == '11' :
	BODY = 'user/orgs'

# users/:user
elif sys.argv[1] == '12' :
	BODY = 'users/%s' % sys.argv[2]

# users/:user/orgs
elif sys.argv[1] == '13' :
	BODY = 'users/%s/orgs' % sys.argv[2]

# user/repos
elif sys.argv[1] == '14' :
	BODY = 'user/repos'

# ---------------------------------------------------
# ORGs
# orgs/:org
elif sys.argv[1] == '20' :
	BODY = 'orgs/%s' % sys.argv[2]

# orgs/:org/members
elif sys.argv[1] == '21' :
	BODY = 'orgs/%s/members' % sys.argv[2]

# orgs/:org/public_members
elif sys.argv[1] == '22' :
	BODY = 'orgs/%s/public_members' % sys.argv[2]

# orgs/:org/members/:user
elif sys.argv[1] == '23' :
	BODY = 'orgs/%s/members/%s' % ( sys.argv[2], sys.argv[3] )

# orgs/:org/teams
elif sys.argv[1] == '24' :
	BODY = 'orgs/%s/teams' % sys.argv[2]

# teams/:id
elif sys.argv[1] == '25' :
	BODY = 'teams/%s' % sys.argv[2]

# teams/:id/members
elif sys.argv[1] == '26' :
	BODY = 'teams/%s/members' % sys.argv[2]

# teams/:id/members/:user
elif sys.argv[1] == '27' :
	BODY = 'teams/%s/members/%s' % ( sys.argv[2], sys.argv[3] )

# teams/:id/repos
elif sys.argv[1] == '28' :
	BODY = 'teams/%s/repos' % sys.argv[2]

# teams/:id/repos/:user/:repo
elif sys.argv[1] == '29' :
	BODY = 'teams/%s/repos/%s/%s' % ( sys.argv[2], sys.argv[3], sys.argv[4] )

# ---------------------------------------------------
# Repos
# users/:user/repos
elif sys.argv[1] == '30' :
	BODY = 'users/%s/repos' % sys.argv[2]

# orgs/:org/repos
elif sys.argv[1] == '31' :
	BODY = 'orgs/%s/repos' % sys.argv[2]

# repos/:user/:repo
elif sys.argv[1] == '32' :
	BODY = 'repos/%s/%s' % ( sys.argv[2], sys.argv[3] )

# repos/:user/:repo/contributors
elif sys.argv[1] == '33' :
	BODY = 'repos/%s/%s/contributors' % ( sys.argv[2], sys.argv[3] )

# repos/:user/:repo/languages
elif sys.argv[1] == '34' :
	BODY = 'repos/%s/%s/languages' % ( sys.argv[2], sys.argv[3] )

# repos/:user/:repo/teams
elif sys.argv[1] == '35' :
	BODY = 'repos/%s/%s/teams' % ( sys.argv[2], sys.argv[3] )

# repos/:user/:repo/tags
elif sys.argv[1] == '36' :
	BODY = 'repos/%s/%s/tags' % ( sys.argv[2], sys.argv[3] )

# repos/:user/:repo/branchs
elif sys.argv[1] == '37' :
	BODY = 'repos/%s/%s/branchs' % ( sys.argv[2], sys.argv[3] )

# repos/:org/:repo/collaborators
# repos/:user/:repo/collaborators
elif sys.argv[1] == '38' :
	BODY = 'repos/%s/%s/collaborators' % ( sys.argv[2], sys.argv[3] )

# repos/:user/:repo/collaborators/:user
elif sys.argv[1] == '39' :
	BODY = 'repos/%s/%s/collaborators/%s' % ( sys.argv[2], sys.argv[3], sys.argv[4] )

# ---------------------------------------------------
# Commits
# repos/:org/:repo/commits
# repos/:user/:repo/commits
elif sys.argv[1] == '41' :
	BODY = 'repos/%s/%s/commits' % ( sys.argv[2], sys.argv[3] )

# repos/:org/:repo/commits/:sha
# repos/:user/:repo/commits/:sha
elif sys.argv[1] == '42' :
	BODY = 'repos/%s/%s/commits/%s' % ( sys.argv[2], sys.argv[3], sys.argv[4] )

# repos/:user/:repo/comments
elif sys.argv[1] == '43' :
	BODY = 'repos/%s/%s/comments' % ( sys.argv[2], sys.argv[3] )

# repos/:user/:repo/comments/:id
elif sys.argv[1] == '44' :
	BODY = 'repos/%s/%s/comments/%s' % ( sys.argv[2], sys.argv[3], sys.argv[4] )

# repos/:user/:repo/commits/:sha/comments
elif sys.argv[1] == '45' :
	BODY = 'repos/%s/%s/commits/%s/comments' % ( sys.argv[2], sys.argv[3], sys.argv[4] )


# ---------------------------------------------------
# CHANGE_SETs

# ---------------------------------------------------
# MESSAGEs

# ---------------------------------------------------
# Process
SAVE	= BODY + '.json'
URL		= '%s%s%s' % ( URL_HEADER, BODY, URL_TAIL )
command = 'curl %s > %s' % ( URL, SAVE )
os.system( command )
