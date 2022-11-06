from user_profile.models import UserProfile
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

@registry.register_document
class UserProfileDocument(Document):
    class Index:
        name = 'user_profile'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = UserProfile
        fields = [
            'email',
            'first_name',
            'organization_name',
            'phone',
        ]

