"""
keys
"""
VANILLA_ISSUE_STRING = "[{2}] <a href='http://vendasta.jira.com/browse/{0}'>{0}</a> " \
                         "{1} - {3}<br>"
COLOURFUL_ISSUE_STRING = "[<span class='{4}'>{2}</span>] <a href='http://vendasta.jira.com/browse/{0}'>{0}</a> " \
                         "{1} - {3}<br>"


class JIRA_TABLE_KEYS(object):
    """
    Keys that identify columns in the Jira column return
    """

    KEY = "Key"
    SUMMARY = "Summary"
    ISSUE_TYPE = "Issue Type"
    PRIORITY = "Priority"
    STATUS = "Status"

    ALL = [KEY, SUMMARY, ISSUE_TYPE, PRIORITY, STATUS]


class JIRA_ISSUE_TYPES(object):
    """
    Keys that identify issue types in Jira
    """

    STORY = "Story"
    TECHNICAL_DEBT = "Technical Debt"
    BUG = "Bug"
    IMPROVEMENT = "Improvement"
    SPIKE = "Spike"
    INJECTED = "Injected"
    EPIC = "Epic"


class FORMAT_KEYS(object):
    """
    Different formats that can be provided by the user
    """

    VANILLA = "vanilla"
    COLOURFUL = "colourful"