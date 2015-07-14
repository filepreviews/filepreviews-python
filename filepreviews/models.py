import json


class PreviewResult(dict):
    def __init__(self, response):
        super(PreviewResult, self).__init__(response)
        self.__dict__ = response

    def __repr__(self):
        return '<PreviewResult at {id}> JSON: {json}'.format(
            id=id(self),
            json=str(self)
        )

    def __str__(self):
        return json.dumps(self, sort_keys=True, indent=2)

    @property
    def preview_url(self):
        return self.preview.get('url')
