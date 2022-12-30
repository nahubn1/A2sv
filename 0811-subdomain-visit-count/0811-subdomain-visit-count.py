from collections import Counter
class Solution:
    @staticmethod
    def next_domain(string):
        dom = []
        add = False
        for s in string:
            if add: dom.append(s) 
            if s == '.': add = True
        
        return ''.join(dom)
            
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cpsub_domains = Counter([])
        for pair in cpdomains:
            count, domain = pair.split()
            count = int(count)
            while domain:
                cpsub_domains[domain] += count
                domain = self.next_domain(domain)
        res = []        
        for k, v in cpsub_domains.items():
            res.append(f'{v} {k}')
        return res