# -*- coding: utf-8 -*-

from trac.core import *
from trac.ticket.api import ITicketChangeListener, ITicketManipulator
revision = "$Rev$"
url = "$URL$"


class TicketCloser(Component):

    implements(ITicketChangeListener)

    def ticket_changed(self, ticket, comment, author, old_values):
        """
        ticket发生变化后，判断该ticket是否有父节点。
        判断父节点下所有子几点是否结束。
        """
        #closed , accepted, new , parents
        if ticket["status"] == "closed" \
            and old_values["status"] != ticket["status"] \
            and ticket.has_key("parents"):
            #这里可以做检查。下面是检查的方法
            pass
        self.log.debug("in tickect changed %s" % tickect)
        pass

    def ticket_deleted(self, ticket):
        pass

    def ticket_created(self, ticket):
        pass
