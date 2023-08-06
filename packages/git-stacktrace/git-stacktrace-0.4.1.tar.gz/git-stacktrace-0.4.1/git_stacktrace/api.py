"""
python API to call git stacktrace.


Example usage:
    from git_stacktrace import api

    traceback = api.Traceback(traceback_string)
    git_range = api.convert_since('1.day')
    results = api.lookup_stacktrace(traceback, git_range, fast=False)
    for r in results.get_sorted_results():
        print ""
        print r
"""


from git_stacktrace import git
from git_stacktrace import result
from git_stacktrace import parse_trace


# So we can call api.Traceback
Traceback = parse_trace.Traceback


def _longest_filename(matches):
    """find longest match by number of '/'."""
    return max(matches, key=lambda filename: len(filename.split('/')))


def _lookup_files(commit_files, git_files, traceback, results):
    """Populate results and line.git_filename."""
    for line in traceback.lines:
        matches = [f for f in git_files if line.trace_filename.endswith(f)]
        if matches:
            git_file = _longest_filename([f for f in git_files if line.trace_filename.endswith(f)])
            for commit, file_list in commit_files.iteritems():
                if git_file in file_list:
                    line.git_filename = git_file
                    results.get_result(commit).files.add(git_file)
            if line.git_filename is None:
                line.git_filename = _longest_filename(matches)


def convert_since(since, path=None):
    """Convert the git since format into a git range

    since -- git formatted since value such as '1,day'
    path -- git path, such as 'origin/master'
    """
    return git.convert_since(since, path=path)


def valid_range(git_range):
    """Make sure there are commits in the range

    Generate a dictionary of files modified by the commits in range
    """
    return git.valid_range(git_range)


def lookup_stacktrace(traceback, git_range, fast):
    """Lookup to see what commits in git_range could have caused the stacktrace.

    If fast is True, don't run pickaxe if cannot find the file in git.

    Pass in a stacktrace object and returns a results object."""
    results = result.Results()

    commit_files = git.files_touched(git_range)
    git_files = git.files(git_range)
    _lookup_files(commit_files, git_files, traceback, results)

    for line in traceback.lines:
        commits = []
        if not (line.git_filename is None and fast is True):
            try:
                commits = git.pickaxe(line.code, git_range, line.git_filename)
            except Exception:
                # If this fails, move on
                continue
        for commit, line_removed in commits:
            if line_removed:
                results.get_result(commit).lines_removed.add(line.code)
            else:
                results.get_result(commit).lines_added.add(line.code)
    return results
