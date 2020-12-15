from instapy import InstaPy
from instapy import smart_run

insta_user = ''
insta_pass = ''

session = InstaPy(
    username=insta_user,
    password=insta_pass,
    headless_browser=False
)

with smart_run(session):
    session.set_smart_hashtags()
    session.follow_by_locations()
    session.set_relationship_bounds(
        enabled=True,
        min_followers=10000,

    )

# with smart_run(session=session):
