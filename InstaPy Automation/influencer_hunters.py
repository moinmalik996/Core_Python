from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''
insta_password = ''


target_business_categories = ['food', 'kitchen', 'pets']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  disable_image_load=True,
                  multi_logs=True)

# let's go! :>
with smart_run(session):

    # general settings
    session.set_simulation(enabled=True)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    min_followers=5000,
                                    min_posts=100)

    session.set_skip_users(skip_private=True,
                           skip_no_profile_pic=True,
                           skip_business=True,
                           dont_skip_business_categories=[target_business_categories])

    # session.set_user_interact(amount=3, randomize=True, percentage=80,
    #                           media='Photo')
    # session.set_do_like(enabled=True, percentage=90)
    # session.set_do_comment(enabled=True, percentage=15)
    # session.set_comments(comments, media='Photo')
    session.set_do_follow(enabled=True, percentage=80, times=1)

