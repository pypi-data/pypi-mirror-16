from __future__ import unicode_literals


class IP_address(object):
    """
    Object representation of the IP-address.

    Attributes:
    access -- "public" or "private"
    address -- the actual IP_address (string)
    ptr_record -- the reverse DNS name (string)
    server -- the UUID of the server this IP is attached to (string)

    The only updateable field is the ptr_record.
    ptr_record and server are present only if /server/uuid endpoint was used.
    """

    def __init__(self, access, cloud_manager, address=None, family='IPv4',
                 ptr_record=None, server=None, *args, **kwargs):
        """
        Initialize IP address with at least access and address.

        ptr_record and server not returned by the API in every case (e.g. when IP is nested).
        Only ptr_record is editable due to restrictions of the API.
        """
        self._cloud_manager = cloud_manager
        self.__reset(access, address, family, ptr_record, server)

    def __reset(self, access, address, family='IPv4', ptr_record=None, server=None):
        """
        Reset after repopulating from API.
        """
        # Always present
        self._access = access
        self._address = address
        self._family = family

        # Present when not populated from /server/uuid endpoint
        self._server_uuid = server
        self.ptr = ptr_record

    def save(self):
        """
        IP_address can only change its PTR record. Saves the current state, PUT /ip_address/uuid.
        """
        body = {'ip_address': {'ptr_record': self.ptr}}
        data = self._cloud_manager.request('PUT', '/ip_address/' + self.address, body)
        self.__reset(**data['ip_address'])

    def destroy(self):
        """
        Release the IP_address. DELETE /ip_address/uuid.
        """
        self._cloud_manager.release_IP(self.address)

    def __str__(self):  # noqa
        return 'IP-address: ' + self.address

    @property
    def address(self):  # noqa
        return self._address

    @property
    def access(self):  # noqa
        return self._access

    @property
    def server_uuid(self):  # noqa
        return self._server_uuid

    @property
    def family(self):  # noqa
        return self._family

    @staticmethod
    def _create_ip_address_objs(ip_addresses, cloud_manager):

        # ip-addresses might be provided as a flat array or as a following dict:
        # {'ip_addresses': {'ip_address': [...]}} || {'ip_address': [...]}

        if 'ip_addresses' in ip_addresses:
            ip_addresses = ip_addresses['ip_addresses']

        if 'ip_address' in ip_addresses:
            ip_addresses = ip_addresses['ip_address']

        ip_address_objs = list()
        for ip_addr in ip_addresses:
            ip_address_objs.append(IP_address(cloud_manager=cloud_manager, **ip_addr))
        return ip_address_objs
