# Beispiel-Klasse CheckMail
class CheckMail:
    def isValidMailAddress(self, address):
        if not address or "@" not in address or "." not in address.split("@")[-1]:
            return False
        adress_parts = address.split("@") # check if more than one @
        if len(adress_parts) > 2:
            return False
        else:
            local_part = adress_parts[0]
            domain_part = adress_parts[1]

        if not local_part or not domain_part or "." not in domain_part:
            return False

        if len(domain_part.split(".")[-1]) < 2: # check if more than two characters after .
            return False
        return True