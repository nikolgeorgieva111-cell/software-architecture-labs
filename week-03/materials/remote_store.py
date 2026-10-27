
"""MaterialStore backed by the faculty file server (HTTP)."""

import urllib.error
from urllib.parse import quote

import http_util
from materials.store import MaterialsUnavailable, MaterialNotFound


class RemoteMaterialStore:
    def __init__(self, base_url, timeout=2.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _call(self, operation, *args):
        try:
            return operation(*args, timeout=self.timeout)

        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise MaterialNotFound("Material not found") from e
            raise MaterialsUnavailable("Server unavailable") from e

        except (urllib.error.URLError, TimeoutError, OSError) as e:
            raise MaterialsUnavailable("Server unavailable") from e

    def list(self, course_id):
        url = f"{self.base_url}/courses/{course_id}/materials"
        result = self._call(http_util.get_json, url)
        return result["files"]

    def read(self, course_id, name):
        safe_name = quote(name, safe="")
        url = f"{self.base_url}/courses/{course_id}/materials/{safe_name}"
        return self._call(http_util.get_bytes, url)

    def write(self, course_id, name, data):
        safe_name = quote(name, safe="")
        url = f"{self.base_url}/courses/{course_id}/materials/{safe_name}"
        self._call(http_util.put_bytes, url, data)
