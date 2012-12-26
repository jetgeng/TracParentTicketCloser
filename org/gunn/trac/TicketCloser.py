# -*- coding: utf-8 -*-

from trac.core import *
from trac.ticket.api import ITicketChangeListener
from trac.ticket.model import Ticket

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
        db = self.env.get_db_cnx()
        cursor = db.cursor()
        if ticket.values["status"] == "closed" and len(ticket.values["parents"]) > 0:
            #这里可以做检查。下面是检查的方法
            #通过上面这一句sql就能搞定。
            cursor.execute("SELECT count(*) as unclosed FROM ticket where id in (select child from subtickets where parent = %s) and status != 'closed'" % ticket.values["parents"])
            row = cursor.fetchone()
            try:
                unclosed = int(row[0])
                if unclosed == 0 :
                    #do close the parent
                    parentTicket = Ticket(self.env,ticket.values["parents"])
                    parentTicket._old["status"] = parentTicket.values["status"]
                    parentTicket.values["status"] = "closed"
                    parentTicket.values["resolution"] = "fixed"

                    parentTicket.save_changes(author, comment="all children has been closed")
                    self.log.debug("parent %s has been closed" % ticket.values["parents"])
                else:
                    self.log.debug("has %d unclosed children,so it did not  close")
                self.log.debug("the parent %s has %d unclosed child" % (ticket["parents"], unclosed))
            except Exception, err :
                 self.log.exception("did not get the count")

    def ticket_deleted(self, ticket):
        pass

    def ticket_created(self, ticket):
        pass
