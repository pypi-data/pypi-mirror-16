"""
Mailchimp v3 Api SDK

"""
from .mailchimpclient import MailChimpClient
from .entities.root import Root
from .entities.authorizedapp import AuthorizedApp
from .entities.automation import Automation
from .entities.message import Message
from .entities.campaign import Campaign
from .entities.report import Report
from .entities.feedback import Feedback
from .entities.conversation import Conversation
from .entities.listabuse import ListAbuse
from .entities.listactivity import ListActivity
from .entities.memberactivity import MemberActivity
from .entities.reportactivity import ReportActivity
from .entities.reportunsubscribed import ReportUnsubscribed
from .entities.client import Client
from .entities.list import List
from .entities.growth import Growth
from .entities.template import Template
from .entities.interest import Interest
from .entities.category import Category
from .entities.goal import Goal
from .entities.member import Member
from .entities.mergefields import MergeFields
from .entities.reportabuse import ReportAbuse
from .entities.files import File
from .entities.folder import Folder
from .entities.automationemail import AutomationEmail
from .entities.automationemailqueue import AutomationEmailQueue
from .entities.automationeremovedsubscriber import AutomationRemovedSubscriber
from .entities.batches import Batches


class MailChimp(MailChimpClient):
    """
    MailChimp class to communicate with the v3 API
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the class with your user_id and secret_key
        """
        super(MailChimp, self).__init__(*args, **kwargs)
        # Authorized Apps
        self.authorized_app = AuthorizedApp(self)
        # Automation
        self.automation = Automation(self)
        self.automationemail = AutomationEmail(self)
        self.automationemailqueue = AutomationEmailQueue(self)
        self.automationeremovedsubscriber = AutomationRemovedSubscriber(self)
        # Campaigns
        self.campaign = Campaign(self)
        self.report = Report(self)
        self.campaignfeedback = Feedback(self)
        self.conversation = Conversation(self)
        self.message = Message(self)
        self.listactivity = ListActivity(self)
        self.listabuse = ListAbuse(self)
        self.client = Client(self)
        self.list = List(self)
        self.growth = Growth(self)
        self.template = Template(self)
        self.file = File(self)
        self.folder = Folder(self)
        self.category = Category(self)
        self.interest = Interest(self)
        self.memberactivity = MemberActivity(self)
        self.reportactivity = ReportActivity(self)
        self.reportunsubscribed = ReportUnsubscribed(self)
        self.goal = Goal(self)
        self.member = Member(self)
        self.mergefields = MergeFields(self)
        self.reportabuse = ReportAbuse(self)
        # Batches operations
        self.batches = Batches(self)
        # Root
        self.root = Root(self)
