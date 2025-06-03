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
            adress (str): Die zu überprüfende E-Mail-Adresse.

        Returns:
            bool: True, wenn die Adresse gültig ist, sonst False.
        """

        # Ungültig, wenn keine Zeichenkette übergeben wurde
        if not isinstance(adress, str) or not adress:
            return False

        # Genau ein "@"-Zeichen muss vorhanden sein
        if adress.count("@") != 1:
            return False

        local, domain = adress.split("@")

        # Vor dem @-Zeichen muss Text stehen
        if not local:
            return False

        # Der Domain-Teil muss einen Punkt enthalten
        if "." not in domain:
            return False

        # Die Top-Level-Domain (Teil nach dem letzten Punkt) muss
        # mindestens zwei Zeichen lang sein
        if len(domain.split(".")[-1]) < 2:
            return False

        return True
