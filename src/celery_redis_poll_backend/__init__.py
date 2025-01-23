__version__ = "0.1.7"

from celery_redis_poll_backend.backend import (
    PollingRedisBackend,
    PollingRedisClusterBackend,
)


def install_redis_poll_backend():
    """Explicitly install.  Useful for local unit tests."""
    from celery.app.backends import BACKEND_ALIASES

    BACKEND_ALIASES["redis"] = "celery_redis_poll.backend:choose_redis_backend"
    BACKEND_ALIASES["rediss"] = "celery_redis_poll.backend:choose_rediss_backend"


__all__ = ["PollingRedisBackend", "PollingRedisClusterBackend"]
