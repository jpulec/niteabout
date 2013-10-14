from storages.backends.s3boto import S3BotoStorage

class MyBoto(S3BotoStorage):
    location = 'static'

    def url(self, name):
        url = super(MyBoto, self).url(name)
        if name.endswith('/') and not url.endswith('/'):
            url += '/'
        return url
