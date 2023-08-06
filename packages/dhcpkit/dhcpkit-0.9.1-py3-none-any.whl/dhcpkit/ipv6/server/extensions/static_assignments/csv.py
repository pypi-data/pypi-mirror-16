"""
An option handler that assigns addresses based on DUID from a CSV file
"""
import codecs
import csv
import logging
from ipaddress import IPv6Address, IPv6Network

from typing import Mapping, List, Tuple

from dhcpkit.ipv6.duids import DUID
from dhcpkit.ipv6.extensions.remote_id import RemoteIdOption
from dhcpkit.ipv6.options import ClientIdOption, InterfaceIdOption
from dhcpkit.ipv6.server.extensions.static_assignments import StaticAssignmentHandler, Assignment
from dhcpkit.ipv6.server.transaction_bundle import TransactionBundle
from dhcpkit.utils import normalise_hex

logger = logging.getLogger(__name__)


class CSVStaticAssignmentHandler(StaticAssignmentHandler):
    """
    Assign addresses and/or prefixes based on the contents of a CSV file
    """

    def __init__(self, filename: str,
                 address_preferred_lifetime: int, address_valid_lifetime: int,
                 prefix_preferred_lifetime: int, prefix_valid_lifetime: int):
        """
        Initialise the mapping. This handler will respond to clients on responsible_for_links and assume that all
        addresses in the mapping are appropriate for on those links.

        :param filename: The filename containing the CSV data
        """
        super().__init__(address_preferred_lifetime, address_valid_lifetime,
                         prefix_preferred_lifetime, prefix_valid_lifetime)

        self.filename = filename
        self.mapping = self.read_csv_file(filename)

    def __str__(self):
        return "{} from {}".format(self.__class__.__name__, self.filename)

    def get_assignment(self, bundle: TransactionBundle) -> Assignment:
        """
        Look up the assignment based on DUID, Interface-ID of the relay closest to the client and Remote-ID of the
        relay closest to the client, in that order.

        :param bundle: The transaction bundle
        :return: The assignment, if any
        """
        # Look up based on DUID
        duid_option = bundle.request.get_option_of_type(ClientIdOption)
        duid = 'duid:' + codecs.encode(duid_option.duid.save(), 'hex').decode('ascii')
        if duid in self.mapping:
            return self.mapping[duid]

        # Look up based on Interface-ID
        interface_id_option = bundle.incoming_relay_messages[0].get_option_of_type(InterfaceIdOption)
        if interface_id_option:
            interface_id = 'interface-id:' + codecs.encode(interface_id_option.interface_id, 'hex').decode('ascii')
            if interface_id in self.mapping:
                return self.mapping[interface_id]

        # Look up based on Remote-ID
        remote_id_option = bundle.incoming_relay_messages[0].get_option_of_type(RemoteIdOption)
        if remote_id_option:
            remote_id = 'remote-id:{}:{}'.format(remote_id_option.enterprise_number,
                                                 codecs.encode(remote_id_option.remote_id, 'hex').decode('ascii'))
            if remote_id in self.mapping:
                return self.mapping[remote_id]

        # Nothing found
        return Assignment(address=None, prefix=None)

    def read_csv_file(self, csv_filename: str) -> Mapping[str, Assignment]:
        """
        Read the assignments from the file specified in the configuration

        :param csv_filename: The filename of the CSV file
        :return: A dictionary mapping identifiers to assignments
        """
        assignments = dict(self.parse_csv_file(csv_filename))
        logger.info("Loaded {} assignments from {}".format(len(assignments), csv_filename))
        return assignments

    @staticmethod
    def parse_csv_file(csv_filename: str) -> List[Tuple[str, Assignment]]:
        """
        Read the assignments from the file specified in the configuration

        :param csv_filename: The filename of the CSV file
        :return: An list of identifiers and their assignment
        """

        logger.debug("Loading assignments from {}".format(csv_filename))

        with open(csv_filename) as csv_file:
            # Auto-detect the CSV dialect
            sniffer = csv.Sniffer()
            sample = csv_file.read(10240)
            dialect = sniffer.sniff(sample)

            # Restart and parse
            csv_file.seek(0)
            reader = csv.DictReader(csv_file, dialect=dialect)

            # First line is column headings
            for row in reader:
                try:
                    address_str = row['address'].strip()
                    address = address_str and IPv6Address(address_str) or None

                    prefix_str = row['prefix'].strip()
                    prefix = prefix_str and IPv6Network(prefix_str) or None

                    # Validate and normalise id input
                    row_id = row['id']

                    if row_id.startswith('duid:'):
                        duid_hex = row_id.split(':', 1)[1]
                        duid_bytes = codecs.decode(duid_hex, 'hex')
                        length, duid = DUID.parse(duid_bytes, length=len(duid_bytes))
                        duid_hex = codecs.encode(duid.save(), 'hex').decode('ascii')
                        row_id = 'duid:{}'.format(duid_hex)

                    elif row_id.startswith('interface-id:'):
                        interface_id_hex = row_id.split(':', 1)[1]
                        interface_id_hex = normalise_hex(interface_id_hex)
                        interface_id = codecs.decode(interface_id_hex, 'hex')
                        interface_id_hex = codecs.encode(interface_id, 'hex').decode('ascii')
                        row_id = 'interface_id:{}'.format(interface_id_hex)

                    elif row_id.startswith('interface-id-str:'):
                        interface_id = row_id.split(':', 1)[1]
                        interface_id_hex = codecs.encode(interface_id.encode('ascii'), 'hex').decode('ascii')
                        row_id = 'interface_id:{}'.format(interface_id_hex)

                    elif row_id.startswith('remote-id:') or row_id.startswith('remote-id-str:'):
                        remote_id_data = row_id.split(':', 1)[1]
                        try:
                            enterprise_id, remote_id = remote_id_data.split(':', 1)
                            enterprise_id = int(enterprise_id)
                            if row_id.startswith('remote-id:'):
                                remote_id = normalise_hex(remote_id)
                                remote_id = codecs.decode(remote_id, 'hex')
                            else:
                                remote_id = remote_id.encode('ascii')

                            row_id = 'remote-id:{}:{}'.format(enterprise_id,
                                                              codecs.encode(remote_id, 'hex').decode('ascii'))
                        except ValueError:
                            raise ValueError("Remote-ID must be formatted as 'remote-id:<enterprise>:<remote-id-hex>', "
                                             "for example: 'remote-id:9:0123456789abcdef")

                    else:
                        raise ValueError("The id must start with duid: or interface-id: followed by a hex-encoded "
                                         "value, interface-id-str: followed by an ascii string, remote-id: followed by "
                                         "an enterprise-id, a colon and a hex-encoded value or remote-id-str: followed"
                                         "by an enterprise-id, a colon and an ascii string")

                    # Store the normalised id
                    logger.debug("Loaded assignment for {}".format(row_id))
                    yield row_id, Assignment(address=address, prefix=prefix)

                except KeyError:
                    raise ValueError("Assignment CSV must have columns 'id', 'address' and 'prefix'")
                except ValueError as e:
                    logger.error("Ignoring {} line {} with invalid value: {}".format(csv_file, reader.line_num, e))
