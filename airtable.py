from pyairtable import Table
import os

AIRTABLE_BASE_ID = 'appQdiMFIIjsEW2aM'
AIRTABLE_API_KEY = 'pat3PvG5VFYBSFb5v.007ade4d95461e456d5045c8b77f80f3e2cc58154ac6cb9175285a98b0df0e53'
AIRTABLE_TABLE_ID = 'tblC9XMw5NHAH6JMy'

def add_task_to_airtable(task, deadline, assign_to, attachment_url):
    #print(task,deadline)
    table = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, AIRTABLE_TABLE_ID)
    record = {
        "Task": task,
        "Deadline": deadline,
        "Assign To": assign_to,
        "Attachment": [{"url": attachment_url}] if attachment_url else [],
    }
    return table.create(record)
