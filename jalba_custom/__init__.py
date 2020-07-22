# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from erpnext.accounts.doctype.journal_entry.journal_entry import JournalEntry

__version__ = '0.0.1'

def set_against_account_mp(self):
    pass

JournalEntry.set_against_account = set_against_account_mp
