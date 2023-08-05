

from .util import urljoin, clean


class Model:
    __mapping__ = {
        'Activity': 'activities',
        'ActivityType': 'activityTypes',
        'Authorization': 'authorizations',
        'Currency': 'currencies',
        'Deal': 'deals',
        'File': 'files',
        'Filter': 'filters',
        'Note': 'notes',
        'Organization': 'organizations',
        'Person': 'persons',
        'Pipeline': 'pipelines',
        'Product': 'products',
        'SearchResult': 'searchResults',
        'Stage': 'stages',
        'User': 'users',
        'ActivityField': 'activityFields',
        'DealField': 'dealFields',
        'OrganizationField': 'organizationFields',
        'PersonField': 'personFields',
        'ProductField': 'productFields',
    }

    def __init__(self, name, client, custom_fields=None):
        """Model Manager

        This class manages the different models available on Pipedrive.

        Arguments:
            name {str} -- name of an Pipedrive object, e.g. "Organization"
            client {client.Client} -- instance of Client object

        Keyword Arguments:
            custom_fields {dict} -- {key: ModelField()} (default: {None})

        Raises:
            TypeError -- When argument 'name' not a valid model name
        """
        self.__name__ = name
        self.__custom_fields__ = custom_fields or {}
        try:
            self.__path__ = self.__mapping__[name]
        except KeyError:
            raise TypeError('Model {} does not exist'.format(name))
        self.client = client
        self.__attributes__ = {}

    def __call__(self, **data):
        """Shortcut to update method

        This is a shortcut to Model.update.

        Arguments:
            **data {dict} -- {attribute_name: value}

        Returns:
            Model -- updated self
        """
        return self.update(**data)

    def __getattr__(self, name):
        name = self.get_field_key(name)
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name not in ('client', ) and not name.startswith('__'):
            name = self.get_field_key(name)
            self.__attributes__[name] = value
        super().__setattr__(name, value)

    def __repr__(self):
        attributes = [
            '{}={}'.format(key, value)
            for key, value in self.__attributes__.items()
        ]
        values = '; '.join(attributes)
        return '<{name}({values})>'.format(name=self.__name__, values=values)

    def get_field_key(self, name):
        """Translate field key

        Translates the field key from how it is in the database to a human
        readable one.

        Arguments:
            name {str} -- field key

        Returns:
            str -- cleaned field key
        """
        fields = super().__getattribute__('__custom_fields__')
        for key, field in fields.items():
            if clean(field.name) == name:
                break
        else:
            key = None
        return key or name

    def update(self, **data):
        """Update own data

        Updates own data with the data given

        Arguments:
            **data {dict} -- {attribute_name: value}

        Returns:
            Model -- updated self
        """
        for key, value in data.items():
            key = self.get_field_key(key)
            try:
                options = self.__custom_fields__[key].options
            except (AttributeError, KeyError):
                pass
            else:
                options = {int(o['id']): o['label'] for o in options}
                try:
                    value = options[int(value)]
                except (ValueError, TypeError):
                    pass
            setattr(self, key, value)
        return self

    def fetch_raw(self, filter_id=None, start=0, limit=50, sort=None):
        """Fetch raw data

        Fetches raw object data in a dictionary format.
        It filters the results based on set attributes on this object.

        Keyword Arguments:
            filter_id {int} -- see: Filters (default: {None})
            start {int} -- id to start at (default: {0})
            limit {int} -- max of items to fetch (default: {50})
            sort {str} -- extra sorting string (default: {None})

        Returns:
            dict -- raw data

        Raises:
            ConnectionError -- When some error has occured while connecting
        """
        params = {'start': start, 'limit': limit}
        if filter_id:
            params.update({'filter_id': filter_id})
        if sort:
            params.update({'sort': sort})

        response = self.client.request(
            method='GET',
            path=self.__path__,
            params=params,
        )
        if 'error' in response:
            raise ConnectionError(response['error'] + response['error_info'])
        if not self.__attributes__:
            return response
        attrs = self.__attributes__.items()
        objects = response['data']
        data = []
        objects = list(objects)
        for obj in objects:
            items = obj.items()
            if all(item in items for item in attrs):
                data.append(obj)
        response['data'] = data
        return response

    def fetch(self, filter_id=None, start=0, limit=50, sort=None):
        """Fetch models

        Fetches models.
        It filters the results based on set attributes on this object.

        Keyword Arguments:
            filter_id {int} -- see: Filters (default: {None})
            start {int} -- id to start at (default: {0})
            limit {int} -- max of items to fetch (default: {50})
            sort {str} -- extra sorting string (default: {None})

        Yields:
            Model -- model that corresponds to filters and set attributes
        """
        response = self.fetch_raw(filter_id, start, limit, sort)
        objects = response['data']
        if not objects:
            return []
        for data in objects:
            yield getattr(self.client, self.__name__)(**data)

    def fetch_all(self, filter_id=None, start=0):
        """Fetch all models

        Fetches all models.
        It filters the results based on set attributes on this object.

        Keyword Arguments:
            filter_id {int} -- see: Filters (default: {None})
            start {int} -- id to start at (default: {0})

        Yields:
            Model -- model that corresponds to filters and set attributes
        """
        current = start
        run = True
        while run:
            response = self.fetch_raw(filter_id, current, 50)
            pagination = response['additional_data']['pagination']
            if pagination['more_items_in_collection']:
                current += 50
            else:
                run = False
            for data in response['data'] or []:
                yield getattr(self.client, self.__name__)(**data)

    def complete(self):
        """Complete self

        Tries to complete itself based on set attributes.

        Returns:
            Model -- self

        Raises:
            ValueError -- When set attributes are not precise enough to
                          match exactly one object
        """
        models = list(self.fetch(limit=2))
        if len(models) > 1:
            raise ValueError(
                'Model is too ambiguous to complete, got too many results'
            )
        else:
            model = models[0]
        return model

    def save(self):
        """Add/Update on REST

        Sends current data to the Pipedrive REST API to be added.
        If the current model has an id, then it will be updated instead.

        Returns:
            Model -- self
        """
        if 'id' in self.__attributes__ and self.id is not None:
            method = 'POST'
            path = self.__path__
        else:
            method = 'PUT'
            path = urljoin(self.__path__, str(self.id))
        self.client.request(
            method=method,
            path=path,
            params=self.__attributes__,
        )
        return self

    def remove(self):
        """Remove on REST

        Marks the current model as removed in the Pipedrive REST API.

        Returns:
            Model -- self

        Raises:
            AttributeError -- When id is not set
        """
        try:
            id = self.id
        except AttributeError:
            raise AttributeError('Requires the attribute "id" to be set')
        self.client.request(
            method='DELETE',
            path=urljoin(self.__path__, str(id)),
        )
        return self

    def merge(self, with_id):
        """Merge on REST

        Merges the current model with another one in the Pipedrive REST API.

        Arguments:
            with_id {int} -- id of object to merge with

        Returns:
            Model -- self

        Raises:
            AttributeError -- When id is not set
        """
        try:
            id = self.id
        except AttributeError:
            raise AttributeError('Requires the attribute "id" to be set')
        self.client.request(
            method='PUT',
            path=urljoin(self.__path__, str(id), 'merge'),
            params={'merge_with_id': with_id},
        )
        return self
