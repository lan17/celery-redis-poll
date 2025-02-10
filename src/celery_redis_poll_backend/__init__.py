__version__ = "0.1.8"

from celery_redis_poll_backend.backend import (
    PollingRedisBackend,
    PollingRedisClusterBackend,
)


__all__ = ["PollingRedisBackend", "PollingRedisClusterBackend"]
