# Implementieren Sie hier die Klasse CheckMail
class CheckMail:
    """
    Eine Klasse zur Überprüfung der Gültigkeit einer E-Mail-Adresse.
    """
    def isValidMailAddress(self, adress):
        """
        Überprüft, ob eine E-Mail-Adresse gültig ist.

        Eine gültige E-Mail-Adresse muss:
        - Ein "@"-Zeichen enthalten (genau eines).
        - Einen Domain-Teil mit mindestens einem Punkt haben.
        - Eine Top-Level-Domain mit mindestens zwei Zeichen haben.

        Args:
            address (str): Die zu überprüfende E-Mail-Adresse.

        Returns:
            bool: True, wenn die Adresse gültig ist, sonst False.
        """
        pass