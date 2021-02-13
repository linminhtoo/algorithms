from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq_mails = set()
        for mail in emails:
            parts = mail.split('@')
            local, domain = parts[0], parts[1]

            local = local.replace('.', '')
            local = local.split('+')[0]

            uniq_mails.add(local + '@' + domain)
        return len(uniq_mails)