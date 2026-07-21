class MediaCache:

    _cache = {}

    @classmethod
    def save(cls, message_id: int, media):
        cls._cache[message_id] = media

    @classmethod
    def get(cls, message_id: int):
        return cls._cache.get(message_id)

    @classmethod
    def delete(cls, message_id: int):
        cls._cache.pop(message_id, None)