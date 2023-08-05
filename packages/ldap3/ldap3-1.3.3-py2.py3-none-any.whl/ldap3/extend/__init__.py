"""
"""

# Created on 2014.04.28
#
# Author: Giovanni Cannata
#
# Copyright 2015 Giovanni Cannata
#
# This file is part of ldap3.
#
# ldap3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ldap3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ldap3 in the COPYING and COPYING.LESSER files.
# If not, see <http://www.gnu.org/licenses/>.

from os import linesep

from .. import SUBTREE, DEREF_ALWAYS, ALL_ATTRIBUTES
from .microsoft.dirSync import DirSync
from .microsoft.modifyPassword import modify_ad_password
from .novell.partition_entry_count import PartitionEntryCount
from .novell.replicaInfo import ReplicaInfo
from .novell.listReplicas import ListReplicas
from .novell.getBindDn import GetBindDn
from .novell.nmasGetUniversalPassword import NmasGetUniversalPassword
from .novell.nmasSetUniversalPassword import NmasSetUniversalPassword
from .novell.startTransaction import StartTransaction
from .novell.endTransaction import EndTransaction
from .novell.addMembersToGroups import add_members_to_groups
from .novell.removeMembersFromGroups import remove_members_from_groups
from .novell.checkGroupsMemberships import check_groups_memberships
from .standard.whoAmI import WhoAmI
from .standard.modifyPassword import ModifyPassword
from .standard.PagedSearch import paged_search_generator, paged_search_accumulator


class ExtendedOperationContainer(object):
    def __init__(self, connection):
        self._connection = connection

    def __repr__(self):
        return linesep.join(['  ' + element for element in dir(self) if element[0] != '_'])

    def __str__(self):
        return self.__repr__()


class StandardExtendedOperations(ExtendedOperationContainer):
    def who_am_i(self, controls=None):
        return WhoAmI(self._connection,
                      controls).send()

    def modify_password(self,
                        user=None,
                        old_password=None,
                        new_password=None,
                        hash_algorithm=None,
                        salt=None,
                        controls=None):

        return ModifyPassword(self._connection,
                              user,
                              old_password,
                              new_password,
                              hash_algorithm,
                              salt,
                              controls).send()

    def paged_search(self,
                     search_base,
                     search_filter,
                     search_scope=SUBTREE,
                     dereference_aliases=DEREF_ALWAYS,
                     attributes=None,
                     size_limit=0,
                     time_limit=0,
                     types_only=False,
                     get_operational_attributes=False,
                     controls=None,
                     paged_size=100,
                     paged_criticality=False,
                     generator=True):

        if generator:
            return paged_search_generator(self._connection,
                                          search_base,
                                          search_filter,
                                          search_scope,
                                          dereference_aliases,
                                          attributes,
                                          size_limit,
                                          time_limit,
                                          types_only,
                                          get_operational_attributes,
                                          controls,
                                          paged_size,
                                          paged_criticality)
        else:
            return paged_search_accumulator(self._connection,
                                            search_base,
                                            search_filter,
                                            search_scope,
                                            dereference_aliases,
                                            attributes,
                                            size_limit,
                                            time_limit,
                                            types_only,
                                            get_operational_attributes,
                                            controls,
                                            paged_size,
                                            paged_criticality)


class NovellExtendedOperations(ExtendedOperationContainer):
    def get_bind_dn(self, controls=None):
        return GetBindDn(self._connection,
                         controls).send()

    def get_universal_password(self, user, controls=None):
        return NmasGetUniversalPassword(self._connection,
                                        user,
                                        controls).send()

    def set_universal_password(self, user, new_password=None, controls=None):
        return NmasSetUniversalPassword(self._connection,
                                        user,
                                        new_password,
                                        controls).send()

    def list_replicas(self, server_dn, controls=None):
        return ListReplicas(self._connection,
                            server_dn,
                            controls).send()

    def partition_entry_count(self, partition_dn, controls=None):
        return PartitionEntryCount(self._connection,
                                   partition_dn,
                                   controls).send()

    def replica_info(self, server_dn, partition_dn, controls=None):
        return ReplicaInfo(self._connection,
                           server_dn,
                           partition_dn,
                           controls).send()

    def start_transaction(self, controls=None):
        return StartTransaction(self._connection,
                                controls).send()

    def end_transaction(self, commit=True, controls=None):  # attach the groupingControl to commit, None to abort transaction
        return EndTransaction(self._connection,
                              commit,
                              controls).send()

    def add_members_to_groups(self, members, groups, fix=True, transaction=True):
        return add_members_to_groups(self._connection,
                                     members_dn=members,
                                     groups_dn=groups,
                                     fix=fix,
                                     transaction=transaction)

    def remove_members_from_groups(self, members, groups, fix=True, transaction=True):
        return remove_members_from_groups(self._connection,
                                          members_dn=members,
                                          groups_dn=groups,
                                          fix=fix,
                                          transaction=transaction)

    def check_groups_memberships(self, members, groups, fix=False, transaction=True):
        return check_groups_memberships(self._connection,
                                        members_dn=members,
                                        groups_dn=groups,
                                        fix=fix,
                                        transaction=transaction)


class MicrosoftExtendedOperations(ExtendedOperationContainer):
    def dir_sync(self,
                 sync_base,
                 sync_filter='(objectclass=*)',
                 attributes=ALL_ATTRIBUTES,
                 cookie=None,
                 object_security=False,
                 ancestors_first=True,
                 public_data_only=False,
                 incremental_values=True,
                 max_length=2147483647,
                 hex_guid=False):
        return DirSync(self._connection,
                       sync_base=sync_base,
                       sync_filter=sync_filter,
                       attributes=attributes,
                       cookie=cookie,
                       object_security=object_security,
                       ancestors_first=ancestors_first,
                       public_data_only=public_data_only,
                       incremental_values=incremental_values,
                       max_length=max_length,
                       hex_guid=hex_guid)

    def modify_password(self, user, new_password, old_password=None, controls=None):
        return modify_ad_password(self._connection,
                                  user,
                                  old_password,
                                  new_password,
                                  controls)


class ExtendedOperationsRoot(ExtendedOperationContainer):
    def __init__(self, connection):
        ExtendedOperationContainer.__init__(self, connection)  # calls super
        self.standard = StandardExtendedOperations(self._connection)
        self.novell = NovellExtendedOperations(self._connection)
        self.microsoft = MicrosoftExtendedOperations(self._connection)
