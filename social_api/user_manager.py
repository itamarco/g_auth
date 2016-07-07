from .models import User


def is_exist(email):
    return User.objects.filter(email=email).count() == 1


def get_or_create(google_info):
    return User.objects.get_or_create(
        first_name=google_info['given_name'],
        last_name=google_info['family_name'],
        email=google_info['email'],
        token=google_info['id']+google_info['email'],
    )






#
# updates = {                                    # Our parsed JSON data
#     'pk': 1337,
#     'foo': 'bar',
#     'baz': 192.05
# }
#
# id = updates.pop('pk')                         # Extract the instance's ID
# Foo.objects.filter(id=id).update(**updates)    # Update the instance's data