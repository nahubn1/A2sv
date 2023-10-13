class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        IP4 = queryIP.split('.')
        IP6 = queryIP.split(':')

        def noLeadingZero(number):
            if number[0] == '0' and len(number) > 1:
                return False
            return True
            
        
        def isHexaDecimal(number):
            try:
                int(number, 16)
                return True
            except ValueError:
                return False

        if len(IP4) == 4:
            if all(number.isdigit() and noLeadingZero(number) and  0 <= int(number) <= 255 for number in IP4):
                return 'IPv4'
        
        if len(IP6) == 8:
            if all(1 <= len(number) <= 4 and isHexaDecimal(number) for number in IP6):
                return 'IPv6'
        
        return 'Neither'