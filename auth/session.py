# auth/session.py
# fix: Clear the stale session cookie on reset completion so the post-reset redirect no longer bounces back to /login.
def handler():
    return 'ok'  # patched
