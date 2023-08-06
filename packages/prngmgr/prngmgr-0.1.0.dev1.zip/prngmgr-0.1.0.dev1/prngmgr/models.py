from django.db import models
from django_handleref.models import HandleRefModel
from django_inet.models import (
    ASNField,
    IPAddressField,
    IPPrefixField,
    MacAddressField,
    URLField
)
from django_peeringdb.models.concrete import *
from prngmgr.settings import *

ALERT_NONE = 0
ALERT_SUCCESS = 1
ALERT_WARNING = 2
ALERT_DANGER = 3

class PeeringRouterBase(HandleRefModel):
    hostname = models.CharField(max_length=20, unique=True)
    class Meta:
        abstract = True
    class HandleRef:
        tag = "prngrtr"

class PeeringRouter(PeeringRouterBase):
    pass

class PeeringRouterIXInterfaceBase(HandleRefModel):
    class Meta:
        abstract = True
    class HandleRef:
        tag = "prngrtriface"

class PeeringRouterIXInterface(PeeringRouterIXInterfaceBase):
    netixlan = models.OneToOneField(
        NetworkIXLan,
        default=0, related_name="+", null=True,
        limit_choices_to={'net__asn': MY_ASN}
    )
    prngrtr = models.ForeignKey(PeeringRouter, default=0, related_name="prngrtriface_set")

class PeeringSessionBase(HandleRefModel):

    PROV_NONE = 0
    PROV_PENDING = 1
    PROV_COMPLETE = 2
    PROV_OPTIONS = (
        (PROV_NONE, None),
        (PROV_PENDING, 'pending'),
        (PROV_COMPLETE, 'complete'),
    )
    provisioning_state = models.IntegerField(choices=PROV_OPTIONS, default=PROV_NONE)
    def _get_provisioning_state_alert(self):
        if self.provisioning_state == self.PROV_COMPLETE:
            return ALERT_SUCCESS
        elif self.provisioning_state == self.PROV_PENDING:
            return ALERT_WARNING
        else:
            return ALERT_NONE
    get_provisioning_state_alert = property(_get_provisioning_state_alert)

    ADMIN_NONE = 0
    ADMIN_STOP = 1
    ADMIN_START = 2
    ADMIN_OPTIONS = (
        (ADMIN_NONE, None),
        (ADMIN_STOP, 'stop'),
        (ADMIN_START, 'start'),
    )
    admin_state = models.IntegerField(choices=ADMIN_OPTIONS, default=ADMIN_NONE)
    def _get_admin_state_alert(self):
        if self.admin_state == self.ADMIN_START:
            return ALERT_SUCCESS
        elif self.admin_state == self.ADMIN_STOP:
            return ALERT_DANGER
        else:
            return ALERT_NONE
    get_admin_state_alert = property(_get_admin_state_alert)

    OPER_NONE = 0
    OPER_IDLE = 1
    OPER_CONNECT = 2
    OPER_ACTIVE = 3
    OPER_OPENSENT = 4
    OPER_OPENCONFIRM = 5
    OPER_ESTABLISHED = 6
    OPER_OPTIONS = (
        (OPER_NONE, None),
        (OPER_IDLE, "idle"),
        (OPER_CONNECT, "connect"),
        (OPER_ACTIVE, "active"),
        (OPER_OPENSENT, "opensent"),
        (OPER_OPENCONFIRM, "openconfirm"),
        (OPER_ESTABLISHED, "established"),
    )
    operational_state = models.IntegerField(choices=OPER_OPTIONS, default=OPER_NONE)
    def _get_operational_state_alert(self):
        if self.operational_state == self.OPER_ESTABLISHED:
            return ALERT_SUCCESS
        elif self.operational_state == self.OPER_NONE:
            return ALERT_NONE
        else:
            return ALERT_DANGER
    get_operational_state_alert = property(_get_operational_state_alert)

    AF_UNKNOWN = 0
    AF_IPV4 = 1
    AF_IPV6 = 2
    AF_OPTIONS = (
        (AF_UNKNOWN, 'unknown'),
        (AF_IPV4, 'ipv4'),
        (AF_IPV6, 'ipv6'),
    )
    af = models.IntegerField(choices=AF_OPTIONS, default=AF_UNKNOWN)

    class Meta:
        abstract = True
    class HandleRef:
        tag = "prngsess"

class PeeringSession(PeeringSessionBase):

    peer_netixlan = models.ForeignKey(NetworkIXLan, default=0, related_name="+", null=True)
    prngrtriface = models.ForeignKey(PeeringRouterIXInterface, default=0, related_name="prngsess_set")

    class Meta:
        unique_together = ("af", "prngrtriface", "peer_netixlan")

    def _get_local_address(self):
        if self.af == 1:
            return self.prngrtriface.netixlan.ipaddr4
        elif self.af == 2:
            return self.prngrtriface.netixlan.ipaddr6
        else:
            return None
    get_local_address = property(_get_local_address)

    def _get_remote_address(self):
        if self.af == 1:
            return self.peer_netixlan.ipaddr4
        elif self.af == 2:
            return self.peer_netixlan.ipaddr6
        else:
            return None
    get_remote_address = property(_get_remote_address)
