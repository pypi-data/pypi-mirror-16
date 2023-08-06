from datetime import datetime

class DevpiObject(object):
    """ Client response object """
    path = None
    _client = None

    def _get(self, path):
        return self._client.get_json(path)

    def __str__(self):
        return self.path

class Index(DevpiObject):
    """ Represents a remote devpi index """

    def __init__(self, client, path, config):
        self._client = client
        self.path = path
        self.config = config
        _, self.user, self.name = path.split('/')

    def project(self, name):
        return Project(self._client, '%s/%s' % (self.path, name))

    def projects(self):
        return list(self.iter_projects())

    def iter_projects(self):
        res = self._get(self.path)
        for p in res['projects']:
            yield Project(self._client, '%s/%s' % (self.path, p))

    def __repr__(self):
        return '<devpitools.Index %s>' % self.path

class Project(DevpiObject):
    """ Represents a remote devpi project """

    def __init__(self, client, path):
        self._client = client
        self.path = path

    def latest_version(self):
        """ Return latest project version based on upload time """
        return sorted(self.versions(), key=lambda x: x.uploaded)[-1]

    def version(self, version):
        path = '%s/%s' % (self.path, version)
        return Version(path, self._get(path))

    def versions(self):
        return list(self.iter_versions())

    def iter_versions(self):
        for vmeta in self._get(self.path).values():
            path = '%s/%s' % (self.path, vmeta['version'])
            yield Version(path, vmeta)

    def __repr__(self):
        return '<devpitools.Project %s>' % self.path

class Version(DevpiObject):
    """ Represents a dist of a remote devpi project """

    def __init__(self, path, meta):
        self.path = path
        self.links = self._read_links(meta.pop('+links'))
        self.uploaded = sorted([ l.uploaded for l in self.links ])[0]
        for k,v in meta.items():
            self.__setattr__(k,v)

    def _read_links(self, links):
        return [ Link(self.path, l) for l in links ]

    def __repr__(self):
        return '<devpitools.Version %s>' % self.path

class Link(DevpiObject):
    """ Represents links associated with a remote devpi project """

    uploaded = datetime.fromtimestamp(0)

    def __init__(self, path, meta):
        self.path = path
        self.log = self._read_log(meta.pop('log'))
        for k,v in meta.items():
            self.__setattr__(k,v)

    def _read_log(self, log):
        """ read log timestamp into datetime obj """
        for l in log:
            year, month, date, hour, minute, second = l['when']
            l['when'] = datetime(year, month, date, hour, minute, second)
            if l['what'] == 'upload':
                self.uploaded = l['when']
        return log

    def __repr__(self):
        return '<devpitools.Link %s>' % self.path
