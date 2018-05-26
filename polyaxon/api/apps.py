from django.apps import AppConfig
from django.conf import settings


class APIConfig(AppConfig):
    name = 'api'
    verbose_name = 'API'

    def ready(self):
        import signals.experiments  # noqa
        import signals.experiment_groups  # noqa
        import signals.projects  # noqa
        import signals.project_plugin_jobs  # noqa
        import signals.nodes  # noqa
        import signals.repos  # noqa
        from signals.users import create_auth_token  # noqa
        import signals.pipelines  # noqa
        if settings.AUTH_LDAP_ENABLED:
            from api.users.ldap_signals import populate_user_handler  # noqa
